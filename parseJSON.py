#!/usr/bin/env python3

import sys
import json

tocheck = json.loads(sys.argv[1])

print( tocheck["count"] )
