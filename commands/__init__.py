import pkgutil
from importlib import import_module
from pathlib import Path

import sys

for (_, name, _) in pkgutil.iter_modules([Path(__file__).parent]):

    imported_module = import_module('.' + name, package=__name__)

    for i in dir(imported_module):
        attribute = getattr(imported_module, i)
        setattr(sys.modules[__name__], name, attribute)
