
In Python, importing modules allows you to access and use code that resides in external Python files or libraries.

```run-python
#Importing - Importing is important
import sys
print(sys.version)

from datetime import datetime #importing a class from a module
now1 = datetime.now()
print(now1)

import datetime
now2 = datetime.datetime.now()
print(now2)
```


## Importing Entire Modules:

```run-python
import math

result = math.sqrt(25)
print(result)   # Output: 5.0
```

```run-python
import sys

print(sys.version)
```


```run-python
import datetime
now = datetime.datetime.now()
print(now)
```

## Importing Specific Functions or Variables:

If you only need to use specific functions or variables from a module, you can import them directly.

```run-python
from math import sqrt

result = sqrt(25)
print(result)   # Output: 5.0
```

```run-python
from datetime import datetime #importing a class from a module
now = datetime.now()
print(now)
```
## Importing Modules with an Alias

You can also import a module and give it an alias using the `as` keyword. This can be helpful when dealing with modules with long names or to avoid naming conflicts.

```run-python
import math as m

result = m.sqrt(25)
print(result)   # Output: 5.0
```

In this example, the `math` module is imported and assigned the alias `m`, so you can use `m.sqrt()` instead of `math.sqrt()`.


```run-python
from datetime import datetime as dt #give an alias

print(dt.now()) # more readability and namespace management
```



## Importing All Functions and Variables

If you want to import all functions and variables from a module, you can use the `*` wildcard character. However, it is generally recommended to import only what you need to avoid namespace pollution.

```
from math import *

result = sqrt(25)
print(result)   # Output: 5.0
```

In this case, all functions and variables from the `math` module are imported directly, allowing you to use them without prefixing with the module name.

