"""
my_project/
├── ioihelper/
│   └── data/

│   ├── __init__.py
│   └── ioihelper_core.py
│   └── ioihelper_cli.py
├── devharness.py

✅ 1. Your script isn't run from the project root
When you run devharness.py, Python uses the current working directory as the base for imports.

If you're running the script like this:

    python devharness.py

from inside the my_project/ folder, it should work.

But if you run it from outside, like:

    python my_project/devharness.py

then Python doesn’t treat my_project/ as the root, and ioihelper won't be found properly.

✅ 2. Fix by adding project root to PYTHONPATH
To make this work reliably from anywhere, update devharness.py like this:
import sys
import os

# Add the parent directory to the path so the package can be found
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

✅ 3. PyCharm tip: set working directory correctly
In PyCharm:

Go to Run > Edit Configurations...

In your run configuration for devharness.py, set Working directory to the project root (my_project/)

This ensures imports work as expected during runs and debugging.
"""

# Add the parent directory to the path so the package can be found

import ioihelper

ioihelper.ioihelper_cli.main()
