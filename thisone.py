print('Ticket Prices:')
prices = dict(Fri=30, Sat=40, Sun=40, ThreeDayPass=100)
for days, price in prices.items():
    print('%s: $%d' % (days, price))

friday = dict(Billy='5pm', Johnny='6pm', TBD='7pm', Deb='8pm')
print('\nFriday Schedule:')
for time, performer in friday.items():
    print('%s: %s' % (performer, time))

saturday = dict(TBD='5pm', Bobby='6pm', Javier='7pm', Deb='8pm')
print('\nSaturday Schedule:')
for time, performer in friday.items():
    print('%s: %s' % (performer, time))

sunday = dict(Salina='1pm', Eric='2pm', TBD='3pm', Emily='4pm')
print('\nSunday Schedule:')
for time, performer in sunday.items():
    print('%s: %s' % (performer, time))



# This program demonstrates a group of Checkbutton widgets.

import tkinter
import tkinter.messagebox
from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E

class MyGUI:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()

        # Create two frames. One for the checkbuttons
        # and another for the regular Button widgets.
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create IntVar objects to use with
        # the Checkbuttons.
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()


        # Create the Checkbutton widgets in the top_frame.
        self.cb1 = tkinter.Checkbutton(self.top_frame, \
                   text='Friday', variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.top_frame, \
                   text='Saturday', variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.top_frame, \
                   text='Sunday', variable=self.cb_var3)
        self.cb4 = tkinter.Checkbutton(self.top_frame, \
                   text='3-Day Tickets', variable=self.cb_var4)


        # Pack the Checkbuttons.
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()


        # Create an OK button and a Quit button.
        self.ok_button = tkinter.Button(self.bottom_frame, \
                    text='Total', command=self.show_choice)

        # Pack the Buttons.
        self.ok_button.pack(side='left')

        # Pack the frames.
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Start the mainloop.
        tkinter.mainloop()

    # The show_choice method is the callback function for the OK button.

    def show_choice(self):
       # Create a message string.
        self.message = '\nYou selected:\n'
        total=0

        # Determine which Checkbuttons are selected and
        # build the message string accordingly.
        if self.cb_var1.get() == 1:
          self.message = self.message + 'Friday\n'
          total+=40.00
        if self.cb_var2.get() == 1:
          self.message = self.message + 'Saturday\n'
          total+=40.00
        if self.cb_var3.get() == 1:
          self.message = self.message + 'Sunday\n'
          total+=40.00
        if self.cb_var4.get() == 1:
          self.message = self.message + '3-Day tickets\n'
          total+=110.00

        
        # Display the message in an info dialog box.
        tkinter.messagebox.showinfo('Selection',('%s Total $%.2f') %(self.message, total))

        print(('%s Total $%.2f') %(self.message, total))

        
# Create an instance of the MyGUI class.
my_gui = MyGUI()
root = Tk()
root.mainloop()



    



