import matplotlib.pyplot as plt
import sqlite3
import datetime
import numpy as np
import json
import math


def get_most(data, which):
    top = -math.inf
    vid = None
    for ele in data:
        if which == "views":
            if ele[2] > top:
                top = ele[2]
                vid = ele
        elif which == "comments":
            if ele[5] > top:
                top = ele[5]
                vid = ele
        elif which == "likes":
            if ele[3] > top:
                top = ele[3]
                vid = ele
        elif which == "dislikes":
            if ele[4] > top:
                top = ele[4]
                vid = ele
    return vid
        
def get_least(data, which):
    top = math.inf
    vid = None
    for ele in data:
        if which == "views":
            if ele[2] < top:
                top = ele[2]
                vid = ele
        elif which == "comments":
            if ele[5] < top:
                top = ele[5]
                vid = ele
        elif which == "likes":
            if ele[3] < top:
                top = ele[3]
                vid = ele
        elif which == "dislikes":
            if ele[4] < top:
                top = ele[4]
                vid = ele
    return vid

con = sqlite3.connect("../../videodata.db")
cur = con.cursor()

data = con.execute('''SELECT
title, channel_title, views, likes, dislikes, comment_counter
FROM videodata''').fetchall()
con.close()

complete_dic = {}


complete_dic["most_views"] = get_most(data, "views")
complete_dic["most_comments"] = get_most(data, "comments")
complete_dic["most_likes"] = get_most(data, "likes")
complete_dic["most_dislikes"] = get_most(data, "dislikes")

complete_dic["least_views"] = get_least(data, "views")
complete_dic["least_comments"] = get_least(data, "comments")
complete_dic["least_likes"] = get_least(data, "likes")
complete_dic["least_dislikes"] = get_least(data, "dislikes")


with open ("all_data.json", 'w', encoding='utf-8') as f:
    json.dump(complete_dic, f)