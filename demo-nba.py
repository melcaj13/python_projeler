import pandas as pd
import numpy as np

data = pd.read_csv("datasets/nba.csv")
df = pd.DataFrame(data)
result = df

# 1 - İlk 10 kaydı getiriniz.
  #result = df.head(10)
# 2 - Toplam kaç kayıt vardır?
  #result = df.count().sum()
  #result = len(df.index)
# 3 - Tüm oyuncuların toplam maaş ortalamsı nedir?
  #result = df["Salary"].mean()
# 4 - En yüksek maaşı ne kadardır.
  #result = df["Salary"].max()
# 5 - En yüksek maaşı alan oyuncu kimdir.
  #result = df.loc[df["Salary"].idxmax(), ["Name", "Salary","Age"]]
# 6 - Yaşı 20-25 arasında oyucuların isim ve oynadıkalrı takımı getiriniz.
  #result = df.loc[(df["Age"] >= 20) & (df["Age"] <= 25) ,["Name","Team","Age"]]
  #result = df[(df["Age"] >= 20) & (df["Age"] <= 25)][["Name","Team","Age"]].sort_values("Age",ascending=False)
# 7 - "john Holland" isimli oyuncunun oydaığı takım nedir
  #result = df[df["Name"] == "john Holland"]["Team"].iloc[0]
# 8 - Takımlara göre oyuncuların ortalama maaş bilgisi nedir
  #result = df.groupby("Team")["Salary"].mean()
# 9 - Kaç farklı takım mevcuttur.
  #result = len(df.groupby("Team"))
  #result = df["Team"].nunique()
# 10 - Her takımda kaç oyuncu oynamaktadır
  #result = df.groupby("Team")["Name"].size()
  #result = df["Team"].value_counts()

# 11 - İsmi İçinde "and" geçen kaydı bulunuz.
  #result = df[df["Name"].str.contains("and", case=False, na=False)]
df.dropna(inplace = True)
#result= df[df["Name"].str.contains("and")]
def str_find(name):
    if "and" in name.lower():
        return True
    return False
result= df[df["Name"].apply(str_find)]


print(result)