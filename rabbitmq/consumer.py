# -*- coding: utf-8 -*-

import time
import pika

user_info = pika.PlainCredentials('fly', 'fly@123')
connection = pika.BlockingConnection(
    pika.ConnectionParameters('127.0.0.1', 5672, '/fly.test', user_info))

channel = connection.channel()

channel.queue_declare('demo')


def callback(ch, method, properties, body):
    print('消息:{}'.format(body))


channel.basic_consume(queue='demo',
                      auto_ack=True,
                      on_message_callback=callback)

print('Waiting for messages. To exit press CTRL+C')

channel.start_consuming()