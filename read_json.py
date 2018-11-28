import json
import pprint

with open('json_test.json') as slownik:
    katalogi_zakladki = json.load(slownik)

print json.dumps(katalogi_zakladki, indent=4, sort_keys=True)

##pprint.pprint(katalogi_zakladki)

##def walk_dict(katalogi_zakladki, depth=0):
##    for k,v in sorted(katalogi_zakladki.items(), key = lambda x: x[0]):
##        if isinstance(v, dict):
##            print(" ")*depth+("%s " % k)
##            walk_dict(v,depth+1)
##        else:
##            print (" ")*depth + "%s %s" % (k, v)
##
##walk_dict(katalogi_zakladki)
