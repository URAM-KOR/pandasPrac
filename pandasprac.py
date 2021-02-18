import pandas as pd

#리스트
list_tmp = [1,2,3]
#print(list_tmp)

#시리즈 만들기
s1 = pd.core.series.Series([1,2,3])
s2 = pd.core.series.Series(['one','two','three'])
#print(pd.DataFrame(data=dict(num=s1, word=s2)))

#csv불러오기
df = pd.read_csv('data/friend_list.csv')
#print(df)
#print(df.head())   #head:앞에서 5개 기본//
#print(df.head(2))
#print(df.tail(3))  #tail:뒤에서

#tab으로 구분된 데이터 불러오기

df = pd.read_csv('data/friend_list_tab.txt',delimiter='\t') #delimiter: 구분자 설정

#print(df)

# 조작

df = pd.read_csv('data/friend_list.csv',header = None) #header 없애기
print(df)

df.columns=['name','age','job'] #header 추가

print(df)