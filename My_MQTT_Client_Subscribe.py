import context  # Ensures paho is in PYTHONPATH
import paho.mqtt.subscribe as subscribe

# markov chain
import argparse
import markov
import utils
import variableSizeCode

topics = ['CNIT561/temp']

while True:
    m = subscribe.simple(topics, hostname="iot.eclipse.org", retained=False, msg_count=1)
    print(m.topic)
    print("data received:"+m.payload)
    data = variableSizeCode.decodeDataFromData(m.payload,"data/markovChain.json",1)
    print("origin data:"+str(data))
