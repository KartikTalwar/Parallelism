import time
import Queue
import threading


class Worker(threading.Thread):

  def __init__(self, queue):
    threading.Thread.__init__(self)
    self.queue = queue


  def run(self):
    while True:
      task = self.queue.get()
      print task
      self.queue.task_done()


queue = Queue.Queue()
for i in range(5):
  t = Worker(queue)
  t.setDaemon(True)
  t.start()

for j in range(5):
  queue.put(j)

queue.join()


