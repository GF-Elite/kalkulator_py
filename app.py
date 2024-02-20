
from tkinter import *

root = Tk()

# judul appku
root.title("appku")
# judul appku

layar = Entry(root, width=31, borderwidth=5)
layar.grid(column=0, row=0, columnspan=3)

def tambahAngka(angka):
	angkaPer = layar.get()
	layar.delete(0, END)
	layar.insert(0, str(angkaPer) + str(angka))

def hapus():
	layar.delete(0, END)

def samaDengan():
	angka_kedua = layar.get()
	layar.delete(0, END)

	if math == "tambah":
		layar.insert(0, angkaFirst + int(angka_kedua))

	if math == "kurang":
		layar.insert(0, angkaFirst - int(angka_kedua))

	if math == "kali":
		layar.insert(0, angkaFirst * int(angka_kedua))

	if math == "bagi":
		layar.insert(0, angkaFirst / int(angka_kedua))


def tambah():
	angka_pertama = layar.get()
	layar.delete(0, END)
	global angkaFirst
	global math
	angkaFirst = int(angka_pertama)
	math = "tambah"


def kurang():
	angka_pertama = layar.get()
	layar.delete(0, END)
	global angkaFirst
	global math
	angkaFirst = int(angka_pertama)
	math = "kurang"

def kali():
	angka_pertama = layar.get()
	layar.delete(0, END)
	global angkaFirst
	global math
	angkaFirst = int(angka_pertama)
	math = "kali"

def bagi():
	angka_pertama = layar.get()
	layar.delete(0, END)
	global angkaFirst
	global math
	angkaFirst = int(angka_pertama)
	math = "bagi"


angka1 = Button(root, text=1, padx=40, pady=20, command=lambda: tambahAngka(1))
angka2 = Button(root, text=2, padx=40, pady=20, command=lambda: tambahAngka(2))
angka3 = Button(root, text=3, padx=40, pady=20, command=lambda: tambahAngka(3))
angka4 = Button(root, text=4, padx=40, pady=20, command=lambda: tambahAngka(4))
angka5 = Button(root, text=5, padx=40, pady=20, command=lambda: tambahAngka(5))
angka6 = Button(root, text=6, padx=40, pady=20, command=lambda: tambahAngka(6))
angka7 = Button(root, text=7, padx=40, pady=20, command=lambda: tambahAngka(7))
angka8 = Button(root, text=8, padx=40, pady=20, command=lambda: tambahAngka(8))
angka9 = Button(root, text=9, padx=40, pady=20, command=lambda: tambahAngka(9))
angka0 = Button(root, text=0, padx=40, pady=20, command=lambda: tambahAngka(0))

hapus = Button(root, text="hapus", padx=73, pady=20, command=hapus)
samaDengan = Button(root, text="=", padx=87, pady=20, command=samaDengan)

tambah = Button(root, text="+", padx=40, pady=20, command=tambah)
kurang = Button(root, text="-", padx=40, pady=20, command=kurang)
bagi = Button(root, text="/", padx=40, pady=20, command=bagi)

kali = Button(root, text="*", padx=40, pady=20, command=kali)

angka1.grid(column=0, row=1)
angka2.grid(column=1, row=1)
angka3.grid(column=2, row=1)

angka4.grid(column=0, row=2)
angka5.grid(column=1, row=2)
angka6.grid(column=2, row=2)

angka7.grid(column=0, row=3)
angka8.grid(column=1, row=3)
angka9.grid(column=2, row=3)

angka0.grid(column=0, row=4)

hapus.grid(column=1, row=4, columnspan=2)
samaDengan.grid(column=1, row=5, columnspan=2)

tambah.grid(column=0, row=5)
kurang.grid(column=0, row=6)
kali.grid(column=1, row=6)

bagi.grid(column=2, row=6)

root.mainloop()







