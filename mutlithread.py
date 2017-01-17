import random
import string
import threading
from queue import Queue
import pafy
import time
import os

counter = 0
directory = "C:/Users/morit_000/Desktop/TubeCast"

# lock to serialize console output
lock = threading.Lock()

#prints all Title and AudioLink of Profile
def printAudioDetail(item):
    p = item
    try:
        best = p.getbestaudio(preftype="m4a")
        title = best.title[20:].replace(":", "_")

        filepath = directory + "/"+title+"." + best.extension
        #print("Check: "+filepath)
        best.download(filepath)
        print(filepath)
    except Exception as err:
        print(err)
        print(filepath)
        #print(p.title +" "+ err)
        q.put(p)
    #print(p.title)
    #print(threading.current_thread().name, best.url)
    filepath = directory + best.title + "." + best.extension


#worker method, thread method
def worker():
    time.sleep(1)
    while True:
        item = q.get()
        printAudioDetail(item)
        #print(item.title)

        q.task_done()


playlist = pafy.get_playlist("PLpaD0ybYH0S3XOMnC8ADVycFyEcjRJ6Aj")
videos = playlist['items']

#Threadpool initialization, number of Threads
for i in range(10):
  t = threading.Thread(target=worker)
  t.daemon = True
  t.start()

#fill Queue, gets processed by the Threads
q = Queue()
for video in videos:
    q.put(video['pafy'])
    counter += 1
q.join()

#if method stops before threads --> Exception
#time.sleep(5)

print("Ergebnis "+counter.__str__())

