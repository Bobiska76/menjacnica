from tkinter import *

def promeni_u_din():
   unos = int(entry.get())
   unos = unos / 120
   output_label.configure(text='Evra: {:.1f}'.format(unos))
   entry.delete(0, END)

def promeni_u_eu():
   unos = int(entry.get())
   unos = unos * 120
   output_label.configure(text='Dinara: {:.1f}'.format(unos))
   entry.delete(0, END)





root = Tk()
root.title('Menjačnica')
massage_label = Label(text = 'Unesite koliko menjate', font = ('Tahoma', 12))                                       #poruka
output_label = Label(font =('Verdana', 16),bg='Black', fg='Red')                                                    #tekst rezultata
entry = Entry(font=('Verdana', 16), width=15)                                                                       #polje za unos
din_button = Button(text='Din >> EU', font=('Verdana', 12), command=promeni_u_din, bg='Blue', fg='White')           # menja vrednost u din
eu_button = Button(text = 'EU >> Din', font=('Verdana', 12), command=promeni_u_eu, bg='Yellow', fg='Red')           #menja vrednost u ev


massage_label.grid(row=0, column=1)                                                                                 # pozicija teksta
entry.grid(row=1, column=1)                                                                                         #pozicija polja za unos
din_button.grid(row=2, column=2)                                                                                    #Pozicija dugmica
eu_button.grid(row=2, column=0)

output_label.grid(row=3, column=0, columnspan=3)                                                                    #pozicija rezultata

mainloop()

