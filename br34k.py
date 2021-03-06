#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import mmap , sys , os , random , Tkinter , time
from PIL import Image , ImageTk

root = Tkinter.Tk() 

def clear() :
	for widget in root.winfo_children():
	    widget.destroy()

def key(event) :
	clear()
	br34k(sys.argv[2],random.randint(0,255))
	sh0w(sys.argv[2])

def reset(event) :
	python = sys.executable
	os.execl(python, python, * sys.argv)

def br34k(fn,x) :
	f = open(fn,"a+")
	m = mmap.mmap(f.fileno(),0)
	ft = fn.split(".")[-1]
	s = 0
	
	if "jpeg" in ft or "jpg" in ft :
		s = m.find(chr(int(0xff))+chr(int(0xda))) # start from the offset of 0xffda which is the start of the scan
	if "png" in ft :
		s = m.find("IDAT") # start from the offset of "IDAT" , I'm assuming there will be just one chunk , because I'm lazy
	
	m[random.randint(s,len(m)-1)] = chr(x)

	m.close()
	f.close()


def sh0w(fn) :
	root.update()
	try :
		im = Image.open(fn)
		im.thumbnail((500,500))
		tk_im = ImageTk.PhotoImage(im)
		label = Tkinter.Label(root,image=tk_im,height=500,width=500)
		label.pack()
		root.bind('<Return>', key)
		root.bind('r' , reset)
		root.wm_attributes("-topmost", 1)
		root.mainloop()
		im.close()
	except :
		reset(1)

def main() :
	if ( len(sys.argv) < 3 ) :
		print "Missing something !"
		print "$ python br34k_1mg.py filename.jpg output.jpg"
	else :
		os.system("cp "+sys.argv[1]+" "+sys.argv[2]) # Command injection lols
		sh0w(sys.argv[2])
		br34k( sys.argv[2], random.randint(0,255) )
	

if __name__ == "__main__" :
	main()
