
def start(self):

        """

        Starts the Service.



        :Exceptions:

         - WebDriverException : Raised either when it can't start the service

           or when it can't connect to the service

        """

        try:

            cmd = [self.path]

            cmd.extend(self.command_line_args())

            if 'win32' in str(sys.platform).lower():   ### 这里判断是否是windows平台

                ###   在windows平台上就隐藏窗口

 

                startupinfo = subprocess.STARTUPINFO()

                startupinfo.dwFlags = subprocess.CREATE_NEW_CONSOLE | subprocess.STARTF_USESHOWWINDOW

                startupinfo.wShowWindow = subprocess.SW_HIDE

            else:

                startupinfo = None

 

 

            self.process = subprocess.Popen(cmd, env=self.env,

                                            close_fds=platform.system() != 'Windows',

                                            stdout=self.log_file, stderr=self.log_file,startupinfo=startupinfo)   ### 启动驱动

 

 

 

            self.PID = self.process.pid  ### 将cmd窗口的进程pid 保留   因为 窗口被隐藏了  所以在后续程序中必须考虑主控进程结束的时候必须结束掉 驱动cmd窗口进程

        except TypeError:

            raise

        except OSError as err:

            if err.errno == errno.ENOENT:

                raise WebDriverException(

                    "'%s' executable needs to be in PATH. %s" % (

                        os.path.basename(self.path), self.start_error_message)

                )

            elif err.errno == errno.EACCES:

                raise WebDriverException(

                    "'%s' executable may have wrong permissions. %s" % (

                        os.path.basename(self.path), self.start_error_message)

                )

            else:

                raise

        except Exception as e:

            raise WebDriverException(

                "The executable %s needs to be available in the path. %s\n%s" %

                (os.path.basename(self.path), self.start_error_message, str(e)))

        count = 0

        while True:

            self.assert_process_still_running()

            if self.is_connectable():

                break

            count += 1

            time.sleep(1)

            if count == 30:

                raise WebDriverException("Can not connect to the Service %s" % self.path)
