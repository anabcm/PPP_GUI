from gi.repository import Gtk

class Handler:
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

builder = Gtk.Builder()
builder.add_from_file("win.glade")
builder.connect_signals(Handler())

window = builder.get_object("window1")
window.show_all()
Gtk.main()