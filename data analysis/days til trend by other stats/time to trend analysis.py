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
    ind = np.argmax(np.array( list(days_dic.values())))
    return list(days_dic.keys())[ind]

def calc_percent(days_dic):
    total = np.sum(np.array(list(days_dic.values())))
    percent = []
    for ele in days_dic.keys():
        percent.append(float(days_dic[ele])/float(total))
    return percent

def calc_standard_div(days_dic):
    return np.std(np.array(list(days_dic)))

def calc_mean_byday(vid_list_by_day, which):
    all_totals = []
    for ele in vid_list_by_day:
        total = 0
        for vid in vid_list_by_day[ele]:
            if which == "comments":
                total += vid[6]
            if which == "views":
                total += vid[3]
        total = total / len(vid_list_by_day[ele])
        all_totals.append(total)
    return all_totals

def calc_sd_byday(vid_list_by_day, which):
    all_totals = []
    for ele in vid_list_by_day:
        all_comments = []
        for vid in vid_list_by_day[ele]:
            if which == "comments":
                all_comments.append(vid[6])
            if which == "views":
                all_comments.append(vid[3])
        all_totals.append(np.std(np.array(list(all_comments))))
    return all_totals

def calc_tot_byday(vid_list_by_day, which):
    all_totals = []
    for ele in vid_list_by_day:
        total = 0
        for vid in vid_list_by_day[ele]:
            if which == "comments":
                total += vid[6]
            if which == "views":
                total += vid[3]
        all_totals.append(total)
    return all_totals

con = sqlite3.connect("../../videodata.db")
cur = con.cursor()

data = con.execute('''SELECT
id, trending_date, publish_time, views, likes, dislikes, comment_counter
FROM videodata''').fetchall()
con.close()

days_dic = {}
vid_list_by_day = {}
for ele in data:
    pub_date = datetime.datetime.strptime(ele[2].split('T')[0], "%Y-%m-%d")
    trend_date = datetime.datetime.strptime(('20'+ele[1]), "%Y.%d.%m")
    if (trend_date-pub_date).days in days_dic.keys():
        days_dic[(trend_date-pub_date).days] += 1
    else:
        days_dic[(trend_date-pub_date).days] = 1
    if (trend_date-pub_date).days in vid_list_by_day.keys():
        vid_list_by_day[(trend_date-pub_date).days].append(ele)
    else:
        vid_list_by_day[(trend_date-pub_date).days] = [ele]

days_dic = dict(sorted(days_dic.items()))
vid_list_by_day = dict(sorted(vid_list_by_day.items()))
mean = calc_mean(days_dic)
median = calc_median(vid_list_by_day)
mode = calc_mode(days_dic)
sd = calc_standard_div(days_dic)
end_data = {"mean": mean, "median": median, "mode": mode, "sd": sd}
with open('graph_data.json', 'w', encoding='utf-8') as f:
          json.dump(end_data, f)

plt.figure(figsize=(20,10))
plt.tick_params(axis='both', labelsize=10)
plt.xticks(rotation=40)
plt.xlabel("Number of days from post to trending", fontsize=16)
plt.ylabel("Number of videos", fontsize=16)
plt.bar([str(x) for x in list(days_dic.keys())], list(days_dic.values()), width=1, color='#000080')
plt.savefig('days_plot.png')
with open('total_vid_by_days.json', 'w', encoding='utf-8') as f:
    json.dump(days_dic, f)
plt.show()

total_comments_byday = calc_tot_byday(vid_list_by_day, "comments")
plt.figure(figsize=(20,10))
plt.tick_params(axis='both', labelsize=10)
plt.xticks(rotation=40)
plt.xlabel("Number of days from post to trending", fontsize=16)
plt.ylabel("Number of comments", fontsize=16)
plt.bar([str(x) for x in list(days_dic.keys())], total_comments_byday, width=1, color='#000080')
plt.savefig('total_byday_com.png')
with open('total_comments_byday.json', 'w', encoding='utf-8') as f:
    json.dump(dict(zip(list(days_dic.keys()), total_comments_byday)), f)
plt.show()


mean_byday_com = calc_mean_byday(vid_list_by_day, "comments")
plt.figure(figsize=(20,10))
plt.tick_params(axis='both', labelsize=10)
plt.xticks(rotation=40)
plt.xlabel("Number of days from post to trending", fontsize=16)
plt.ylabel("Mean number of comments", fontsize=16)
plt.bar([str(x) for x in list(days_dic.keys())], mean_byday_com, width=1, color='#800000')
plt.savefig('mean_byday_com.png')
with open('mean_comments_byday.json', 'w', encoding='utf-8') as f:
    json.dump(dict(zip(list(days_dic.keys()), mean_byday_com)), f)
plt.show()

sd_byday_com = calc_sd_byday(vid_list_by_day, "comments")
plt.figure(figsize=(20,10))
plt.tick_params(axis='both', labelsize=10)
plt.xticks(rotation=40)
plt.xlabel("Number of days from post to trending", fontsize=16)
plt.ylabel("Standard Deviation of number of comments", fontsize=16)
plt.bar([str(x) for x in list(days_dic.keys())], sd_byday_com, width=1, color='#800080')
plt.savefig('sd_byday_com.png')
with open('sd_comments_byday.json', 'w', encoding='utf-8') as f:
    json.dump(dict(zip(list(days_dic.keys()), sd_byday_com)), f)
plt.show()

total_views_byday = calc_tot_byday(vid_list_by_day, 'views')
plt.figure(figsize=(20,10))
plt.tick_params(axis='both', labelsize=10)
plt.xticks(rotation=40)
plt.xlabel("Number of days from post to trending", fontsize=16)
plt.ylabel("Number of views", fontsize=16)
plt.bar([str(x) for x in list(days_dic.keys())], total_views_byday, width=1, color='#000080')
plt.savefig('total_byday_views.png')
with open('total_views_byday', 'w', encoding='utf-8') as f:
    json.dump(dict(zip(list(days_dic.keys()), total_views_byday)), f)
plt.show()

mean_byday_views = calc_mean_byday(vid_list_by_day, "views")
plt.figure(figsize=(20,10))
plt.tick_params(axis='both', labelsize=10)
plt.xticks(rotation=40)
plt.xlabel("Number of days from post to trending", fontsize=16)
plt.ylabel("Mean number or views", fontsize=16)
plt.bar([str(x) for x in list(days_dic.keys())], mean_byday_views, width=1, color='#800000')
plt.savefig('mean_byday_views.png')
with open('mean_views_byday.json', 'w', encoding='utf-8') as f:
    json.dump(dict(zip(list(days_dic.keys()), mean_byday_views)), f)
plt.show()

sd_byday_views = calc_sd_byday(vid_list_by_day, "views")
plt.figure(figsize=(20,10))
plt.tick_params(axis='both', labelsize=10)
plt.xticks(rotation=40)
plt.xlabel("Number of days from post to trending", fontsize=16)
plt.ylabel("Standard Deviation of number of views", fontsize=16)
plt.bar([str(x) for x in list(days_dic.keys())], sd_byday_views, width=1, color='#800080')
plt.savefig('sd_byday_views.png')
with open('sd_views_byday.json', 'w', encoding='utf-8') as f:
    json.dump(dict(zip(list(days_dic.keys()), sd_byday_views)), f)
plt.show()