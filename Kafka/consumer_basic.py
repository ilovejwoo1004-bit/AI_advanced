#===========================================================
'''
producer가 kafka topic으로 데이터를 보내고,
consumer 가 같은 topic에서 데이터를 받는 것을 확인
'''
#===========================================================

# kafka로 데이터를 받는 comsumer 객체를 만들기 위한 클래스
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "press-force",                                # 구독할 topic 이름 정의
    bootstrap_servers=["localhost:9092"],               # broker 주소 지정
    auto_offset_reset="latest",                         # consumer 가 처음 실행 될 때 최신 데이터로부터 읽도록 설정
    group_id="basic-consumer-group",                    # consumer 그룹 id 지정
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

print("Consumer_basic 시작: press-force topic 데이터를 수신합니다.")

for message in consumer:
    data = message.value
    print("수신:", data)