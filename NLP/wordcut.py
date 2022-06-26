#!/usr/bin/python
# -*- coding: UTF-8 -*-
# cd  C:\Users\user\Desktop\Project\AI\New_DeepLearning\MyNewDeepLearning_Project\NLP
# python wordcut.py

# importing os module
import os

# Get the current working
# directory (CWD)
cwd = os.getcwd()

# Print the current working
# directory (CWD)
print("Current working directory:", cwd)

#=========================================#
#encoding=utf-8
import jieba

sentence = "獨立音樂需要大家一起來推廣，歡迎加入我們的行列！"
print("Input：", sentence)
words = jieba.cut(sentence, cut_all=False)
print("Output 精確模式 Full Mode：")
for word in words:
    print(word)

sentence = "独立音乐需要大家一起来推广，欢迎加入我们的行列！"
print("Input：", sentence)
words = jieba.cut(sentence, cut_all=False)
print("Output 精確模式 Full Mode：")
for word in words:
    print(word)
