import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = "SimHei"

data = pd.read_csv(r"C:\Users\ekish\Desktop\2022年合格实例 (2).csv",encoding="ANSI")
data.info()
#总共有246个值，学部，学科，eju。日语，理科，数学均有缺失值
dataEjuNull = data[data["EJU得点"].isnull()]
data.drop(index = dataEjuNull.index, inplace=True)
dataSubNull = data[data["学部"].isnull()]
data.drop(index=dataSubNull.index , inplace=True)
data.info()