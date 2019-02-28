from db.db_helper import SQLHelper
import requests
import json
import time

last_id = 0


def main():
    global last_id
    url = 'http://gongfudou.com/insight/map/designs?count=5&last={}'.format(last_id)
    ret = requests.get(url)
    if ret.status_code == 200:
        try:
            data = json.loads(ret.text, encoding='utf8')
            print(len(data))
            for item in data:
                origin_id = item.get('id')
                lat = item.get('map_x')
                lng = item.get('map_y')
                nickname = item.get('nickname')
                city = item.get('region_name')
                avatar = item.get('headimgurl')
                SQLHelper.execute(
                    'INSERT INTO users(nickname,city,avatar,lat,lng,origin_id) VALUES (%s,%s,%s,%s,%s,%s)',
                    (nickname, city, avatar, lat, lng, origin_id))
                last_id = origin_id
        except Exception as e:
            pass


if __name__ == '__main__':
    while True:
        main()
        time.sleep(1)
