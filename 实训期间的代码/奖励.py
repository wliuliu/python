print('\n'.join('  '.join('{}*{}={}'.format(j, i, i * j) for j in range(1, i + 1)) for i in range(1, 10)))
