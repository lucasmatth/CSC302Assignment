import cv2
import matplotlib.pyplot as plt
import sqlite3
import datetime
import numpy as np
import json

def calc_mean(days_dic):
    total = np.sum(np.multiply(np.array(list(days_dic.keys())), np.array(list(days_dic.values()))))
    total = total / np.sum(np.array(list(days_dic.values())))
    return total

def calc_median(vid_list_by_day):
    lst = [i[0] for i in list(vid_list_by_day.values())]
    n = len(lst)
    med_vid = lst[int(n/2)]
    pub_date = datetime.datetime.strptime(med_vid[2].split('T')[0], "%Y-%m-%d")
    trend_date = datetime.datetime.strptime(('20'+med_vid[1]), "%Y.%d.%m")
    return (trend_date-pub_date).days

def calc_mode(days_dic):
    ind = np.argmax(np.array(list(days_dic.values())))
    return list(days_dic.keys())[ind]

def calc_percent(days_dic):
    total = np.sum(np.array(list(days_dic.values())))
    percent = []
    for ele in days_dic.keys():
        percent.append(float(days_dic[ele])/float(total))
    return percent

def calc_standard_div(days_dic):
    return np.std(np.array(list(days_dic)))

con = sqlite3.connect("../../videodata.db")
cur = con.cursor()

data = con.execute('''SELECT
id, trending_date, publish_time, views, likes, dislikes
FROM videodata''').fetchall()
con.close()

days_dic = {}
vid_list_by_day = {}
for ele in data:
    pub_date = datetime.datetime.strptime(ele[2].split('T')[0], "%Y-%m-%d")
    trend_date = datetime.datetime.strptime(('20'+ele[1]), "%Y.%d.%m")
    if (trend_date-pub_date).days in days_dic.keys():
        days_dic[(trend_date-pub_date).days] = days_dic[(trend_date-pub_date).days]+1
    else:
        days_dic[(trend_date-pub_date).days] = 1
    if (trend_date-pub_date).days in vid_list_by_day.keys():
        vid_list_by_day[(trend_date-pub_date).days].append(ele)
    else:
        vid_list_by_day[(trend_date-pub_date).days] = [ele]

days_dic = dict(sorted(days_dic.items()))

days_dic_copy = dict(days_dic)
for ele in list(days_dic_copy):
    if days_dic_copy[ele] <= 1:
        del days_dic_copy[ele]

mean = calc_mean(days_dic)
median = calc_median(vid_list_by_day)
mode = calc_mode(days_dic)
sd = calc_standard_div(days_dic)
end_data = {"mean": mean, "median": median, "mode": mode, "sd": sd}
with open('data.json', 'w', encoding='utf-8') as f:
          json.dump(end_data, f)

percent = calc_percent(days_dic)
plt.figure(figsize=(20,10))
plt.tick_params(axis='both', labelsize=10)
plt.xticks(rotation=40)
plt.bar([str(x) for x in list(days_dic.keys())], percent, width=1)
plt.savefig('days_plot.png')
