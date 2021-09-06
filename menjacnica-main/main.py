from tkinter import *

def promeni_u_din():
   srednji_kurs = eval(kurs.get())
   unos = int(entry.get())
   unos = unos / srednji_kurs
   output_label.configure(text='Evra: {:.1f}'.format(unos))
   entry.delete(0, END)

def promeni_u_eu():
   unos = int(entry.get())
   sredni_kurs = eval(kurs.get())
   unos = unos * sredni_kurs
   output_label.configure(text='Dinara: {:.1f}'.format(unos))
   entry.delete(0, END)





root = Tk()
root.title('Menjačnica')
massage_label = Label(text = 'Unesite koliko menjate', font = ('Tahoma', 12))                                       #poruka
kurs_label = Label(text = 'Unesite kurs', font = ('Tahoma', 12))
output_label = Label(font =('Verdana', 16),bg='Black', fg='Red')                                                    #tekst rezultata
entry = Entry(font=('Verdana', 16), width=15)                                                                       #polje za unos
kurs = Entry(font=('Verdana', 16), width=15)
din_button = Button(text='Din >> EU', font=('Verdana', 12), command=promeni_u_din, bg='Blue', fg='White')           # menja vrednost u din
eu_button = Button(text = 'EU >> Din', font=('Verdana', 12), command=promeni_u_eu, bg='Yellow', fg='Red')           #menja vrednost u ev


massage_label.grid(row=0, column=0)                                                                                 # pozicija teksta
kurs_label.grid(row=0, column=2)
entry.grid(row=1, column=0)                                                                                         #pozicija polja za unos
kurs.grid(row=1, column=2)
din_button.grid(row=2, column=2)                                                                                    #Pozicija dugmica
eu_button.grid(row=2, column=0)

output_label.grid(row=3, column=0, columnspan=3)                                                                    #pozicija rezultata

mainloop()

