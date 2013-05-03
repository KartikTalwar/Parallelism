import os
import sys
import time
import Queue
import threading


class Parallelism(object):

  def __init__(self, **kwargs):
    self.arguments = kwargs


  def map(self, function, arguments, threads):
    return None


  def filter(self, function, arguments, threads):
    return None


  def reduce(self, function, arguments, threads):
    return None


  def worker(self):
    return None


  def process(self):
    return None