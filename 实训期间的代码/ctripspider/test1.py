
import redis
res=redis.Redis(host='120.77.253.36',db=10)
res.set('baoqiang',17)