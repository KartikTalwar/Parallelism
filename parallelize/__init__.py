import os
import sys
import time
import Queue
import threading


class Parallelize(object):

  def __init__(self, output, concurrent=1):
    self.concurrent = concurrent
    self.queue   = Queue.Queue()
    self.threads = []
    self.output  = output


  def spawn(self):
    t = threading.Thread(target=self.compute, args=[self])
    t.setDaemon(True)
    t.start()
    self.threads.append(t)


  def compute(self, *args):
    while True:
      task = self.queue.get()
      function, arguments = task
      print function(arguments)
      #self.output.append(function(arguments))


  def add(self, function, arguments):
    self.queue.put((function, arguments))


  def start(self):
    self.spawn()

    while len(self.threads) is not 0:
      temp = []

      for task in self.threads:
        if task.is_alive():
          temp.append(task.join(1) or task)

      print self.threads

      self.threads = temp
      if not self.queue.empty():
        self.spawn()



def map(function, arguments, threads=10):
  queue = Queue.Queue()
  data  = []

  worker = Parallelize(10, data)

  for i in arguments:
    worker.add(function, i)

  worker.start()

  return data


def filter(function, arguments, threads=10):
  return None


def reduce(function, arguments, threads=10):
  return None



