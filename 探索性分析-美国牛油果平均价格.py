# 准备
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = "SimHei"
#读取文件
data = pd.read_csv(r"C:\Users\ekish\Desktop\data\美国牛油果平均价格\avocado.csv")
data["Date"] = pd.to_datetime(data["Date"])
data = data.set_index("Date")
#根据城市region将数据分组采样聚合来获取纽约和芝加哥两个城市每个月的牛油果平均价格
regionAve = data["AveragePrice"].groupby(data["region"]).resample("M").mean()
NewYorkAve = regionAve["NewYork"]
ChicagoAve = regionAve["Chicago"]
USAAve = data["AveragePrice"].resample("M").mean()
print(USAAve)
#以月份为x轴绘制折线图
plt.plot(NewYorkAve,color = "skyblue",marker = "o",label="纽约价格水平")
plt.plot(ChicagoAve,color = "blue",marker = "o",label ="芝加哥价格水平")
plt.plot(USAAve,color = "green",marker = "o",label ="全美价格水平")
#设置x轴，y轴，图例
plt.xlabel("时间")
plt.ylabel("价格水平")
plt.legend(loc="upper left")
#展示图像
plt.show()