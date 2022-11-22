import matplotlib.pyplot as plt
import sqlite3
import datetime
import numpy as np
import json

def calc_mean_byday(vid_list_by_day, which):
    all_totals = []
    for ele in vid_list_by_day:
        total = 0
        for vid in vid_list_by_day[ele]:
            if which == "views":
                total += vid[2]
        total = total / len(vid_list_by_day[ele])
        all_totals.append(total)
    return all_totals

    

con = sqlite3.connect("../../videodata.db")
cur = con.cursor()

data = con.execute('''SELECT
id, publish_time, views
FROM videodata''').fetchall()
con.close()

print(data[0][1].split('T')[1].split(":")[0])

hours_dic_num = {}
hours_dic_vids = {}

for ele in data:
    if int(ele[1].split('T')[1].split(":")[0]) in hours_dic_num:
        hours_dic_num[int(ele[1].split('T')[1].split(":")[0])] += 1
    else:
        hours_dic_num[int(ele[1].split('T')[1].split(":")[0])] = 1
    if int(ele[1].split('T')[1].split(":")[0]) in hours_dic_vids:
        hours_dic_vids[int(ele[1].split('T')[1].split(":")[0])].append(ele)
    else:
        hours_dic_vids[int(ele[1].split('T')[1].split(":")[0])] = [ele]

hours_dic_num = dict(sorted(hours_dic_num.items()))
hours_dic_vids = dict(sorted(hours_dic_vids.items()))

plt.figure(figsize=(20,10))
plt.tick_params(axis='both', labelsize=10)
plt.xticks(rotation=40)
plt.bar([str(x) for x in list(hours_dic_num.keys())], list(hours_dic_num.values()), width=1)
plt.savefig('num_vid_by_hour.png')
plt.show()

mean_byday_views = calc_mean_byday(hours_dic_vids, "views")
plt.figure(figsize=(20,10))
plt.tick_params(axis='both', labelsize=10)
plt.xticks(rotation=40)
plt.bar([str(x) for x in list(hours_dic_num.keys())], mean_byday_views, width=1)
plt.savefig('mean_views_by_hour.png')
plt.show()
#sd_byday_views = calc_sd_byday(hours_dic_vids, "views")
