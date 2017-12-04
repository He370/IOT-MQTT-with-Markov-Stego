import context  # Ensures paho is in PYTHONPATH
import paho.mqtt.publish as publish
import time
import datetime

from random import *

# markov chain
import argparse
import markov
import utils
import variableSizeCode

while True:
    time.sleep(1)
    x = randint(1, 100)
    x = "Data:" + str(x) + ",Time:" + str(datetime.datetime.now().time())
    print("origin data:"+str(x))
    data = variableSizeCode.encodeDataFromData(str(x),"data/markovChain.json", True, 1)
    print("data sent:"+str(data))
    #publish.single("CNIT561/temp", str(data), hostname="broker.hivemq.com")
    publish.single("CNIT561/temp", str(data), hostname="iot.eclipse.org")
