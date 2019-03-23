from sip_lstm import generate_sip
from tkinter import *
import datetime
import tkinter.font

def change_sip():
	sip_text.set('loading...')
	window.update()
	sip_text.set(generate_sip(['']))

def reset_sip():
	sip_text.set('')
	window.update()
	sip_text.set(default_sip)

def save_sip():
	file = open('saved_sips/sip_%s.txt' % datetime.datetime.now(), 'w')
	file.write(sip_text.get())
	file.close()

default_sip = 'authored by computer...\nshort Issa poems for you\nnow, click the button'

window = Tk()
window.title('SIP Generator')
window.configure(background='black')
window_size = 1000
window.geometry(str(window_size) + 'x' + str(window_size))

sip_text = StringVar()
sip_text.set(default_sip)
sip_font = tkinter.font.Font(family='Helvetica', size=36, weight='bold')
sip_label = Label(window, textvariable=sip_text, font=sip_font, bg='black', fg='white')
sip_label.place(relx=0.5, rely=0.4, anchor='c')

generate_font = tkinter.font.Font(family='Helvetica', size=24, weight='bold')
generate_button = Button(window, text='Take a SIP', font=generate_font, command=change_sip)
generate_button.place(relx=0.5, rely=0.8, anchor='c')

small_font = tkinter.font.Font(family='Helvetica', size=12)
sub_label = Label(window, text='(Short Issa Poem)', font=small_font, bg='black', fg='white')
sub_label.place(relx=0.5, rely=0.85, anchor='c')

reset_button = Button(window, text='Reset SIP', font=small_font, command=reset_sip)
reset_button.place(relx=0.25, rely=0.9, anchor='c')

save_button = Button(window, text='Save SIP', font=small_font, command=save_sip)
save_button.place(relx=0.75, rely=0.9, anchor='c')

mainloop()