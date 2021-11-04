
'''
移動平均を求めてグラフ化する
'''

import pandas as pd
import matplotlib.pyplot as plt


folder1 = 'C:/Users/S2/Documents/実験結果/NJL5501/2021ver01/washino'
folder2 = 'C:/Users/S2/Documents/実験結果/NJL5501/2021ver01/perry'
folder3 = 'C:/Users/S2/Documents/実験結果/NJL5501/2021ver01/mitsunaka'
folder4 = 'C:/Users/S2/Documents/実験結果/NJL5501/2021ver01/kaito'

name1 = 'C:/Users/S2/Documents/実験結果/NJL5501/2021ver01/washino/202111021827_washino'
name2 = 'C:/Users/S2/Documents/実験結果/NJL5501/2021ver01/perry/202111021853_perry'
name3 = 'C:/Users/S2/Documents/実験結果/NJL5501/2021ver01/mitsunaka/202111021910_mitsunaka'
name4 = 'C:/Users/S2/Documents/実験結果/NJL5501/2021ver01/kaito/202111021938_kaito'

name = [folder1, folder2, folder3, folder4], [name1, name2, name3, name4]
 
#誰のデータを使うか
num = 3

print(name[1][num])

#data = pd.read_csv(name, encoding = 'UTF8',names=('time','R_LED', 'IR_LED'), dtype=pd.Int64Dtype())
data = pd.read_csv(name[1][num] + '.csv', encoding = 'UTF8',names=('time','R_LED', 'IR_LED'))
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
print(data.iloc[3,1])

data['time'] = data['time']-data.iloc[0,0]


SMAdata_R_LED = []
SMAdata_IR_LED = []

for i in range(len(data['R_LED'])):
    sum = 0
    if(i < 9):
        SMAdata_R_LED.append(0)
    if(i >= 9):
        for j in range(10):
            sum =+ data.iloc[i-j,1]
        SMAdata_R_LED.append(sum/10)
        
for i in range(len(data['IR_LED'])):
    sum = 0
    if(i < 9):
        SMAdata_IR_LED.append(0)
    if(i >= 9):
        for j in range(10):
            sum =+ data.iloc[i-j,2]
        SMAdata_IR_LED.append(sum/10)

print(SMAdata_R_LED)
print(SMAdata_IR_LED)
        
#print((data['R_LED']))
fig = plt.figure()
plt.xlabel('time[ms]')
plt.ylabel('HbT change')

print(data)

plt.plot(data['time'], SMAdata_R_LED, linewidth = 0.3,  label = 'HbT change(Red LED)')
plt.plot(data['time'], SMAdata_IR_LED, linewidth = 0.3,  label = 'HbT change(IR LED)')

plt.ylim(30,40)

#1つ目だけ
#plt.xlim(20000,90000)

#2つ目だけ
#plt.xlim(60000,250000)

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

plt.savefig(name[0][num]+ '/' +'figure_SMA.png')
 
