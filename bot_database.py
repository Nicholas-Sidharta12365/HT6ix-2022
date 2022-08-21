import sqlite3
import datetime
import math
from numpy_preprocess import convert_array

def create_db(user_id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute(f'''CREATE TABLE IF NOT EXISTS user{user_id} (message TEXT, time_since BIGINT, classification TEXT)''')
    conn.commit()
    c.execute(f'''CREATE TABLE IF NOT EXISTS user{user_id}_reminder (mood TEXT, time_since BIGINT)''')
    conn.commit()
    conn.close()

def log_reminder(user_id, mood, time_since):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute(f'''INSERT INTO user{user_id}_reminder (mood, time_since) VALUES (?, ?)''', (mood, time_since))
    conn.commit()
    conn.close()

def log_message(user_id, message, time_since, classification):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute(f'''INSERT INTO user{user_id} (message, time_since, classification) VALUES (?, ?, ?)''', (message, time_since, classification))
    conn.commit()
    conn.close()

def get_reminder(user_id, mood_now):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    time_limit = datetime.datetime.now() - datetime.datetime(2022, 8, 19, 0, 0, 0) - datetime.timedelta(minutes=15)
    c.execute(f'''SELECT * FROM user{user_id}_reminder WHERE time_since > ? AND mood=?''', (math.floor(time_limit.total_seconds()), mood_now))
    reminder = c.fetchall()
    conn.close()
    return reminder

def get_time_limit(time, x):
    time_limit = datetime.timedelta(seconds=time) + datetime.timedelta(hours=x) - (datetime.datetime.now() - datetime.datetime(2022, 8, 19, 0, 0, 0))
    return math.floor(time_limit.total_seconds())

def get_all_messages_past_x_hours(user_id, x):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    time_limit = datetime.datetime.now() - datetime.datetime(2022, 8, 19, 0, 0, 0) - datetime.timedelta(hours=x)
    c.execute(f'''SELECT message, time_since, classification FROM user{user_id} WHERE time_since > {math.floor(time_limit.total_seconds())}''')
    messages = c.fetchall()
    conn.close()
    messages = [(message[0], get_time_limit(message[1], x), convert_array(message[2])) for message in messages]
    # print(messages)
    return messages

# create_db('1')