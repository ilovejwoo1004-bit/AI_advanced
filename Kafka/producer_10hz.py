# =========================================================
'''
producer : 0.1초마다 데이터 전송
consumer : 초당 약 10건씩 수진 tps 출력
'''
# =========================================================

from kafka import KafkaProducer  # kafka로 데이터를 보내는 producer 객체를 만들기 위한 클래스
import json
import random
import time
from datetime import datetime

# kafka 객체 생성
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# 데이터를 전송할 topic 지정
topic = "press-force"
seq = 0   # 메시지 순번을 저장하기 위한 변수

print("producer 시작: 0.1초마다 1건, 초당 약 10건을 전송합니다.")

# 데이터 강제 종료까지 무한 전송
while True:
    seq += 1  # 메시지 순번을 1 증가시킴
    force = random.uniform(130, 150)

    # 5% 확률로 이상 force 데이터를 발생시킴
    if random.random() < 0.05:
        force = random.uniform(175, 210)

    # 메시지 구성
    message ={
        "seq": seq,  # 메세지 순번
        # 현재 시간을 밀리초 단위까지 문자열로 저장
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3],
        "machine_id": "press_01",    # 설비 id
        "force": round(force, 2),    # force 값을 소수점 둘 째 자리까지 반올림
    }

    # kafka topic으로 메시지 전송
    producer.send(topic, value=message)
    producer.flush()

    print(f"전송 seq={message['seq']}, force={message['force']}")

    # 0.1초마다 데이터 전송 (1초에 약 10건 데이터 전송)
    time.sleep(0.1)




