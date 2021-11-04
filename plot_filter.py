
'''
移動平均を求めてグラフ化する
'''

import pandas as pd
import matplotlib.pyplot as plt


folder = 'C:/Users/S2/Documents/実験結果/NJL5501/2021ver01/washino_long'

name = 'C:/Users/S2/Documents/実験結果/NJL5501/2021ver01/washino_long/202111042245.csv'

#誰のデータを使うか

#data = pd.read_csv(name, encoding = 'UTF8',names=('time','R_LED', 'IR_LED'), dtype=pd.Int64Dtype())
data = pd.read_csv(name, encoding = 'UTF8',names=('time','R_LED', 'IR_LED'))
data.replace(['nan'],0)
data.dropna()

indexNames_R1 = data[(data['R_LED'] >= 350)].index
indexNames_R2 =  data[(data['R_LED'] <= 320)].index

data.drop(indexNames_R1, inplace=True)
data.drop(indexNames_R2, inplace=True)

indexNames_IR1= data[data['IR_LED'] >= 350].index
indexNames_IR2= data[data['IR_LED'] <= 320].index

data.drop(indexNames_IR1, inplace=True)
data.drop(indexNames_IR2, inplace=True)


print(data.iloc[0,1])

data['time'] = data['time']-data.iloc[0,0]


        
#print((data['R_LED']))
fig = plt.figure()
plt.xlabel('time[ms]')
plt.ylabel('HbT change')

print(data)

#plt.plot(data['time'], data['R_LED'], linewidth = 0.3,  label = 'HbT change(Red LED)')
plt.plot(data['time'], data['IR_LED'], linewidth = 0.3,  label = 'HbT change(IR LED)')


#1つ目だけ
#plt.xlim(20000,90000)

#2つ目だけ
#plt.xlim(60000,250000)

plt.ylim(320,350)

plt.legend(bbox_to_anchor=(1, 1), loc='upper right', borderaxespad=0, fontsize=10)

#水
#コップ動かす
plt.vlines(30000, 0, 1000, colors='red', linestyle='dashed', linewidth=0.8)
#香りはじめ
plt.vlines(34000, 0, 1000, colors='red', linestyle='dashed', linewidth=0.8)
#コップ戻す
plt.vlines(44000, 0, 1000, colors='red', linestyle='dashed', linewidth=0.8)
#ワッテ移動
plt.vlines(48000, 0, 1000, colors='red', linestyle='dashed', linewidth=0.8)
#ワッテ開始
plt.vlines(52000, 0, 1000, colors='red', linestyle='dashed', linewidth=0.8)
#ワッテ終わり
plt.vlines(82000, 0, 1000, colors='red', linestyle='dashed', linewidth=0.8)


#レモン
#コップ動かす
plt.vlines(172000, 0, 1000, colors='red', linestyle='dashed', linewidth=0.8)
#香りはじめ
plt.vlines(176000, 0, 1000, colors='red', linestyle='dashed', linewidth=0.8)
#コップ戻す
plt.vlines(186000, 0, 1000, colors='red', linestyle='dashed', linewidth=0.8)
#ワッテ移動
plt.vlines(190000, 0, 1000, colors='red', linestyle='dashed', linewidth=0.8)
#ワッテ開始
plt.vlines(194000, 0, 1000, colors='red', linestyle='dashed', linewidth=0.8)
#ワッテ留置
plt.vlines(224000, 0, 1000, colors='red', linestyle='dashed', linewidth=0.8)

#水
#コップ動かす
plt.vlines(314000, 0, 1000, colors='red', linestyle='dashed', linewidth=0.8)
#香りはじめ
plt.vlines(318000, 0, 1000, colors='red', linestyle='dashed', linewidth=0.8)
#コップ戻す
plt.vlines(328000, 0, 1000, colors='red', linestyle='dashed', linewidth=0.8)
#ワッテ移動
plt.vlines(332000, 0, 1000, colors='red', linestyle='dashed', linewidth=0.8)
#ワッテ開始
plt.vlines(336000, 0, 1000, colors='red', linestyle='dashed', linewidth=0.8)
#ワッテ留置
plt.vlines(366000, 0, 1000, colors='red', linestyle='dashed', linewidth=0.8)

#水
#コップ動かす
plt.vlines(456000, 0, 1000, colors='red', linestyle='dashed', linewidth=0.8)
#香りはじめ
plt.vlines(460000, 0, 1000, colors='red', linestyle='dashed', linewidth=0.8)
#コップ戻す
plt.vlines(470000, 0, 1000, colors='red', linestyle='dashed', linewidth=0.8)
#ワッテ移動
plt.vlines(474000, 0, 1000, colors='red', linestyle='dashed', linewidth=0.8)
#ワッテ開始
plt.vlines(478000, 0, 1000, colors='red', linestyle='dashed', linewidth=0.8)
#ワッテ留置
plt.vlines(508000, 0, 1000, colors='red', linestyle='dashed', linewidth=0.8)

#print(name[0][num]+ '/' +'figure.png')
plt.savefig(folder+ '/' +'figure_filter.png')
 
