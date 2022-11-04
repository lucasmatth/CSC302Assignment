import sqlite3

diff_files = ["RUvideos", "CAvideos", "DEvideos", "USvideos",
              "INvideos", "GBvideos", "FRvideos", "MXvideos",
              "KRvideos", "JPvideos"]

for fl in diff_files:
    with open(fl+".csv", encoding="ISO-8859-1") as file:
        contents = csv.reader(file)
        connection = sqlite3.connect(fl+".db")
        cursor = connection.cursor()
        create_table = '''CREATE TABLE IF NOT EXISTS {}(
id INTEGER PRIMARY KEY AUTOINCREMENT,
video_id VARCHAR(20) NOT NULL,
trending_date VARCHAR(10) NOT NULL,
title VARCHAR(102) NOT NULL,
channel_title VARCHAR(52) NOT NULL,
category_id INTEGER NOT NULL,
publish_time DATETIME NOT NULL,
tags BLOB NOT NULL,
views INTEGER NOT NULL,
likes INTEGER NOT NULL,
dislikes INTEGER NOT NULL,
comment_counter INTEGER NOT NULL,
thumbnail_link TEXT NOT NULL,
comments_disabled BOOL NOT NULL,
ratings_disabled BOOL NOT NULL,
video_error_or_removed BOOL NOT NULL,
description BLOB NOT NULL);
'''.format(fl)
        cursor.execute(create_table)
        for ele in contents:
            insert = '''INSERT INTO {}
(video_id,
trending_date,
title,
channel_title,
category_id,
publish_time,
tags,
views,
likes,
dislikes,
comment_counter,
thumbnail_link,
comments_disabled,
ratings_disabled,
video_error_or_removed,
description)
VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
'''.format(fl)
            cursor.execute(insert, ele)
            
        connection.commit()
connection.close()
