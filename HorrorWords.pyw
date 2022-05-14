from tkinter import *
from random import choice
from PIL import Image, ImageTk
from audioplayer import AudioPlayer
import os
import sys
import webbrowser
def restart():
	os.execl(sys.executable, sys.executable, *sys.argv)
win = Tk()
introplayer = AudioPlayer("data/intro.mp3")
introplayer.play(loop = 0, block = 0)
musicplayer = AudioPlayer("data/horror.mp3")
musicplayer.play(loop = True, block = False)
ws = win.winfo_screenwidth()
hs = win.winfo_screenheight()
Label(win, bg = "black", bd = 0, width = 960, height = 540).place(x = 0, y = 0)
#win.iconbitmap('data/icon.ico')
win.geometry("%dx%d+%d+%d" % (960, 540, ws/2 - 480, hs/2 - 270))
win.resizable(0, 0)
win.title("Horror Words")

image = Image.open("data/initbg.jpg")
image = image.resize((960, 540), Image.ANTIALIAS)
my_img0 = ImageTk.PhotoImage(image)
initimg = Label(image = my_img0)
initimg.image = my_img0
initimg.pack()

word = choice(open("data/words.txt","r").readline().split())
guesses = ""
guess = ""
health = ["♥", "♥", "♥", "♥", "♥", "♥", "♥", "♥", "♥", "♥"]
var = 0
def web(site):
	webbrowser.open(site, new = 2)
def main():
	global playbutt, settingsbutt, aboutbutt, quitbutt
	playbutt = Button(text = "   Play   ", padx = 45, pady = 17, bg = "black", fg = "red", relief = "ridge", command = tuto, cursor = "hand2", activebackground = "black", activeforeground = "white", font = ("system", 15), highlightthickness = 0)
	playbutt.place(x = 585, y = 200)
	settingsbutt = Button(text = "Settings", padx = 45, pady = 17, bg = "black", fg = "red", relief = "ridge", command = settings, cursor = "hand2", activebackground = "black", activeforeground = "white", font = ("system", 15), highlightthickness = 0)
	settingsbutt.place(x = 585, y = 340)
	aboutbutt = Button(text = "   About ", padx = 45, pady = 17, bg = "black", fg = "red", relief = "ridge", command = about, cursor = "hand2", activebackground = "black", activeforeground = "white", font = ("system", 15), highlightthickness = 0)
	aboutbutt.place(x = 585, y = 270)
	quitbutt = Button(text = "   Quit    ", padx = 45, pady = 17, bg = "black", fg = "red", relief = "ridge", command = win.quit, cursor = "hand2", activebackground = "black", activeforeground = "white", font = ("system", 15), highlightthickness = 0)
	quitbutt.place(x = 585, y = 410)
		
		
		
	
	
def settings():
	image = Image.open("data/settingsbg.jpg")
	image = image.resize((960, 540), Image.ANTIALIAS)
	my_img0 = ImageTk.PhotoImage(image)
	settingsimg = Label(image = my_img0, bd = 0)
	settingsimg.image = my_img0
	settingsimg.place(x = 0, y = 0)

	def onbutt():
		global on
		on = Button(win, text = "ON", command = lambda : [offbutt(), musicplayer.pause(), on.destroy(), backbutt.destroy()], bg = "black", fg = "red", activeforeground = "white", activebackground = "black", width = 4, height = 1, cursor = "hand2", font = ("system", 960//32), bd = 0, highlightthickness = 0)
		on.place(x = 960/1.54, y = 540/4.15)
		backbutt = Button(win, text = "Back", command = lambda : [on.destroy(), aboutbutt.destroy(), settingsimg.destroy(), backbutt.destroy()], fg = "red", bg = "black", cursor = "hand2")
		backbutt.place(x = 960/1.2, y = 540/1.102)
	def offbutt():
		global off
		off = Button(win, text = "OFF", command = lambda : [onbutt(), musicplayer.play(loop = True, block = False), off.destroy(), backbutt.destroy()], bg = "black", fg = "red", activeforeground = "white", activebackground = "black", width = 4, height = 1, cursor = "hand2", font = ("system", 960//32), bd = 0, highlightthickness = 0)
		off.place(x = 960/1.54, y = 540/4.15)
		backbutt = Button(win, text = "Back", command = lambda : [off.destroy(), aboutbutt.destroy(), settingsimg.destroy(), backbutt.destroy()], fg = "red", bg = "black", cursor = "hand2")
		backbutt.place(x = 960/1.2, y = 540/1.102)
	onbutt()
	aboutbutt = Button(win, text = "hrogus.herokuapp.com", command = lambda : [web("hrogus.herokuapp.com")], bg = "black", fg = "red", activeforeground = "white", activebackground = "black", width = 20, height = 1, cursor = "hand2", font = ("system", 960//53), bd = 0, highlightthickness = 0)
	aboutbutt.place(x = 960/1.5, y = 540/2.25)
	
	
	
	
def about():
	label = Label(win, bg = "black", padx = 960, pady = 540)
	label.place(x = 0, y = 0)
	txt = Label(label, text = "Hello everyone !\nthis game was developped by taha namir (me)\nIt has a concept of playing the hangman game with some horror added to it !\n\nFor those who don't know what the hangman game is;\nIt's a game where you have to guess the selected word by trying every\nletter you get in your mind before there are no chances left.\n\nI hope you like it", fg = "red", bg = "black", font = ("system", 16))
	txt.place(x = 220, y = 100)
	linkbutt = Button(win, text = "MyPaypalAccount", command = lambda : [web("paypal.com/tahanamir")], bg = "black", fg = "red", activebackground = "white", cursor = "hand2")
	linkbutt.place(x = 960/2.315, y = 540/1.35)
	backbutt = Button(win, text = "Back", cursor = "hand2", command = lambda : [label.destroy(), linkbutt.destroy(), txt.destroy(), backbutt.destroy()], bg = "black", fg = "red", activebackground = "white")
	backbutt.place(x = 960/2.1, y = 540/1.2)
def tuto():
	global runningmusic
	playbutt.destroy()
	settingsbutt.destroy()
	aboutbutt.destroy()
	quitbutt.destroy()
	initimg.destroy()
	
	image = Image.open("data/tutobg.png")
	image = image.resize((960, 540), Image.ANTIALIAS)
	my_img0 = ImageTk.PhotoImage(image)
	my_img1 = Label(image = my_img0)
	my_img1.image = my_img0
	my_img1.pack()

	runningmusic = AudioPlayer("data/run.mp3")
	startbutt = Button(win, text = "Start the adventure", font = ("system", 960//64), cursor = "hand2", command = lambda : [runningmusic.play(loop = 1, block = False), my_img1.destroy(), startbutt.destroy(), play()])
	startbutt.place(x = 960/2.3, y = 960/2.133)
	
def play():
	global guesses, entry, blood, var, vidlabel_, b
	musicplayer.pause()
	if var == 0 :
		image = Image.open("data/playbg.jpg")
		image = image.resize((960, 540), Image.ANTIALIAS)
		my_img0 = ImageTk.PhotoImage(image)
		vidlabel_ = Label(image = my_img0)
		vidlabel_.image = my_img0
		vidlabel_.pack()
	var = 1
	
	b = Button(text = "Quit", padx = 960/29.09, pady = 960/80, bd = 1, bg = "black", fg = "white", relief = "raised", activebackground = "grey", activeforeground = "black", command = win.quit, cursor = "hand2")
	b.place(x = 960/1.16, y = 960/2.042)
	blood = Label(win, text = health, bg = "black", fg = "white")
	blood.place(x = (960/2 - 6), y = 960/9.6 , anchor="center")
	
	d = Button(win, text = "Retry", padx = 960/29.09, pady = 960/80, bd = 1, fg = "white", bg = "black", relief = "raised", command = restart, cursor = "hand2", activebackground = "grey", activeforeground = "black")
	d.place(x = 25, y = 960/2.042)
	
	entry = Entry(text = "guess the letter", width = 4, justify = "center", fg = "white", bg = "black")
	entry.place(x = (960/2 - 8), y = 260, anchor="center")
	entry.focus_force()
	#PROJECT TO ADD LETTERS BUTTONS INSIDE THE GAME SO NO NEED TO USE THE KEYBOARD
	
	a = Button(win, text = "a", cursor = "hand1", bg = "black", fg = "white", activebackground = "grey", activeforeground = "black", command = lambda : [entry.insert(0, "a"), getentry("<Return>")])
	a.place(x = 190, y = 350)
	
	z = Button(win, text = "z", cursor = "hand1", bg = "black", fg = "white", activebackground = "grey", activeforeground = "black", command = lambda : [entry.insert(0, "z"), getentry("<Return>")])
	z.place(x = 250, y = 350)
	
	e = Button(win, text = "e", cursor = "hand1", bg = "black", fg = "white", activebackground = "grey", activeforeground = "black", command = lambda : [entry.insert(0, "e"), getentry("<Return>")])
	e.place(x = 310, y = 350)
	
	r = Button(win, text = "r", cursor = "hand1", bg = "black", fg = "white", activebackground = "grey", activeforeground = "black", command = lambda : [entry.insert(0, "r"), getentry("<Return>")])
	r.place(x = 370, y = 350)
	
	t = Button(win, text = "t", cursor = "hand1", bg = "black", fg = "white", activebackground = "grey", activeforeground = "black", command = lambda : [entry.insert(0, "t"), getentry("<Return>")])
	t.place(x = 430, y = 350)
	
	y = Button(win, text = "y", cursor = "hand1", bg = "black", fg = "white", activebackground = "grey", activeforeground = "black", command = lambda : [entry.insert(0, "y"), getentry("<Return>")])
	y.place(x = 490, y = 350)
	
	u = Button(win, text = "u", cursor = "hand1", bg = "black", fg = "white", activebackground = "grey", activeforeground = "black", command = lambda : [entry.insert(0, "u"), getentry("<Return>")])
	u.place(x = 550, y = 350)
	
	i = Button(win, text = "i", cursor = "hand1", bg = "black", fg = "white", activebackground = "grey", activeforeground = "black", command = lambda : [entry.insert(0, "i"), getentry("<Return>")])
	i.place(x = 610, y = 350)
	
	o = Button(win, text = "o", cursor = "hand1", bg = "black", fg = "white", activebackground = "grey", activeforeground = "black", command = lambda : [entry.insert(0, "o"), getentry("<Return>")])
	o.place(x = 670, y = 350)
	
	p = Button(win, text = "p", cursor = "hand1", bg = "black", fg = "white", activebackground = "grey", activeforeground = "black", command = lambda : [entry.insert(0, "p"), getentry("<Return>")])
	p.place(x = 730, y = 350)
	
	########## next line
		
	q = Button(win, text = "q", cursor = "hand1", bg = "black", fg = "white", activebackground = "grey", activeforeground = "black", command = lambda : [entry.insert(0, "q"), getentry("<Return>")])
	q.place(x = 190, y = 400)
	
	s = Button(win, text = "s", cursor = "hand1", bg = "black", fg = "white", activebackground = "grey", activeforeground = "black", command = lambda : [entry.insert(0, "s"), getentry("<Return>")])
	s.place(x = 250, y = 400)
	
	d = Button(win, text = "d", cursor = "hand1", bg = "black", fg = "white", activebackground = "grey", activeforeground = "black", command = lambda : [entry.insert(0, "d"), getentry("<Return>")])
	d.place(x = 310, y = 400)
	
	f = Button(win, text = "f", cursor = "hand1", bg = "black", fg = "white", activebackground = "grey", activeforeground = "black", command = lambda : [entry.insert(0, "f"), getentry("<Return>")])
	f.place(x = 370, y = 400)
	
	g = Button(win, text = "g", cursor = "hand1", bg = "black", fg = "white", activebackground = "grey", activeforeground = "black", command = lambda : [entry.insert(0, "g"), getentry("<Return>")])
	g.place(x = 430, y = 400)
	
	h = Button(win, text = "h", cursor = "hand1", bg = "black", fg = "white", activebackground = "grey", activeforeground = "black", command = lambda : [entry.insert(0, "h"), getentry("<Return>")])
	h.place(x = 490, y = 400)
	
	j = Button(win, text = "j", cursor = "hand1", bg = "black", fg = "white", activebackground = "grey", activeforeground = "black", command = lambda : [entry.insert(0, "j"), getentry("<Return>")])
	j.place(x = 550, y = 400)
	
	k = Button(win, text = "k", cursor = "hand1", bg = "black", fg = "white", activebackground = "grey", activeforeground = "black", command = lambda : [entry.insert(0, "k"), getentry("<Return>")])
	k.place(x = 610, y = 400)
	
	l = Button(win, text = "l", cursor = "hand1", bg = "black", fg = "white", activebackground = "grey", activeforeground = "black", command = lambda : [entry.insert(0, "l"), getentry("<Return>")])
	l.place(x = 670, y = 400)
	
	m = Button(win, text = "m", cursor = "hand1", bg = "black", fg = "white", activebackground = "grey", activeforeground = "black", command = lambda : [entry.insert(0, "m"), getentry("<Return>")])
	m.place(x = 730, y = 400)
	
	###### next line
	
	w = Button(win, text = "w", cursor = "hand1", bg = "black", fg = "white", activebackground = "grey", activeforeground = "black", command = lambda : [entry.insert(0, "w"), getentry("<Return>")])
	w.place(x = 310, y = 450)
	
	x = Button(win, text = "x", cursor = "hand1", bg = "black", fg = "white", activebackground = "grey", activeforeground = "black", command = lambda : [entry.insert(0, "x"), getentry("<Return>")])
	x.place(x = 370, y = 450)
	
	c = Button(win, text = "c", cursor = "hand1", bg = "black", fg = "white", activebackground = "grey", activeforeground = "black", command = lambda : [entry.insert(0, "c"), getentry("<Return>")])
	c.place(x = 430, y = 450)
	
	v = Button(win, text = "v", cursor = "hand1", bg = "black", fg = "white", activebackground = "grey", activeforeground = "black", command = lambda : [entry.insert(0, "v"), getentry("<Return>")])
	v.place(x = 490, y = 450)
	
	b = Button(win, text = "b", cursor = "hand1", bg = "black", fg = "white", activebackground = "grey", activeforeground = "black", command = lambda : [entry.insert(0, "b"), getentry("<Return>")])
	b.place(x = 550, y = 450)
	
	n = Button(win, text = "n", cursor = "hand1", bg = "black", fg = "white", activebackground = "grey", activeforeground = "black", command = lambda : [entry.insert(0, "n"), getentry("<Return>")])
	n.place(x = 610, y = 450)
	
	###########################game algo
	failed = 0
	lista = ""
	for char in word:
		if char in guesses:
			lista += char+" "	
		else:
			lista += "_ "
			failed += 1
	txt = Label(win, text = lista, bg = "black", fg = "white")
	txt.place(x = (960/2 - len(lista)/2 ), y = 200, anchor="center")
		
	def getentry(retrunbutt):
		global guesses, entry, blood, vidlabel_
		guess = entry.get()
		entry.delete(0, END)
		if guess not in word:
			if len(health) > 1 :
				lol = AudioPlayer("data/incorrect.mp3")
				lol.play(block = 0, loop = 1)
				win.after(1150, lol.stop)
				image = Image.open("data/danger.png")
				image = image.resize((960, 540), Image.ANTIALIAS)
				my_img0 = ImageTk.PhotoImage(image)
				redhurt = Label(image = my_img0, bd = 0)
				redhurt.image = my_img0
				redhurt.place(x = 0, y = 0)
				win.after(120, redhurt.destroy)
			else :
				lul = AudioPlayer("data/lose.mp3")
				lul.play(block = 0, loop = 1)
				win.after(1150, lul.stop)
			if "♥" in health :
				health.pop()
				blood.destroy()
		else :
			lil = AudioPlayer("data/correct.mp3")
			lil.play(block = 0, loop = 1)
			win.after(600, lil.stop)
			guesses += guess
		blood.destroy()
		
		if "♥" not in health :
			
			vidlabel_.destroy()
			image = Image.open("data/losebg.jpg")
			image = image.resize((960, 540), Image.ANTIALIAS)
			my_img0 = ImageTk.PhotoImage(image)
			my_label = Label(image = my_img0, bd = 0)
			my_label.image = my_img0
			my_label.place(x = 0, y = 0)
			but1 = Button(text = "Replay ", padx = 29, pady = 12, bd = 0, bg = "black", fg = "red", relief = "groove", activebackground = "#002638", command = restart, cursor = "hand2")
			but1.place(x = 600, y = 310)
			but2 = Button(text = " Quit ", padx = 33, pady = 12, bd = 0, bg = "black", fg = "red", relief = "groove", command = win.quit, activebackground = "#002638", cursor = "hand2")
			but2.place(x = 600, y = 370)
		else :
			play()

	win.bind("<Return>", getentry)
	if lista.replace(" ", "").replace("\n", "") == word :
		vidlabel_.destroy()
		
		yay = AudioPlayer("data/yay.mp3")
		yay.play(block = 0, loop = 1)
		win.after(1100, yay.stop)
		image = Image.open("data/win1.jpg")
		image = image.resize((960, 540), Image.ANTIALIAS)
		my_img0 = ImageTk.PhotoImage(image)
		vidlabel0 = Label(image = my_img0, bd = 0)
		vidlabel0.image = my_img0
		vidlabel0.pack()
		win.after(3000, vidlabel0.destroy)
		image = Image.open("data/win2.jpg")
		image = image.resize((960, 540), Image.ANTIALIAS)
		my_img0 = ImageTk.PhotoImage(image)
		vidlabel0 = Label(image = my_img0, bd = 0)
		vidlabel0.image = my_img0
		vidlabel0.pack()
		but1 = Button(text = "Replay ", padx = 29, pady = 12, bd = 1, bg = "black", fg = "white", relief = "raised", activebackground = "grey", command = restart, cursor = "hand2")
		but1.place(x = 15, y = 470)
		but2 = Button(text = "Quit ", padx = 29, pady = 12, bd = 1, bg = "black", fg = "white", relief = "raised", command = win.quit, activebackground = "grey", cursor = "hand2")
		but2.place(x = 850, y = 470)
main()

win.mainloop()