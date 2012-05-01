#!/usr/bin/env python
import os

virtdir= os.environ['OPENSHIFT_DATA_DIR']
os.environ['PYTHON_EGG_CACHE'] = os.path.join(virtdir, 'virtenv/lib/python2.6/site-packages')
virtualenv = os.path.join(virtdir, 'virtenv/bin/activate_this.py')
execfile(virtualenv, dict(__file__=virtualenv))

import main

if __name__ == "__main__":
    port = os.environ['OPENSHIFT_INTERNAL_PORT']
    address = os.environ['OPENSHIFT_INTERNAL_IP']
    main.run(port,address)

