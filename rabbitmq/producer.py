# -*- coding: utf-8 -*-
import time
import pika

user_info = pika.PlainCredentials('fly', 'fly@123')
connection = pika.BlockingConnection(
    pika.ConnectionParameters('127.0.0.1', 5672, '/fly.test', user_info))

channel = connection.channel()

channel.queue_declare('demo')

for i in range(0, 10):
    msg = '{}'.format(i)
    channel.basic_publish(exchange='demo',
                          routing_key='demo',
                          body='{}'.format(i))
    print('发送:{}'.format(msg))
    time.sleep(1)

print('发送完毕!!!')
connection.close()
