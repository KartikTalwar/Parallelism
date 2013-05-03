import time
import Queue
import threading


class Worker(threading.Thread):

  def __init__(self, queue, function):
    threading.Thread.__init__(self)
    self.queue = queue
    self.function = function


  def run(self):
    while True:
      task = self.queue.get()
      print self.function(task)
      self.queue.task_done()


def map(function, args, threads):
  queue = Queue.Queue()
  data = []

  for i in range(threads):
    t = Worker(queue, function)
    t.setDaemon(True)
    t.start()

  for j in args:
    queue.put(j)

  queue.join()


def cube(x):
  return x*x*x

print map(cube, [3, 6, 8], 5)


