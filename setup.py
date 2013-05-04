from setuptools import setup

setup(
    name = "parallelize",
    version = "0.1",
    author = "Kartik Talwar",
    author_email = "hi@kartikt.com",
    description = ("Utilities for running functions in parallel"),
    keywords = "parallel, multiprocessing, map, reduce, threading",
    license = 'Apache',
    url = "http://github.com/KartikTalwar/parallelize",
    packages = ['parallelize'],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Operating System :: Unix',        
        "Programming Language :: Python",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    long_description = """
# Parallelism - Parallel Processing for Python

## Methods

### Map

```python
import parallelize

def cube(x):
  return x*x*x

print parallelize.map(cube, [100, 999, 12321])
```
"""
)
