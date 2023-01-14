#zad 8-13
class TV():
    def __init__(self)-> None:
        self.is_on=False
        self.channel_no=1
    def turn_on(self):
        self.is_on=True
    def turn_off(self):
        self.is_on=False

    def show_stat(self):
        if self.is_on:
            print("is on")
            print(self.channel_no)
        else: print("is off")

    def set_channel(self, new_channel):
        self.channel_no=new_channel





tv_set=TV()
tv_set.show_stat()
tv_set.turn_on()
tv_set.show_stat()
tv_set.turn_off()
tv_set.show_stat()
tv_set.turn_on()
tv_set.set_channel(4)
tv_set.show_stat()






