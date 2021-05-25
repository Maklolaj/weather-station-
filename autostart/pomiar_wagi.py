import paho.mqtt.client as mqtt
import pandas as pd
from datetime import datetime
import time

MQTT_ADDRESS = '192.168.137.204'
MQTT_USER = 'rasberry'
MQTT_PASSWORD = 'rasberry'   
MQTT_TOPIC = 'barak/+/+'



def on_connect(client, userdata, flags, rc):    
    """ The callback for when the client receives a CONNACK response from the server."""
    print('Connected with result code ' + str(rc))
    
    if rc == 0:
        client.connected_flag=True
        print("All OK")
    else:
        print("Bad connection with result code =", rc)
    
    
    client.subscribe(MQTT_TOPIC)
    
def normalize(string):
    string = string.replace("'","")
    string = string.replace("b","")
    return string



def on_message(client, userdata, msg):
    """The callback for when a PUBLISH message is received from the server."""
    
    print(msg.topic + ' ' + str(msg.payload))
    
    
    waga = normalize(str(msg.payload))
    
    
    df = pd.read_excel("/home/pi/Programiki/autostart/waga.xlsx",engine='openpyxl')  # zapisz excela do dataframe
    
    now=datetime.now()
    current_time=now.strftime("%H:%M:%S")
    
    new_row = {'Waga': waga, 'Czas':current_time} # stworz nowy record
    
    df = df.append(new_row, ignore_index=True) # dodaj record do dataframe object
    
    
    df.to_excel("/home/pi/Programiki/autostart/waga.xlsx",index=False) # zapisz dataframe do excela


def main():
    mqtt.Client.connected_flag=False
    mqtt_client = mqtt.Client()
    mqtt_client.username_pw_set(MQTT_USER, MQTT_PASSWORD)
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    
    print("Connecting to the broker")
    
    while not mqtt_client.connected_flag:
        try:
            
            mqtt_client.connect(MQTT_ADDRESS, 1883)
            mqtt_client.connected_flag=True
        except:
            time.sleep(5)
            print("Czekam")
            
    
    mqtt_client.loop_forever()


if __name__ == '__main__':
    print('MQTT to InfluxDB bridge')
    main()



