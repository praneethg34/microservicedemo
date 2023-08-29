import config 
from confluent_kafka import Producer
import flight
import time
import datetime

producer =Producer(config.KAFKA_CONFIG)


def kafka_call_back(err,msg):
    curr_time=datetime.datetime.strftime(datetime.datetime.now(),"%Y-%m-%d %H:%M:S")
    if err:
        print(f"{curr_time}: unable to send the message to kafka")
    else:
        print(f"{curr_time}: message sent successfully to kafka")        



def send_to_kafka(ft,xy):
    payload={
        "flight": ft.flight_number,
        "start": ft.start,
        "end": ft.end,
        "xy": xy,
        "time": datetime.datetime.strftime(datetime.datetime.now(),"%Y-%m-%d %H:%M")
    }
    print(str(payload))
    producer.produce(config.KAFKA_TOPIC,str(payload).encode("UTF-8"),callback=kafka_call_back)
    producer.poll(1)

def main():
    ft=flight.Flight(config.FLIGHT_NUMBER,config.START_CITY,config.START_STATE,config.END_CITY,config.END_STATE)
    print(f" flight number {ft.flight_number}  is at {ft.start} ready to go to {ft.end}")
    ft.take_flight()
    while ft.status=="flying":
        xy=ft.get_current_xy()
        print(f"flight {ft.flight_number} status: {xy}")

        send_to_kafka(ft,xy)


        time.sleep(5)



if __name__=="__main__":
    main()        