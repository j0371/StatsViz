import calculation
import rw
import numpy as np
import collections, re

d = {"key1" : 'object', "key11" : 'object', "key2" : 'object', "key22" : 'object', "jay1" : 'object', "jay2" : 'object'}


my_fun = lambda k,v: [k, int(v)]

string = "key11"

print(re.match(r'([a-zA-Z]+)(\d+)', string))

d2 = collections.OrderedDict(sorted(d.items(), key=lambda t: my_fun(*re.match(r'([a-zA-Z]+)(\d+)',t[0]).groups())))

print(d2)