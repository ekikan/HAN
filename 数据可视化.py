#準備段階
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = "SimHei"

#対象CSVを読み込む
data = pd.read_csv(r"C:\Users\ekish\Desktop\HAN\yequ\可视化数据3.csv")

#创建画布
plt.figure(figsize=(6,6),facecolor="white",edgecolor="black")

#建立时间按与曝光度的折线图
plt.bar(data["month"],data["CVR"],color="orange",width=0.7,label="转化率")
plt.ylabel("转化率")
plt.title("曝光率与转化率的关系")
plt.legend()

#建立双y轴坐标图
plt.twinx()

#建立时间与转化率的柱状图
plt.plot(data["month"],data["exposure"],color="blue",marker="o",label="曝光率")
plt.xlabel("时间")
plt.ylabel("曝光率")
plt.legend(loc="upper left")


#展现图标
plt.show()
data.info()