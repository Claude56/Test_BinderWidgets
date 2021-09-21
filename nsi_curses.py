# coding: utf-8

#
# Bibliotheque d'interface utilisateur pour le manuel NSI de 1ere.
# v1.0 / avril 2021 / M. Beaudouin-Lafon
#
# init_curses()
#	initialise l'écran du terminal en mode plein écran
#
# end_curses()
#	remet l'écran du terminal en mode normal
#
# clear()
#	efface l'écran du terminal
#
# add_str(x, y, ch)
#	affiche la chaine ch à la position x, y
#
# c = wait_key()
#	attend que l'on tape une touche et retourne le caractère tapé
#
# c = get_key(n)
#	attend au maximum n dixièmes de seconde que l'on tape un touche
#	retourne le caractère tapé, ou '' si on n'a rien tapé dans le délai imparti
#

import curses
import atexit

_screen = None

def init_curses():
	""" Initialiser l'écran """
	global _screen
	if _screen is None:
		_screen = curses.initscr()
		curses.noecho()
		curses.cbreak()
		_screen.keypad(True)
		_screen.clear()
		atexit.register(end_curses)

def end_curses():
	""" Terminer le mode plein écran """
	global _screen
	if _screen is not None:
		curses.nocbreak()
		_screen.keypad(False)
		curses.echo()
		_screen = None
		curses.endwin()
		atexit.unregister(end_curses)

def clear():
	if _screen is not None:
		_screen.clear()
		_screen.refresh()

def add_str(x, y, ch):
	""" Affiche la chaîne ch à la position x, y """
	if _screen is not None:
		_screen.addstr(y, x, ch)
		_screen.refresh()

def wait_key():
	""" Attend que l'on tape une touche et retourne le caractère tapé """
	if _screen is None:
		return None
	return _screen.getkey()

def get_key(n = 10):
	""" Retourne le caractère tapé ou '' si rien n'est tapé en n dixième de secondes """
	if _screen is None:
		return None

	curses.nocbreak()
	if n == 0:
		_screen.nodelay(True)
	else:
		curses.halfdelay(n)

	c = _screen.getch()
	if c == -1 or c >= 255:
		c = ''
	else:
		c = chr(c)

	if n == 0:
		_screen.nodelay(False)
	else:
		curses.nocbreak()
		curses.cbreak()

	return c

