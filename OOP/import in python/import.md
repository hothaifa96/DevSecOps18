# Python `import` and `from ... import` Commands

## Introduction
Python provides a powerful module system that allows code reuse across different files and projects. The `import` and `from ... import` statements enable developers to use functions, classes, and variables from other modules or packages.

---

## 1. `import` Statement
The `import` statement allows you to include an entire module in your script.

### Syntax:
```python
import module_name
```

### Example:
```python
import math
print(math.sqrt(16))  # Output: 4.0
```

### Accessing Module Members
To access functions or variables from an imported module, use the dot notation:
```python
module_name.function_name()
```

### Importing Multiple Modules
```python
import math, random
print(math.pi)
print(random.randint(1, 10))
```

---

## 2. `from ... import` Statement
The `from ... import` statement allows you to import specific functions, classes, or variables from a module.

### Syntax:
```python
from module_name import function_name
```

### Example:
```python
from math import sqrt
print(sqrt(16))  # Output: 4.0
```

### Importing Multiple Items
```python
from math import sqrt, pi
print(sqrt(25))
print(pi)
```

### Importing All Items (`*`)
```python
from math import *
print(sqrt(36))
print(pi)
```
*Note:* Using `import *` is generally discouraged as it can lead to name conflicts.

---

## 3. Using Aliases with `import` and `from ... import`
You can rename modules or functions using `as` for convenience.

### Module Alias:
```python
import numpy as np
print(np.array([1, 2, 3]))
```

### Function Alias:
```python
from math import sqrt as square_root
print(square_root(49))  # Output: 7.0
```

---

## 4. Importing Custom Modules
You can create and import your own modules.

### Example:
**`my_module.py`**
```python
def greet(name):
    return f"Hello, {name}!"
```

**Main Script:**
```python
import my_module
print(my_module.greet("Alice"))
```

---

## 5. Importing from Packages
A package is a directory containing multiple modules along with an `__init__.py` file (optional in Python 3.3+).

### Example:
```
my_package/
    __init__.py
    module1.py
    module2.py
```

Importing a module from a package:
```python
from my_package import module1
```

---

## 6. Relative Imports
Relative imports are used within packages to import modules relative to the current script’s location.

### Example:
```python
from . import module_name  # Import from the same package
from .. import another_module  # Import from the parent package
```

*Note:* Relative imports only work in package structures, not in standalone scripts.

---

## 7. Lazy Imports (Dynamic Imports)
Modules can be imported dynamically at runtime using `importlib`.

### Example:
```python
import importlib
math_module = importlib.import_module("math")
print(math_module.sqrt(64))  # Output: 8.0
```

---

## Summary Table

| Statement | Usage Example |
|-----------|--------------|
| `import module_name` | `import math` |
| `import module1, module2` | `import os, sys` |
| `from module import name` | `from math import sqrt` |
| `from module import *` | `from math import *` |
| `import module as alias` | `import numpy as np` |
| `from module import name as alias` | `from math import sqrt as square_root` |

---

## Conclusion
Understanding the `import` and `from ... import` statements is crucial for writing modular, reusable Python code. By structuring code into modules and packages, developers can improve maintainability and reduce redundancy.

---


