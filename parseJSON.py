#!/usr/bin/env python

import sys
import json

tocheck = json.loads(sys.argv[1])

print tocheck["count"]
