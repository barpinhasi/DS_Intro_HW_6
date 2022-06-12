import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('LP_destinations.csv',encoding='latin-1')

####1####
count = df['Descrption'].str.split().str.len()
df['num_of_words'] = count

####2####
No_punct_description = [] 
b ="\,.:-;…,"
for line in df['Descrption']:
    for char in b:
        line = line.replace(char,"")
    No_punct_description.append(line)
df['No_punct_description'] = No_punct_description

####3+4+5####
listrest = []
listmeu = []
listbeach = []
for index,row in df.iterrows():
    str_count1 = row["Descrption"].count("restaurant")
    str_count2 = row["Descrption"].count("museum")
    str_count3 = row["Descrption"].count("ocean") + row["Descrption"].count("beach") + row["Descrption"].count("sea")
    listrest.append(str_count1)
    listmeu.append(str_count2)
    listbeach.append(str_count3)
df['has_restaurants'] = listrest
df['has_museums'] = listmeu
df['has_beaches'] = listbeach

####6####
avg = df['num_of_words'].mean()

####7####
maxi = df['num_of_words'].max()
k = df.loc[df['num_of_words'] == maxi]['city']
print(k)

####8####
df.hist('num_of_words')

####9####
plt.scatter(df['has_beaches'], df['has_restaurants'])
plt.xlabel("number of beaches")
plt.ylabel("number of resturants")

####10####
plt.scatter(df['has_museums'], df['has_beaches'])
plt.xlabel("number of museums")
plt.ylabel("number of _beaches")


    

