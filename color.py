#准备
from doctest import DocFileCase
import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams["font.sans-serif"]="SimHei"

#读取csv
df = pd.read_csv(r"C:\Users\ekish\Desktop\HAN\yequ\可视化数据1.csv")

#建立画布
plt.figure(figsize=(8,8),facecolor='white',edgecolor = "red")

#绘制折线图
plt.plot(df["date"],df["sales"],color="orange",marker="x",label="销售变化")
plt.xlabel("时间")
plt.ylabel("销售量")
plt.title("2019年到2020年7月销售量变化")

#展示
plt.legend()
plt.show()
