import turtle as t
t.pen(speed =0)

def vk(l, n):
	if n == 1:
		t.forward(l)
		return
	d = l / 3
	vk(d, n - 1)
	t.left(60)
	vk(d, n - 1)
	t.right(120)
	vk(d, n - 1)
	t.left(60)
	vk(d, n - 1)

def f(l, n):
	t.up()
	t.goto( - l / 2, l / 3 )
	t.down()
	for i in rang(3):
		vk(l, n)
		t.right(120)

f(300, 6)

"""

from tkinter import *
import os

t.ht()
ts = t.getscreen()
ts.getcanvas().postscript(file="{0}.eps".format("van_koch"))
t.mainloop()

"""
