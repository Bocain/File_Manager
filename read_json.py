import json
import gtk



class OpenJason(gtk.Window):
    def __init__(self):
        super(OpenJason, self).__init__()
            
        self.connect("destroy", lambda w: gtk.main_quit())
        self.set_default_size(300, 300)
        self.set_position(gtk.WIN_POS_CENTER)
        
        with open('Database.json') as slownik:
            data = json.load(slownik)
        text = json.dumps(data, indent=4, sort_keys=True)

        label = gtk.Label()
        label.set_text(text)
        frame = gtk.Frame("Zawartosc katalogow")
        frame.add(label)

        self.add(frame)
        self.show_all()
        gtk.main()        
        return

OpenJason()

##=========Inne sposoby na otwarcie json=========##

##with open('json_test.json') as slownik:
##    katalogi_zakladki = json.load(slownik)
##
##print json.dumps(katalogi_zakladki, indent=4, sort_keys=True)

##import pprint
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
