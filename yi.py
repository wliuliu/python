f=open(‪D:\lianxing\shangke\\JAVA笔记.text)
#文件每一行，统计每个单词出现字数
#键：单词        次数：值
word_freq={}
for line in f:
    words=line.split()
    for word in words:
        if word in word_freq:
            word_freq[word]+=1
        else:
            word_freq[word]=1
for word in word_freq:
    print(word,word_freq[word])
