"""Defines documentation management behaviors for the package
"""

import pydoc
import os
import importlib
import morning

def getDocDir():
	"""Returns the absolute path to the documentation directory of the pyroclast
	   package (where this file is located).
	"""
	return os.path.dirname(os.path.realpath(__file__)) + os.sep

def buildAllDocs(symbol=None):
	"""Recursively constructs HTML pages of documentation the given module
	   contents, beginning with the package itself, which are subsequently
       written to the package's 'docs/' folder.
	"""
    if symbol is None:
        symbol = morning
	dd = getDocDir()
	obj, name = pydoc.resolve(symbol)
	page = pydoc.html.page(pydoc.describe(obj), pydoc.html.document(obj,name))
	with open(dd + name + '.html', 'w') as f:
		f.write(page)
	if hasattr(obj, '__all__'):
		for a in obj.__all__:
			identifier = name + '.' + a
			child = importlib.import_module(identifier)
			buildAllDocs(child)

if __name__ == '__main__':
	buildAllDocs()
