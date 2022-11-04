import sqlite3

diff_files = ["RUvideos", "CAvideos", "DEvideos", "USvideos",
              "INvideos", "GBvideos", "FRvideos", "MXvideos",
              "KRvideos", "JPvideos"]

con = sqlite3.connect("videodata.db")
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS videodata(
id INTEGER PRIMARY KEY AUTOINCREMENT,
video_id VARCHAR(20) NOT NULL,
trending_date VARCHAR(10) NOT NULL,
title VARCHAR(102) NOT NULL,
channel_title VARCHAR(52) NOT NULL,
category_id INTEGER NOT NULL,
publish_time DATETIME NOT NULL,
time_to_trend DATETIME,
tags BLOB NOT NULL,
views INTEGER NOT NULL,
likes INTEGER NOT NULL,
dislikes INTEGER NOT NULL,
comment_counter INTEGER NOT NULL,
thumbnail_link TEXT NOT NULL,
description BLOB NOT NULL,
region VARCHAR(2) NOT NULL);
''')

for fl in diff_files:
    con2 = sqlite3.connect(fl+".db")
    cur2 = con2.cursor()
    the_stuff = con2.execute('''SELECT video_id, trending_date, title, channel_title, category_id,
publish_time, tags, views, likes, dislikes, comment_counter, thumbnail_link, description
FROM {}
WHERE comments_disabled =? AND ratings_disabled=? AND video_error_or_removed =?
ORDER BY random()
LIMIT 4300'''.format(fl), ('FALSE', 'FALSE', 'FALSE')).fetchall()
    for ele in the_stuff:
        cur.execute('''INSERT into videodata
(video_id, trending_date, title, channel_title, category_id, publish_time,
tags, views, likes, dislikes, comment_counter, thumbnail_link, description, region)
VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', list(ele)+[fl[:2]])
    con2.close()
    con.commit()
con.close()
