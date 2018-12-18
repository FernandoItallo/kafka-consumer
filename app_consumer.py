from kafka import KafkaConsumer

# To consume latest messages and auto-commit offsets

while True:
    consumer = KafkaConsumer('first_topic', auto_offset_reset='latest',
                             group_id='my-group_03',
                             bootstrap_servers=['127.0.0.1:9092'])
    for message in consumer:
        # message value and key are raw bytes -- decode if necessary!
        # e.g., for unicode: `message.value.decode('utf-8')`
        print(message.value)
