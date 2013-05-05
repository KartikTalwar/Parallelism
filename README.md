# Parallelize - Parallel Processing for Python

## Methods

### Map

```python
import parallelize

def cube(x):
  return x*x*x

print parallelize.map(cube, [100, 999, 12321])
```


### Filter

### Reduce


## TODO

- Documentation
- Major refactoring
- Use multiprocessing?
- Make decorators?
