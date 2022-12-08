import matplotlib.pyplot as plt
import sqlite3
import json

def calc_mean_byday(vid_list_by_day, which):
    all_totals = []
    for ele in vid_list_by_day:
        total = 0
        for vid in vid_list_by_day[ele]:
            if which == "views":
                total += vid[2]
            if which == 'likes':
                total += vid[3]
            if which == 'comments':
                total += vid[4]
        total = total / len(vid_list_by_day[ele])
        all_totals.append(total)
    return all_totals

def calc_tot_by_hour(hours_dic_vids, which):
    all_totals = []
    for ele in hours_dic_vids:
        total = 0
        for vid in hours_dic_vids[ele]:
            if which == 'views':
                total += vid[2]
            if which == 'likes':
                total += vid[3]
            if which == 'comments':
                total += vid[4]
        all_totals.append(total)
    return all_totals

con = sqlite3.connect("../../videodata.db")
cur = con.cursor()

data = con.execute('''SELECT
id, publish_time, views, likes, comment_counter
FROM videodata''').fetchall()
con.close()

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

plt.figure(figsize=(40,10))
plt.tick_params(axis='both', labelsize=9)
plt.xticks(rotation=50)
plt.xlabel('Hour of day', fontsize=16)
plt.ylabel('Number of videos', fontsize=16)
plt.bar([str(x) for x in list(hours_dic_num.keys())], list(hours_dic_num.values()), width=1, color='#000080')
plt.savefig('num_vid_by_hour.png')
with open('total_vid_by_hour.json', 'w', encoding='utf-8') as f:
    json.dump(dict(zip(list(hours_dic_num.keys()), list(hours_dic_num.values()))), f)
plt.show()

total_views_by_hour = calc_tot_by_hour(hours_dic_vids, 'views')
plt.figure(figsize=(40,10))
plt.tick_params(axis='both', labelsize=9)
plt.xticks(rotation=50)
plt.xlabel('Hour of day', fontsize=16)
plt.ylabel('Total views', fontsize=16)
plt.bar([str(x) for x in list(hours_dic_num.keys())], total_views_by_hour, width=1, color='#000080')
plt.savefig('total_views_by_hour.png')
with open('total_views_by_hour.json', 'w', encoding='utf-8') as f:
    json.dump(dict(zip(list(hours_dic_num.keys()), total_views_by_hour)), f)
plt.show()

mean_views_by_hour = calc_mean_byday(hours_dic_vids, "views")
plt.figure(figsize=(40,10))
plt.tick_params(axis='both', labelsize=9)
plt.xticks(rotation=50)
plt.xlabel("Hours of day", fontsize=16)
plt.ylabel("Mean number of views", fontsize=16)
plt.bar([str(x) for x in list(hours_dic_num.keys())], mean_views_by_hour, width=1, color='#800000')
plt.savefig('mean_views_by_hour.png')
with open('mean_views_by_hour.json', 'w', encoding='utf-8') as f:
    json.dump(dict(zip(list(hours_dic_num.keys()), mean_views_by_hour)), f)
plt.show()

total_likes_by_hour = calc_tot_by_hour(hours_dic_vids, 'likes')
plt.figure(figsize=(40,10))
plt.tick_params(axis='both', labelsize=9)
plt.xticks(rotation=50)
plt.xlabel('Hour of day', fontsize=16)
plt.ylabel('Total likes', fontsize=16)
plt.bar([str(x) for x in list(hours_dic_num.keys())], total_likes_by_hour, width=1, color='#000080')
plt.savefig('total_likes_by_hour.png')
with open('total_likes_by_hour.json', 'w', encoding='utf-8') as f:
    json.dump(dict(zip(list(hours_dic_num.keys()), total_likes_by_hour)), f)
plt.show()

mean_likes_by_hour = calc_mean_byday(hours_dic_vids, "likes")
plt.figure(figsize=(40,10))
plt.tick_params(axis='both', labelsize=9)
plt.xticks(rotation=50)
plt.xlabel("Hours of day", fontsize=16)
plt.ylabel("Mean number of likes", fontsize=16)
plt.bar([str(x) for x in list(hours_dic_num.keys())], mean_likes_by_hour, width=1, color='#800000')
plt.savefig('mean_likes_by_hour.png')
with open('mean_likes_by_hour.json', 'w', encoding='utf-8') as f:
    json.dump(dict(zip(list(hours_dic_num.keys()), mean_likes_by_hour)), f)
plt.show()

total_comments_by_hour = calc_tot_by_hour(hours_dic_vids, 'comments')
plt.figure(figsize=(40,10))
plt.tick_params(axis='both', labelsize=9)
plt.xticks(rotation=50)
plt.xlabel('Hour of day', fontsize=16)
plt.ylabel('Total comments', fontsize=16)
plt.bar([str(x) for x in list(hours_dic_num.keys())], total_comments_by_hour, width=1, color='#000080')
plt.savefig('total_comments_by_hour.png')
with open('total_comments_by_hour.json', 'w', encoding='utf-8') as f:
    json.dump(dict(zip(list(hours_dic_num.keys()), total_comments_by_hour)), f)
plt.show()

mean_comments_by_hour = calc_mean_byday(hours_dic_vids, "comments")
plt.figure(figsize=(40,10))
plt.tick_params(axis='both', labelsize=9)
plt.xticks(rotation=50)
plt.xlabel("Hours of day", fontsize=16)
plt.ylabel("Mean number of comments", fontsize=16)
plt.bar([str(x) for x in list(hours_dic_num.keys())], mean_comments_by_hour, width=1, color='#800000')
plt.savefig('mean_comments_by_hour.png')
with open('mean_comments_by_hour.json', 'w', encoding='utf-8') as f:
    json.dump(dict(zip(list(hours_dic_num.keys()), mean_comments_by_hour)), f)
plt.show()

