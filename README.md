# Parallelism - Parallel Processing for Python

## Methods

### Map

```python
import parallelism

def cube(x):
  return x*x*x

print parallelism.map(cube, [100, 999, 12321])
```


### Filter

### Reduce


## TODO

- Documentation
- Major refactoring
- Use multiprocessing?
- Make decorators?
