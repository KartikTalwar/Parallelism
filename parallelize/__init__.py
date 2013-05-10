import os
import sys
import time
import Queue
import threading


class Parallelize(object):

  def __init__(self, output, threads, ftype='map'):
    self.queue   = Queue.Queue()
    self.threads = []
    self.ftype   = ftype
    self.output  = output
    self.alive   = True


  def spawn(self):
    t = threading.Thread(target=self.compute, args=[self])
    t.setDaemon(True)
    t.start()
    self.threads.append(t)


  def compute(self, *args):
    while not self.queue.empty() and self.alive:
      task = self.queue.get()
      function, arguments = task
      evaluate = function(arguments)

      if self.ftype == 'filter':
        if evaluate:
          self.output.append(evaluate)
      else:
        self.output.append(evaluate)


      self.queue.task_done()


  def add(self, function, arguments):
    self.queue.put((function, arguments))


  def start(self):
    self.spawn()

    try:
      while len(self.threads):
        temp = []

        for task in self.threads:
          if task.is_alive():
            temp.append(task.join(1) or task)

        self.threads = temp
        if not self.queue.empty():
          self.spawn()
    except KeyboardInterrupt:
      self.alive = False



def map(function, arguments, threads=10):
  output = []
  worker = Parallelize(output, threads)

  for i in arguments:
    worker.add(function, i)

  worker.start()

  return output


def filter(function, arguments, threads=10):
  output = []
  worker = Parallelize(output, threads, ftype='filter')

  for i in arguments:
    worker.add(function, i)

  worker.start()

  return output


def reduce(function, arguments, threads=10):
  return None



