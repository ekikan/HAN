#准备
import pandas as pd 
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"]="SimHei"
#读取文件
data2019 = pd.read_csv(r"C:\Users\ekish\Desktop\data\Lily销售量与转化率的关系\2019年下半年订单表.csv")
data2020 = pd.read_csv(r"C:\Users\ekish\Desktop\data\Lily销售量与转化率的关系\2020年上半年订单表.csv")
#纵向合并文件
dataOrder = pd.concat([data2019,data2020])
#将下单时间转化为时间类型数据并设置为index
dataOrder["下单时间"] = pd.to_datetime(dataOrder["下单时间"])
dataOrder = dataOrder.set_index("下单时间")
#对数据按商品ID进行分类，计算每月销售数量的综合
dataOrder = dataOrder["数量"].groupby(dataOrder["商品ID"]).resample("M").sum()
#还原索引并将时间转化为年-月的形式
dataOrder = dataOrder.reset_index()
dataOrder["下单时间"] = dataOrder["下单时间"].dt.strftime("%Y-%m")
#读取浏览量的文件
dataView = pd.read_csv(r"C:\Users\ekish\Desktop\data\Lily销售量与转化率的关系\Exposure.csv")
#横向合并两项数据表
dataTotal = pd.merge(dataView,dataOrder,left_on=["ID","Month"],right_on=["商品ID","下单时间"])
#计算出购买转化率并添加到合并后的数据中
dataTotal["orderRate"] = dataTotal["数量"]/dataTotal["Exposure"]*1000000
#合并数据根据ID分类计算并抽出index
dataTotalSum = dataTotal.groupby(dataTotal["ID"]).count()
dataId = dataTotalSum.index
print(dataTotal)

#设置k为0 并遍历所有商品ID（index）
k=0
for i in dataId:
    k+=1
    #分别绘制六个不同商品的折线图y坐标的范围在0-0.3，
    plt.subplot(2,3,k)
    data1 = dataTotal[dataTotal["ID"]==i]
    plt.plot(data1["Month"],data1["orderRate"].round(2),color = "red",marker="o",label="转化率")
    plt.xticks(rotation=45)
    plt.title(i)
    plt.legend(loc="upper right")
    plt.twinx()
    plt.subplot(2,3,k)
    plt.bar(data1["Month"],data1["Exposure"],label="浏览量")
    plt.legend(loc="upper left")
    plt.ylim(0,500000)
#调整布局并显示图像
plt.legend()
plt.tight_layout()
plt.show()