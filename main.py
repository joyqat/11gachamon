import requests
import csv
import time
import os
from datetime import datetime

# 接口URL
# 主角特权-110283
# 鸣人-110381
# 嫦娥-110154
# 神龙-110284
API_ENDPOINT = 'https://rpgact.5211game.com/show/GetAwardList/110154'
# COOKIE
COOKIES = {'PassportCookie_xxxxx': 'xxxxxxxxx'}
# 轮询间隔
WAIT_TIME = 0.5
# 输出文件路径
OUTPUTFILE_PATH = 'd:/11gamemon/output.csv'
# 输出文件编码，建议使用gb18030或者gb2312方便Excel处理
ENCODING = 'gb18030'

# 从接口获得数据，失败时会循环重试
def fetch_data():
    while True:
        try:
            response = requests.get(API_ENDPOINT, cookies=COOKIES)
            response.raise_for_status()
            data = response.json()
            if data['errCode'] == 0:
                return data['data']
            else:
                print(f"接口返回错误: {data['msg']}")
                time.sleep(WAIT_TIME)
        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")
            time.sleep(WAIT_TIME)

def setdiff(prev, curr):
    if all_equal(prev, curr):
        return []

    # API返回的数据类似一个宽20的滑动窗
    # 在假定轮询速率足够的情况下
    # 比较当前数据的尾部与旧数据的头部来剔除重复的数据
    # 当一个轮询期间有超出20条数据的更新，则会漏掉数据
    for i in range(len(curr)):
        if is_equal(prev[0], curr[i]):
            if all_equal(prev[0:len(prev)-i], curr[i:]):
                return curr[0:i]

    print("数据无公共部分，可能发生数据遗漏")
    return curr

def all_equal(l1, l2):
    return len(l1) == len(l2) and all([l1[x] == l2[x] for x in range(len(l1))])

def is_equal(obj1, obj2):
    return obj1['user_id'] == obj2['user_id'] and obj1['show_name'] == obj2['show_name']

def write_to_csv(data):
    with open(OUTPUTFILE_PATH, mode='a', newline='', encoding=ENCODING) as file:
        writer = csv.writer(file)
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for item in data:
            writer.writerow([current_time, item['user_id'], item['user_name'], item['show_name'], item['rarity']])
    print(f"{current_time}: 添加了{len(data):2}条数据")

def main():
    # TODO: 首次写入时，判断此次数据是否与csv最后的数据有重叠
    previous_data = fetch_data()
    write_to_csv(previous_data)

    while True:
        time.sleep(WAIT_TIME)
        current_data = fetch_data()
        if current_data:
            diff = setdiff(previous_data, current_data)
            if diff:
                write_to_csv(diff)
            previous_data = current_data


if __name__ == "__main__":
    # 初始化 CSV 文件，写入标题行
    # 文件存在时写入分隔符
    if not os.path.exists(OUTPUTFILE_PATH):
        with open(OUTPUTFILE_PATH, mode='w', newline='', encoding=ENCODING) as file:
            writer = csv.writer(file)
            writer.writerow(['timestamp', 'user_id', 'user_name', 'show_name', 'rarity'])
    else:
        with open(OUTPUTFILE_PATH, mode='a', newline='', encoding=ENCODING) as file:
            writer = csv.writer(file)
            writer.writerow(['-', '-', '-', '-', '-'])

    main()
