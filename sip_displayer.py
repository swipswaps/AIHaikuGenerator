from tkinter import *
from sip_lstm import generate_SIP
import tkinter.font

def change_SIP():
	sip_text.set('')
	window.update()
	sip_text.set(generate_SIP(''))

def reset_SIP():
	sip_text.set('')
	window.update()
	sip_text.set(default_sip)

default_sip = 'authored by computer...\nshort Issa poems for you\nnow, click the button'

window = Tk()
window.title('SIP Generator')
window.configure(background='black')
window_size = 1000
window.geometry(str(window_size) + 'x' + str(window_size))
#window.resizable(width=False, height=False)

sip_text = StringVar()
sip_text.set(default_sip)
sip_font = tkinter.font.Font(family='Helvetica', size=36, weight='bold')
sip_label = Label(window, textvariable=sip_text, font=sip_font, bg='black', fg='white')
sip_label.place(relx=0.5, rely=0.4, anchor='c')

button_font = tkinter.font.Font(family='Helvetica', size=24, weight='bold')
generate_button = Button(window, text='Take a SIP', font=button_font, command=change_SIP)
generate_button.place(relx=0.5, rely=0.8, anchor='c')

small_font = tkinter.font.Font(family='Helvetica', size=12)
sub_label = Label(window, text='(Short Issa Poem)', font=small_font, bg='black', fg='white')
sub_label.place(relx=0.5, rely=0.85, anchor='c')

generate_button = Button(window, text='Reset SIP', font=small_font, command=reset_SIP)
generate_button.place(relx=0.5, rely=0.9, anchor='c')

mainloop()