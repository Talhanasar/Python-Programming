class Laptop:
    def parts(self):
        print('Keyboard, Display, Motherboard')



my_laptop = Laptop()
my_laptop.parts()


class Desktop(Laptop):
    def weight(self):
        print('Desktops are heavy-weight')


my_desktop = Desktop()
my_desktop.parts()
my_desktop.weight()