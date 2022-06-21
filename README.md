链工宝答题自动化

# 自动化的链工宝答题

题库不全，比较看脸

## 方法1

1. git clone https://github.com/nfjBill/liangongbao.git
2. users.yaml配置好账号，密码，可批量。(userAgent可选，可设置userAgent为本机设备)
3. pip install -r requirements.txt
4. python main.py

## 方法2：docker

- `every_day`为每日触发脚本时间
- `users.yaml`为用户配置文件，可提前配置，参考项目中`users.yaml`

```shell

docker run \
    --name lgb -d \
    --restart=always \
    -e every_day="06:00" \
    -v /绝对路径/users.yaml:/users.yaml \
    nfjbill/liangongbao:1.2
```

## 方法3：docker-compose

```yaml
version: '3.1'
services:
  lgb:
    image: nfjbill/liangongbao:1.2
    container_name: lgb
    restart: always
    environment:
      - every_day="06:00"
    volumes:
      - ./users.yaml:/users.yaml
```
