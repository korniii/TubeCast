import threading
from queue import Queue
import pafy
import time

lock = threading.Lock()

def printAudioDetail(item):
    p = item
    best = p.getbestaudio()
    print(p.title)
    print(threading.current_thread().name, best.url)

def worker():
    while True:
        time.sleep(1)
        item = q.get()
        printAudioDetail(item)
        q.task_done()


playlist = pafy.get_playlist("PLpaD0ybYH0S3XOMnC8ADVycFyEcjRJ6Aj")
videos = playlist['items']

for i in range(100):
  t = threading.Thread(target=worker)
  t.daemon = True
  t.start()

#fill Queue
q = Queue()
for video in videos:
    q.put(video['pafy'])

q.join()

time.sleep(5)


