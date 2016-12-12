import threading
from queue import Queue
import pafy
import time

# lock to serialize console output
lock = threading.Lock()

#prints all Title and AudioLink of Profile
def printAudioDetail(item):
    p = item
    best = p.getbestaudio()
    print(p.title)
    print(threading.current_thread().name, best.url)

#worker method, thread method
def worker():
    time.sleep(1)
    while True:
        item = q.get()
        printAudioDetail(item)
        q.task_done()


playlist = pafy.get_playlist("PLpaD0ybYH0S3XOMnC8ADVycFyEcjRJ6Aj")
videos = playlist['items']

#Threadpool initialization, number of Threads
for i in range(100):
  t = threading.Thread(target=worker)
  t.daemon = True
  t.start()

#fill Queue, gets processed by the Threads
q = Queue()
for video in videos:
    q.put(video['pafy'])

q.join()

#if method stops before threads --> Exception
time.sleep(10)


