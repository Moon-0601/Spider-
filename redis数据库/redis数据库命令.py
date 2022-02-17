import redis
def main():
    # #连接redis（1）
    # r=redis.StrictRedis(host='localhost',port=6379,db=0)
    # 连接redis（2）使用连接池去连接
    pool=redis.ConnectionPool(host='localhost',port=6379,decode_responses=True)
    r=redis.StrictRedis(connection_pool=pool)
    """======================================================="""
    ####基本功能
    r.set("key1","value111")
    ##有过期时间
    r.set("key2","value222",px=10000)
    #print(r.get("key1").decode("utf-8"))
    r.setex("key3",10,"val3")
    ##多值存储
    r.mset({"haha1": "111", "haha2": "222","ada333":"3333"})
    print(r.mget("haha1","haha2"))  #list-['111', '222']
    """======================================================="""

    ####hash功能
    r.hset("hash1","k1","value1")
    r.hset("hash1","k2","value22222")
    print(r.hkeys("hash1"))     #list-['k1', 'k2']
    print(r.hget("hash1","k1"))    #str-value1
    print(r.hmget("hash1","k1","k2"))   #list-['value1', 'value22222']
    r.hmset("hash2",{"n1":"nnnn1111","n2":"nnnn2222","n3":99})
    print(r.hgetall("hash2"))   #dic-{'n1': 'nnnn1111', 'n2': 'nnnn2222'}
    #判断是否存在某元素
    print(r.hexists("hash1","xxx"))
    print(r.hexists("hash1","k1"))
    #自增减(包含浮点数加减)
    r.hincrby("hash2","n3",amount=+100)
    """======================================================="""

    ####list功能
    r.rpush("list1",1,2,3,4,5,6,7,8,9)
    print(r.llen("list1"))
    print(r.lrange("list1",0,3))
    #在值3的前面加一个99
    r.linsert("list1","before",3,99)
    #将第五个值改为-300
    r.lset("list1",4,-300)
    #删除列表最左边的元素
    r.lpop("list1")
    #删除索引号0-2以外的所有元素
    r.ltrim("list1",0,2)
    #取出索引为1的值
    print(r.lindex("list1",1))
    """======================================================="""

    ####set命令(无序，值不可修改)
    r.sadd("set1",11,22,33,44,55)
    print(r.scard("set1"))#5
    print(r.smembers("set1"))#{'11', '44', '33', '22', '55'}
    #使用迭代获取元素
    for i in r.sscan_iter("set1"):
        print(i)
    #随机删除一个元素
    r.spop("set1")
    #指定删除某个元素
    r.srem("set1",33)
    """======================================================="""

    ####zset命令(权重，只添加)
    r.zadd("zset1", mapping={'m1': 2, 'm2': 9, 'm3': 7, 'm4': 1})
    #几个元素
    print(r.zcard("zset1"))
    #获取所有元素（正向）
    print(r.zrange("zset1",0,-1))
    #反向排序
    print(r.zrevrange("zset1",0,-1))
    #修改权重（排序）
    r.zincrby("zset1",value='m3',amount=2)
    #删除
    r.zrem("zset1","m2")
    #查看权重
    print(r.zscore("zset1","m3"))
    """======================================================="""
    ####通用命令
    #任意数据类型删除
    r.delete("haha2")
    #判断是否存在
    print(r.exists("zset1"))
    #重命名
    r.rename("set1","set100")
    #获得数据类型
    print(r.type('zset1'))
    pass
if __name__ == '__main__':
    main()
