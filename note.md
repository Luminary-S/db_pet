
# 怎么在redis上更新数据 然后定时插入mysql 
1. redis是一种内存性的数据存储服务，所以它的速度要比mysql快。
2. redis只支持String,hashmap,set,sortedset等基本数据类型，但是不支持联合查询，所以它适合做缓存。
3. 有时候缓存的数据量非常大，如果这个时候服务宕机了，且开启了redis的持久化功能，重新启动服务，数据基本上不会丢。
4. redis可以做内存共享，因为它可以被多个不同的客户端连接。
5. 做为mysql等数据库的缓存，是把部分热点数据先存储到redis中，或第一次用的时候加载到redis中，下次再用的时候，直接从redis中取。
6. redis中的数据可以设置过期时间expire，如果这个数据在一定时间内没有被延长这个时间，那个一定时间之后这个数据就会从redis清除。 