import tweepy
import main
import csv
import pandas as pd
from csv import reader
import matplotlib.pyplot as plt
import numpy as np



client= tweepy.Client(bearer_token=main.BEARER_TOKEN) #
query=' #Russian -is:retweet'

counts =client.get_recent_tweets_count(query=query, granularity='day')
file_name='name.csv'
with open(file_name, 'a') as filehandler:

   for counts in counts.data:
    #print(counts)
    filehandler.write('%s\n' %counts)

filehandler.close()
count=0
value_array=[]
time_array=[]
with open('name.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        column=[]
        #print(row[0]+" "+row[2])
        column=row[2].split(": ")
       #print(column[1])
        value=column[1][0:len(column[1])-1]
        #print(value)
        value_array.append(value)
        time_array.append(count)
        count=count+1
plt.rcParams["figure.figsize"] = [7.5, 3.5]
plt.rcParams["figure.autolayout"] = True
plt.title("Line graph")
plt.plot(time_array,value_array,'--')
plt.xlabel("zilele")
plt.ylabel("numarul de tweet-uri")
plt.show()
print(time_array)