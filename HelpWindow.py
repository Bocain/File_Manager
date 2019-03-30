import gtk

class HelpWindow(gtk.Window):
    def __init__(self):
        super(HelpWindow, self).__init__()
            
        self.connect("destroy", lambda w: gtk.main_quit())
        self.set_default_size(50, 50)
        self.set_position(gtk.WIN_POS_CENTER)

        text = "Napisz maila na adres : letmehelpyou@youarewelcome.pl"

        label = gtk.Label()
        label.set_text(text)
        frame = gtk.Frame("W razie problemow z programem zalecane jest : ")
        frame.add(label)

        self.add(frame)
        self.show_all()
        gtk.main()        
        return
