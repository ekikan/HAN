#准备
import pandas as pd

#1-寻找相似物品
#读取并拼接数据
movies = pd.read_csv(r"C:\Users\ekish\Desktop\data\movie\movies.csv")
ratings = pd.read_csv(r"C:\Users\ekish\Desktop\data\movie\ratings.csv")
result = pd.merge(movies,ratings)
#构建【用户-物品数据透视表】
movieRatings = result.pivot_table(index="用户id",columns="电影名",values="评分")
#计算每两部电影之间的皮尔逊相关系数
moviesPearson = movieRatings.corr(method="pearson")
#2-寻找目标用户感兴趣的物品，预测目标用户对未评分过物品的感兴趣程度
#获取目标用户评分过的每一部电影数据，以及评分过电影的相关电影
user1Ratings = movieRatings.loc[1].dropna()
name = user1Ratings.index
score = user1Ratings.values
#计算目标评分过物品与其他未评分过物品的皮尔逊相关系数
likePearson = moviesPearson[name].drop(index=name)
#计算用户对评分过物品的评分与皮尔逊相关系数的乘积并求和计算出目标用户对为评分过物品的感兴趣程度列表
prod = score*likePearson
prodSum = prod.sum(axis=1)
#针对目标用户和推荐规则做出推荐
prodSum = prodSum.sort_values(ascending=False)
prodSum = prodSum.index[0:5]
movieList = prodSum.values
print(movieRatings)
print(moviesPearson)
print(f"推荐给目标用户1的带电影列表是{movieList}。")
