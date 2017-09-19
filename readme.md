To use:

    python rc8.py
    
In your own programs, create a file with content similar to this:

```python
from rc8 import readConfig, raspRobot
import time

config = readConfig('config.yaml')

r = raspRobot( config )

r.setSpeed( 50 )
time.sleep( 2 )

r.setDirection( 20 )
time.sleep( 2 )

```

    
Errors

1. `ImportError: No module named yaml`

    install the yaml module: `apt-get install python-yaml`
    
