print("Hello")
print("World")
import pandas
df = pandas.read_csv('/home/user/Загрузки/titanic.csv')
print(df.columns) #1
#print(df['Name'].count()) #2
print(df.shape[0]) #2_1
males_only=df[(df['Sex'] == "male")]
print(males_only.shape[0]) #3
c=df[(df["Survived"]==1)] #4
print(c.shape[0]/df.shape[0])

males_only=df[(df['Sex'] == "male")] #5
females_only=df[(df['Sex'] == "female")]
print(males_only.shape[0])
print(females_only.shape[0])

k=df[(df["Survived"]==1)] #6
print(k.shape[0]/males_only.shape[0])

#f=df[(df["Survived"]==0)]
#one_class=df[(df['Pclass']=='абрамович')]
#two_class=df[(df['Pclass']=='хватило на timberland')]
#three_class=df[(df['Pclass']=='нищеброд')]
#print(f.shape[])

info = pandas.read_csv("/home/user/Загрузки/info.csv")
marks = pandas.read_csv("/home/user/Загрузки/marks.csv")


 #1
k=info.merge(marks, left_on='id', right_on='id2')
print(info.shape[0]-k.shape[0])
#2
g=marks.merge(info,left_on='id', right_on='id2')
print(gender.shape[0]-g.shape[0])

