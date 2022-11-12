import pandas as pd 
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = "SimHei"

data = pd.read_csv(r"C:\Users\ekish\Desktop\data\商场营业额分析上\商场营业额分析上.csv")
data["date"] = pd.to_datetime(data["date"])
data = data.set_index("date")

#想要了解商场销售额随月份的变化
dataM = data.resample("M").sum()
plt.subplot(2,2,1)
plt.plot(dataM,color="skyblue",marker="o",label="每月销售额")
plt.xticks(rotation=45)
plt.xlabel("月份")
plt.ylabel("销售量")
plt.title("2018年到2019年每月销售额变化")
plt.legend()
#发现销售量波动大，在3月和7月放假期间销售量增加明显

#细分各个行业的销售量变化
dataCat = data.groupby(data["category"]).resample("M").sum()
happy = dataCat.loc["娱乐"]
eat = dataCat.loc["餐饮"]
sale = dataCat.loc["零售"]
service = dataCat.loc["服务"]
dataCatRe = dataCat.unstack("category")
dataCatReSum = dataCatRe.sum(axis=1)

def getPercentage(item):
    return item/dataCatReSum

percentage = dataCatRe.apply(getPercentage)
percentage.index = percentage.index.strftime("%Y-%m")
plt.subplot(2,2,1)
plt.plot(happy,color = "purple",marker="x",label="娱乐")
plt.xticks(rotation=45)
plt.legend(loc="upper left")
plt.subplot(2,2,1)
plt.plot(eat,color = "red",marker="x",label="餐饮")
plt.legend(loc="upper left")
plt.xticks(rotation=45)
plt.subplot(2,2,1)
plt.plot(sale,color = "orange",marker="x",label="零售")
plt.legend()
plt.xticks(rotation=45)
plt.subplot(2,2,1)
plt.plot(service,color = "green",marker = "x",label="服务")
plt.xticks(rotation=45)
plt.legend()
plt.subplot(2,2,2)
percentage.plot.bar(stacked=True,ax=plt.gca())

#发现零售业和餐饮行业的销售量变动也随月份变动，其中零售业销售额占比最大
#探索零售业产品销量细分
dataMo = data.groupby([data["category"],data["module"]]).resample("M").sum()
dataMo_sale = dataMo.loc["零售"]
dataMo_market =dataMo_sale.loc["商超"]
dataMo_kid = dataMo_sale.loc["童装"]
dataMo_man = dataMo_sale.loc["男装"]
dataMO_woman =dataMo_sale.loc["女装"]

plt.subplot(2,2,3)
plt.plot(dataMo_market,color="red",marker="o",label="商超")
plt.legend()
plt.xticks(rotation=45)
plt.plot(dataMo_kid,color="blue",marker="o",label="童装")
plt.legend()
plt.xticks(rotation=45)
plt.plot(dataMo_man,color="orange",marker="o",label="男装")
plt.legend()
plt.xticks(rotation=45)
plt.plot(dataMO_woman,color="green",marker="o",label="女装")
plt.legend()
plt.xticks(rotation=45)
#女装的销量在零轴中占比最大，收月份印象

plt.tight_layout()
plt.show()
