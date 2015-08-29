##
#!/usr/bin/python2
##
##
#   Script to Exit , logout , reboot , suspend  [ gdm / openbox ]
#   Depend : python2-imaging
#
#   http://crunchbanglinux.org/forums/topic/295/updated-openboxlogout-script/
##

import gtk
import os
import pwd
from PIL import Image, ImageFilter

class MyApp():
    def __init__(self):

        self.window = gtk.Window()
        self.window.set_title("Log Out ..")
        self.window.connect("destroy", self.doquit)
        self.window.connect("key-press-event", self.onkeypress)
        self.window.set_decorated(False)

        self.mainpanel = gtk.Fixed()
        self.window.add(self.mainpanel)

        self.screen_x , self.screen_y = gtk.gdk.screen_width(), gtk.gdk.screen_height()

        x = ( self.screen_x / 2 ) - ( 140 * 4 / 2 ) - 30
        y = ( self.screen_y / 2 ) - 100

        ## 1st Line
        self.add_bouton("application-exit",x+30,y+30)
        self.add_bouton("system-log-out",x+170,y+30)
        self.add_bouton("system-restart",x+310,y+30)
        self.add_bouton("system-shutdown",x+450,y+30)
       
        self.add_label("Retour",x+75, y+170)
        self.add_label("Deconnexion",x+196, y+170)
        self.add_label("Redemarrage",x+333, y+170)
        self.add_label("Extinction",x+486, y+170)


        self.set_background()

    def set_background(self):
        img_file = "/tmp/root_window.jpg"
        w = gtk.gdk.get_default_root_window()
        sz = w.get_size()
        pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
        pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
        if (pb != None):
            pb.save(img_file,"jpeg")
            image = Image.open(img_file)
            color = 'black'
            alpha = 0.5
            mask = Image.new("RGB", image.size, color)
            image = Image.blend(image, mask, alpha)
            image.save(img_file,"jpeg")

        pixbuf = gtk.gdk.pixbuf_new_from_file_at_size(img_file, self.screen_x, self.screen_y)
        pixmap, mask = pixbuf.render_pixmap_and_mask()
        # width, height = pixmap.get_size()
        self.window.set_app_paintable(True)
        self.window.resize(self.screen_x, self.screen_y)
        self.window.realize()
        self.window.window.set_back_pixmap(pixmap, False)
        self.window.move(0,0)
        del pixbuf
        del pixmap



    def add_bouton(self, name, x, y):
        image = gtk.Image()
        image.set_from_file("img/" + name + ".png")
        image.show()
        # un bouton pour contenir le widget image
        bouton = gtk.Button()
        bouton.set_relief(gtk.RELIEF_NONE)
        bouton.set_focus_on_click(False)
        bouton.set_border_width(0)
        bouton.set_property('can-focus', False)
        bouton.add(image)
        bouton.show()
        self.mainpanel.put(bouton, x,y)
        bouton.connect("clicked", self.clic_bouton, name)

    def add_label(self, name, x, y):
        label = gtk.Label(name)
        label.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse("white"))
        self.mainpanel.put(label, x, y)

    # Cette fonction est invoquee quand on clique sur un bouton.
    def clic_bouton(self, widget, data=None):

        if (data=='application-exit'):
            self.doquit()

        elif (data=='system-log-out'):
            os.system('openbox --exit')

        elif (data=='system-restart'):
            os.system('systemctl reboot')

        elif (data=='system-shutdown'):
            os.system('systemctl poweroff')


    def onkeypress(self, widget=None, event=None, data=None):
        if event.keyval == gtk.keysyms.Escape:
            self.doquit()

    def doquit(self, widget=None, data=None):
        gtk.main_quit()

    def run(self):
        self.window.show_all()
        gtk.main()

#-------------------------
if __name__ == "__main__":
#-------------------------
    ## need to change directory
    SRC_PATH = os.path.dirname( os.path.realpath( __file__ ) )
    os.chdir(SRC_PATH)
    app = MyApp()
    app.run()
