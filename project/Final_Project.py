import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('Gapminder.csv')
df1=df.fillna(0)
myData = df.values
myData1 = df1.values
#To find the data continent vise simply add the continent name in place of 'World" in continent variable below:
continent = 'World'
Ranked_Country = 'Pakistan'
Profitable_Data_list1 = ['DemocracyScore','EnergyUsePerPerson','GDPpercapita','Taxrevenue','IncomePerPerson','Tradebalance']
unProfitable_Data_list1 = ['ChildrenPerWoman','Poverty','Inflation','Populationdensity','Murder','Imports']
abc = Profitable_Data_list1[0]
countries = []
columnNames = list(df.head(0))
def funct(lst):
    return lst
#to find the data according to unprofitable data you just need to replace funct(Profitable_Data_list1) to funct(unProfitable_Data_list1) in below line:
Profitable_Data_list = funct(Profitable_Data_list1)
Profitable_list = []
for element in Profitable_Data_list:
    Profitable_list.append(columnNames.index(element))
rowNames = list(df.iloc[:, 0])
myData = df.values
countries = []
myDataDict = {}
CountryIndexDict = {}
j=0
answer = 0
def MaxNmbr(nmbr):
    answer = 0
    for i in myData[:,nmbr]:
        if i > answer:
            answer = i
    return answer
for j in rowNames:
    ind = []
    for i in range(len(rowNames)):
        if rowNames[i] == j:
            ind.append(i)
    CountryIndexDict[j] = ind[:]
CorrectInd = {}
CorrectIndDict = CountryIndexDict.copy()
countries1 = set(rowNames)
countries = sorted(countries1)
def NanIndexFind(columnNames,rowNames):
    NanIndDict = {}
    for k in columnNames:
        list1 = []
        for i in range(len(rowNames)):
            if df[k].isnull().iloc[i]:
                list1.append(i)
        NanIndDict[k] = list1[:]
    return NanIndDict
NanIndDict = NanIndexFind(columnNames,rowNames)
for j in range(len(columnNames)-6):
    for i in range(len(rowNames)):
        myData1[i,j+6] = myData[i,j+6]/MaxNmbr(j+6)
def AvgOfCountries(myData,lst1,lst2):
    lst = [0,0,0,0,0,0]
    for k in range(len(columnNames)-6):
        sum = 0
        counter = 0
        for j in lst1:
            if j not in lst2[columnNames[k+6]]:
                sum += myData[j,k+6]
                counter += 1
        if counter != 0:
            sum = sum / counter
        lst.append(sum)
    return lst
AvgDict = {}
for i in countries:
    AvgDict[i] = AvgOfCountries(myData1,CountryIndexDict[i],NanIndDict)
for m in range(len(columnNames)-7):
    for j in countries:
        for i in CountryIndexDict[j]:
            if myData1[i,m] == 0.0:
                myData[i,m] = AvgDict[j][m]
lst = []
lst1 = [0,0]
for i in countries:
    lst1.append(AvgDict[i][6])

TotalAvgDict = {}
sum_list = []
new_sum_list = []
def lstFunct(lst):
    return lst
Profitable_list = lstFunct(Profitable_list)
for country in countries:
    new_sum = 0
    sum = 0
    for index in range(6,len(columnNames)):
        if index in Profitable_list:
            sum += AvgDict[country][index]
    sum_list.append(sum)
sorted_profitable_sum = sorted(sum_list)
if Profitable_Data_list[0] == abc:
    sorted_profitable_sum.reverse()
def ReigonFind(reigon):
    lst = []
    countries_ind = []
    for index in range(len(rowNames)):
        if reigon != 'World' and myData[index,2] == reigon:
            lst.append(myData[index,0])
        if reigon == 'World':
            lst = countries
    my_countries = set(lst)
    for country in my_countries:
        countries_ind.append(countries.index(country))
    return my_countries , countries_ind
my_countries , countries_ind = ReigonFind(continent)
AvgList = []
for index in countries_ind:
    AvgList.append(sorted_profitable_sum[index])
indices = []
for element in sorted_profitable_sum:
    indices.append(sum_list.index(element))
def RankedFunct(sum_list,sorted_profitable_sum,my_countries):
    j=1
    rank = 0
    for index in range(len(indices)):
        if countries[indices[index]] == Ranked_Country:
            ind = index
            rank = j
            print('Rank ', j, ': ', countries[indices[index]], 'with data ', sorted_profitable_sum[index])
            j += 1
        else:
            if sorted_profitable_sum[index] != 0 and countries[indices[index]] in my_countries:
                print('Rank ', j , ': ', countries[indices[index]] , 'with data ', sorted_profitable_sum[index])
                j+=1

    print('The Rank of ', Ranked_Country, ' is ', rank , 'with data ', sorted_profitable_sum[ind])
    return 'Ranked'
data_ind = []
Data = []
countr = []
CountryNames = [Ranked_Country]
for index in range(len(indices)):
    if countries[indices[index]] == Ranked_Country:
        Data.append(sorted_profitable_sum[index])
    if sorted_profitable_sum[index] != 0 and countries[indices[index]] in my_countries:
        data_ind.append(sorted_profitable_sum[index])
        countr.append(countries[indices[index]])
# if len(data_ind) > 9:
for i in range(10):
    Data.append(data_ind[i])
    CountryNames.append(countr[i])
colors = ['green','violet','purple','yellow','red','black','orange','blue','indigo','red','pink']
fig = plt.figure(figsize=(10, 5))
plt.bar(CountryNames, Data,color = colors,
            width=0.4)
plt.xlabel("Countries")
plt.ylabel("Normalized Data")
plt.title("Pakistan Aaisa q hai")
print(RankedFunct(sum_list,sorted_profitable_sum,my_countries))
plt.show()