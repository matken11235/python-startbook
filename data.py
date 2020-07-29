#coding:utf-8

import numpy as np

# MNISTデータセットから配列として読み込む
data_file = open("MNIST_dataset/mnist_test.csv", 'r')
data_list = data_file.readlines()
data_file.close()

for i in range(len(data_list)):
	# ","(カンマ)を"\n"(改行コード)に置き換えて代入
	all_values = data_list[i].replace(',','\n')
	# "FileNumber as TeacherNumber"という命名規則で書き込み
	f = open('output/'+str(i)+'.txt', 'w')
	# 最後の要素は\nであるため排除して書き込む
	f.write(all_values[0:len(all_values)-1])
	f.close()
