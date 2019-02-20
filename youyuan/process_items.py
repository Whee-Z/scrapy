import json
import redis
import MySQLdb

def main():
    # 指定redis数据库信息
    rediscli = redis.StrictRedis(host='192.168.50.159', port = 6379, db = 0)
    # 指定mysql数据库
    mysqlcli = MySQLdb.connect(host='127.0.0.1', user='root', passwd='你的密码咯', db = 'youyuan', port=3306, use_unicode=True)

    while True:
        # FIFO模式为 blpop，LIFO模式为 brpop，获取键值
        source, data = rediscli.blpop(["youyuan:items"])
        item = json.loads(data)

        try:
            # 使用cursor()方法获取操作游标
            cur = mysqlcli.cursor()
            # 使用execute方法执行SQL INSERT语句
            cur.execute("INSERT INTO shenzhen_18_25 (username,age,header_url,images_url,content,place_from,education,hobby,source_url,source) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s )", [item['username'],item['age'], item['header_url'], item['images_url'], item['content'], item['place_from'], item['education'], item['hobby'], item['source_url'], item['source']])
            # 提交sql事务
            mysqlcli.commit()
            #关闭本次操作
            cur.close()
            print("inserted %s" % item['source_url'])
        except MySQLdb.Error as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

if __name__ == '__main__':
    main()
