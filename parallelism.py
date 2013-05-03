import os
import sys
import time
import Queue
import threading


class Parallelism(threading.Thread):

  def __init__(self, queue, function, output):
    threading.Thread.__init__(self)
    self.queue    = queue
    self.function = function
    self.output   = output


  def run(self):
    while True:
      task = self.queue.get()
      self.output.append(self.function(task))
      self.queue.task_done()




def map(function, arguments, threads=10):
  queue = Queue.Queue()
  data  = []

  for i in range(threads):
    task = Parallelism(queue, function, data)
    task.setDaemon(True)
    task.start()

  for j in arguments:
    queue.put(j)

  queue.join()

  return data


def filter(function, arguments, threads=10):
  return None


def reduce(function, arguments, threads=10):
  return None



