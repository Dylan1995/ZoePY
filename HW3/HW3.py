# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 18:06:23 2018

@author: breezefay
"""

import csv
import prettytable as pt;



csv_file=csv.reader(open("E:\zoePY\hw3\Data\Grade.csv",'r'))
lines = csv_file;

#df = pd.read_csv(csv_file)

#df.head()

###get data from Grade.csv and find the id in case of being unable to get value
list1 = []
for line in lines:
    list1.append(line)
    #mandGra = line[1]
    #engGra = line[2]
   # mathGra = line[3]
    #linej = line[1][1]
    
    #a = np.array(line[1])
    #b = np.array(line[2])
    #c = a + b

 

##not finish yet TT

aveGG = ["平均"]
for j in range(1,4):
    temp =0
    cont =0
    for i in range(1,9):
        
        temp = int(list1[i][j])
        cont = cont + temp
        ave = cont/8
        if i == 8:
            aveGG.append(str(ave))
    
            
       # '''
        #if j == 1:
         #   ave = cont / 8
       # else:
         #   ave = cont /(8*(j-1))
       # '''
    
    #aveGG.append(str(cont))

print(aveGG)




avePPerG = []
for j in range(1,9):
    tempp = 0
    contt = 0
    for i in range(1,4):
        
        tempp = int(list1[j][i])
        contt = contt + tempp
        avePGG = contt / 3
        if i == 3:
            avePGG = round((avePGG)+0.01,2)
            avePPerG.append(str(avePGG))
print(avePPerG)


## calculate the value

'''
temp1 = 0
cont1 = 0

for i in range(1,9):
    temp1 = int(list1[i][1])
    cont1 = cont1 + temp1

aveMand = cont1/8

temp2 = 0
cont2 = 0

for i in range(1,9):
    temp2 = int(list1[i][2])
    cont2 = cont2 + temp2
aveEng = cont2 / 8

temp3 = 0
cont3 = 0
for i in range(1,9):
    temp3 = int(list1[i][3])
    cont3 = cont3 + temp3
aveMath = cont3 / 8

aveManEngMat = (aveMand + aveEng + aveMath) /3

aveG =["平均",str(aveMand),str(aveEng),str(aveMath)]

#print(aveG)

temp4 = 0
cont4 = 0
for i in range(1,4):
    temp4 = int(list1[1][i])
    cont4 = cont4 + temp4
BluePerG = round(cont4 / 3+0.01,2)
temp5 = 0
cont5 = 0
for i in range(1,4):
    temp5 = int(list1[2][i])
    cont5 = cont5 + temp5
fishPerG = round(cont5 /3+0.01,2)
temp6 = 0
cont6 = 0
for i in range(1,4):
    temp6 = int(list1[3][i])
    cont6 = cont6 + temp6
HHPerG = round(cont6/3+0.01,2)
temp7 = 0
cont7 = 0
for i in range(1,4):
    temp7 = int(list1[4][i])
    cont7 = cont7 + temp7
ZoePerG = round(cont7/3+0.01,2)
temp8 = 0
cont8 = 0
for i in range(1,4):
    temp8 = int(list1[5][i])
    cont8 = cont8 + temp8
YenPerG = round(cont8/3+0.01,2)
temp9 = 0
cont9 = 0
for i in range(1,4):
    temp9 = int(list1[6][i])
    cont9 = cont9 + temp9    
KaiPerG = round(cont9/3+0.01,2)    
temp10 = 0
cont10 = 0
for i in range(1,4):
    temp10 = int(list1[7][i])
    cont10 = cont10 + temp10
XianPerG= round(cont10/3+0.01,2)
temp11 = 0
cont11 = 0
for i in range(1,4):
    temp11 = int(list1[8][i])
    cont11 = cont11 + temp11
ShihPerG = round(cont11/3+0.001,2)
    
avePerG =[str(BluePerG),str(fishPerG),str(HHPerG),str(ZoePerG),str(YenPerG),str(KaiPerG),str(XianPerG),str(ShihPerG),str(aveManEngMat)]

#print(avePerG)
'''
from prettytable import from_csv 
fp = open("E:\zoePY\hw3\Data\Grade.csv", "r") 

pt = csv.reader(fp)
pt = from_csv(fp)
pt.add_row(aveG)
pt.add_column("個人平均",avePerG)
print(pt)
fp.close() 








        
    
