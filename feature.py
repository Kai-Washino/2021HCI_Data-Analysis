
'''
移動平均を求めてグラフ化する
'''

import pandas as pd
import matplotlib.pyplot as plt



folder1 = 'C:/Users/S2/Documents/実験結果/NJL5501/2021ver01/washino'
folder2 = 'C:/Users/S2/Documents/実験結果/NJL5501/2021ver01/perry'
folder3 = 'C:/Users/S2/Documents/実験結果/NJL5501/2021ver01/mitsunaka'
folder4 = 'C:/Users/S2/Documents/実験結果/NJL5501/2021ver01/kaito'

name1 = 'C:/Users/S2/Documents/実験結果/NJL5501/2021ver01/washino/202111021827_washino.csv'
name2 = 'C:/Users/S2/Documents/実験結果/NJL5501/2021ver01/perry/202111021853_perry.csv'
name3 = 'C:/Users/S2/Documents/実験結果/NJL5501/2021ver01/mitsunaka/202111021910_mitsunaka.csv'
name4 = 'C:/Users/S2/Documents/実験結果/NJL5501/2021ver01/kaito/202111021938_kaito.csv'


folder = 'C:/Users/S2/Documents/実験結果/NJL5501/2021ver01/washino_long'

name = 'C:/Users/S2/Documents/実験結果/NJL5501/2021ver01/washino_long/202111042245.csv'



#data = pd.read_csv(name, encoding = 'UTF8',names=('time','R_LED', 'IR_LED'), dtype=pd.Int64Dtype())
data = pd.read_csv(name4, encoding = 'UTF8',names=('time','R_LED', 'IR_LED'))

data['time'] = data['time']-data.iloc[0,0]
#print(data)

indexNames_R1 = data[(data['R_LED'] >= 370)].index
indexNames_R2 =  data[(data['R_LED'] <= 304)].index

data.drop(indexNames_R1, inplace=True)
data.drop(indexNames_R2, inplace=True)

indexNames_IR1= data[data['IR_LED'] >= 370].index
indexNames_IR2= data[data['IR_LED'] <= 304].index

data.drop(indexNames_IR1, inplace=True)
data.drop(indexNames_IR2, inplace=True)


#print(data.iloc[0,1])



#print(data)

IR_LED_feature = []
ave = []
var = []
PtoP = []

'''
#学習データ用
for i in range(15):
    sum_var = 0
    
    data4feature = data[data.time > 58000 + (142000 * i)]
    data4feature = data4feature[data4feature.time < 76700 + (142000 * i)]
    #print(data4feature)
    IR_LED_feature.append(data4feature.IR_LED)
    ave.append(sum(IR_LED_feature[i])/len(IR_LED_feature[i]))
    PtoP.append(max(IR_LED_feature[i])-min(IR_LED_feature[i]))
    
    for j in range(len(IR_LED_feature[i])):
        sum_var += abs(ave[i]-IR_LED_feature[i].iloc[j])
    var.append(sum_var/len(IR_LED_feature[i]))
#print(data4feature)
#print(IR_LED_feature)
 
#print(IR_LED_feature[11].iloc[0])
print(len(ave))
print(len(var))
print(len(PtoP))
'''

#テストデータ用
for i in range(4):
    sum_var = 0
    if(i < 3):
        data4feature = data[data.time > 58000 + (142000 * i)]
        data4feature = data4feature[data4feature.time < 76700 + (142000 * i)]
        #print(data4feature)
    else:
        data4feature = data[data.time > 58000 + (142000 * i) - 30000]
        data4feature = data4feature[data4feature.time < 76700 + (142000 * i) - 30000]
    IR_LED_feature.append(data4feature.IR_LED)
    ave.append(sum(IR_LED_feature[i])/len(IR_LED_feature[i]))
    PtoP.append(max(IR_LED_feature[i])-min(IR_LED_feature[i]))
    
    for j in range(len(IR_LED_feature[i])):
        sum_var += abs(ave[i]-IR_LED_feature[i].iloc[j])
    var.append(sum_var/len(IR_LED_feature[i]))
    
#print(data4feature)
#print(IR_LED_feature)
 
#print(IR_LED_feature[11].iloc[0])
print(len(ave))
print(len(var))
print(len(PtoP))

print(ave)
print(var)
print(PtoP)


'''

#print((data['R_LED']))
fig = plt.figure()
plt.xlabel('time[ms]')
plt.ylabel('HbT change')


#plt.plot(data['time'], data['R_LED'], linewidth = 0.3,  label = 'HbT change(Red LED)')
plt.plot(data['time'], data['IR_LED'], linewidth = 0.3,  label = 'HbT change(IR LED)')


#1つ目だけ
#plt.xlim(20000,90000)

#2つ目だけ
#plt.xlim(60000,250000)

plt.ylim(320,350)

plt.legend(bbox_to_anchor=(1, 1), loc='upper right', borderaxespad=0, fontsize=10)

for i in range(16):
    plt.vlines(30000 + (142000 * i), 0, 1000, colors='red', linestyle='dashed', linewidth=0.8)
    #香りはじめ
    plt.vlines(34000 + (142000 * i), 0, 1000, colors='red', linestyle='dashed', linewidth=0.8)
    #コップ戻す
    plt.vlines(44000 + (142000 * i), 0, 1000, colors='red', linestyle='dashed', linewidth=0.8)
    #ワッテ移動
    plt.vlines(48000 + (142000 * i), 0, 1000, colors='red', linestyle='dashed', linewidth=0.8)
    #ワッテ開始
    plt.vlines(52000 + (142000 * i), 0, 1000, colors='red', linestyle='dashed', linewidth=0.8)
    #ワッテ終わり
    plt.vlines(82000 + (142000 * i), 0, 1000, colors='red', linestyle='dashed', linewidth=0.8)

#print(name[0][num]+ '/' +'figure.png')
plt.savefig(folder+ '/' +'figure_filter.png')
'''
