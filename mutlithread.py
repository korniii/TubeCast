import threading
import timeit
from queue import Queue
import pafy
import time

start = timeit.timeit()

def worker():
    while True:
        p = video['pafy']
        best = p.getbestaudio()
        print(p.title)
        print(threading.current_thread().name, best.url)

playlist = pafy.get_playlist("PLpaD0ybYH0S3XOMnC8ADVycFyEcjRJ6Aj")
videos = playlist['items']

#fill Queue
q = Queue()


for video in videos:
  t = threading.Thread(target=worker)
  t.daemon = True
  t.start()

time.sleep(10)

end = timeit.timeit()
print (end - start)

