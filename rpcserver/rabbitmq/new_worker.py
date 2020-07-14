

import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.17.43.109'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print(" [*] Waiting for messages. To exit press CTRL+C")

def callback(ch, method, properties, body):
    body = str(body)
    print(" [x] Received %r" % body)
    time.sleep(body.count('.'))
    print("[x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(callback,
                      queue='task_queue')

channel.start_consuming()
