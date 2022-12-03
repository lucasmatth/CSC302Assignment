import matplotlib.pyplot as plt
import sqlite3
import datetime
import numpy as np
import json
import math

con = sqlite3.connect("../../videodata.db")
cur = con.cursor()

data = con.execute('''SELECT
id, publish_time, views, comment_counter, likes, dislikes
FROM videodata''').fetchall()

count = con.execute('''SELECT id, COUNT(*) FROM videodata''').fetchall()
print(count)
con.close()

lowest_views = math.inf
highest_views = -math.inf
for vid in data:
    if vid[2] < lowest_views:
        lowest_views = vid[2]
    if vid[2] > highest_views:
        highest_views = vid[2]

print(lowest_views)
print(highest_views)
total_range = highest_views-lowest_views
split_num = total_range//60
print(total_range)
print(split_num)

views_dic_num = {}
views_dic_vids = {}

lower = 157
upper = lower+794486
for i in range(75):
    views_dic_num[str(lower)+"-"+str(upper)] = 0
    views_dic_vids[str(lower)+"-"+str(upper)] = []
    lower = upper
    upper = upper+1012924

for vid in data:
    for ind in views_dic_num:
        if vid[2] >= int(ind.split("-")[0]) and vid[2] < int(ind.split("-")[1]):
            views_dic_num[ind] += 1
            views_dic_vids[ind].append(vid)

test = 0
for val in views_dic_vids.values():
    test += len(val)

print(test)

plt.figure(figsize=(20,10))
plt.tick_params(axis='both', labelsize=9)
plt.xticks(rotation=40)
plt.xlabel('Total views range', fontsize=16)
plt.ylabel('Number of videos', fontsize=16)
plt.bar(list(views_dic_num.keys()), list(views_dic_num.values()), width=1, color='#000080')
plt.savefig('num_of_vid_by_view.png')
with open('total_vid_by_view.json', 'w', encoding='utf-8') as f:
    json.dump(dict(zip(list(views_dic_num.keys())), list(views_dic_num.keys())), f)
plt.show()
