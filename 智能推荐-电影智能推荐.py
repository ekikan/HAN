#准备
import pandas as pd
import matplotlib.pyplot as plt

#读取文件
ratings = pd.read_csv(r"C:\Users\ekish\Desktop\data\movie\ratings.csv",sep = "::", header=None , names=["用户id","电影id","评分","评分时间"])
movies = pd.read_csv(r"C:\Users\ekish\Desktop\data\movie\movies.csv")

#储存文件
ratings.to_csv(r"C:\Users\ekish\Desktop\data\movie\ratings.csv",index = False)
movies.to_csv(r"C:\Users\ekish\Desktop\data\movie\movies.csv",index = False)

#重新读取
ratings = pd.read_csv(r"C:\Users\ekish\Desktop\data\movie\ratings.csv",usecols = ["用户id","电影id","评分"])
movies = pd.read_csv(r"C:\Users\ekish\Desktop\data\movie\ratings.csv",usecols=["电影id","电影名"])
#横向合并两个数据表创建数据库
movieratings = pd.merge(ratings,movies)
print(ratings)
print(movies)
print(movieratings)