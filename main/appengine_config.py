from google.appengine.ext import vendor
import os
import sys

ENDPOINTS_PROJECT_DIR = os.path.join(os.path.dirname(__file__),
                                     'endpoints-proto-datastore')
sys.path.append(ENDPOINTS_PROJECT_DIR)

# Add any libraries installed in the `lib` folder.
vendor.add('lib')
