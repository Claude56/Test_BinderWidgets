# coding: utf-8

#
# Bibliotheque de compatibilité du module turtle pour le manuel NSI de 1ere.
# v1.0 / avril 2021 / M. Beaudouin-Lafon
#
# Cette bibliothèque peut être importée à la place du module `turtle`.
# Elle remplace la fonction suivante :
#   ondrag(commande) - remplace turtle.ondrag avec une version reentrante
# et elle ajoute les fonctions suivantes :
#   write_text(t) - affiche le texte t
#   set_font(f) - change la police pour write_text
#   set_size(s) - change la taille pour write_text
#   set_style(s) - change le style pour write_text
#   set_align(a) - change l'alignement pour write_text
#
# Dans Jupyter, elle remplace (au mieux) le module `turtle` en utilisant `ipyturtle`.
# En particulier, elle ne traite pas les événements liés à la tortue.

import sys
if 'ipykernel' in sys.modules:
    import ipyturtle
    import math

    class NSITurtle(ipyturtle.Turtle):
        """ A turtle with closer functionality to the original Python turtle package """

        def __init__(self, width=320, height=320, fixed=True):
            ipyturtle.Turtle.__init__(self, width, height, fixed)

        def _reset(self):
            super()._reset()
            # fixing buggy _reset
            self._turtle_heading = 0.0
            self._turtle_heading_x = 1.0
            self._turtle_heading_y = 0.0

        def xcor(self):
            """ Retourner la coordonnée x de la tortue """
            return self._turtle_location_x

        def ycor(self):
            """ Retourner la coordonnée y de la tortue """
            return self._turtle_location_y

        def goto(self, x, y=None):
            """ Aller au point de coordonnées x, y """
            if y is None:
                y = x[1]
                x = x[0]

            cur_x = self._turtle_location_x
            cur_y = self._turtle_location_y
            self._turtle_location_x = x
            self._turtle_location_y = y

            if self._pen_on:
                precision = 4
                start = "{} {}".format(round(cur_x,precision),
                                       round(cur_y,precision))
                end = " {} {}".format(round(x, precision),
                                      round(y, precision))
                color = self._current_color
                if len(self._current_color)==0:
                    color = "rgb({},{},{})".format(self._current_color_rgb[0],
                                                   self._current_color_rgb[1],
                                                   self._current_color_rgb[2])
                self._line = start + end + " " + color

    _the_default_turtle = None
    _the_default_size = (400, 400)
    def _default_turtle():
        global _the_default_turtle
        if _the_default_turtle is None:
            w, h = _the_default_size
            _the_default_turtle = NSITurtle(w, h, True) # True -> fenetre flottante
            display(_the_default_turtle)
        return _the_default_turtle

    def forward(n):
        """ Avancer de n pas """
        _default_turtle().forward(n)

    def fd(n):
        """ Avancer de n pas """
        _default_turtle().forward(n)

    def backward(n):
        """ Reculer de n pas """
        _default_turtle().back(n)

    def back(n):
        """ Reculer de n pas """
        _default_turtle().back(n)

    def left(n):
        """ Tourner à gauche de n degrés """
        _default_turtle().left(n)

    def right(n):
        """ Tourner à droite de n degrés """
        _default_turtle().right(n)

    def penup():
        """ Lever le stylet """
        _default_turtle().penup()

    def pendown():
        """ Baisser le stylet """
        _default_turtle().pendown()

    def pencolor(c):
        """ Changer la couleur de l'encre """
        _default_turtle().pencolor(c)

    def xcor():
        """ Retourner la coordonnée x de la tortue """
        return _default_turtle().xcor()

    def ycor():
        """ Retourner la coordonnée y de la tortue """
        return _default_turtle().ycor()

    def heading():
        """ Retourner l'orientation de la tortue """
        return _default_turtle().heading()

    def setheading(h):
        """ Changer l'orientation de la tortue """
        t = _default_turtle()
        t._turtle_heading = h % 360
        t._turtle_heading_x = math.cos(math.radians(h))
        t._turtle_heading_y = math.sin(math.radians(h))

    def goto(x, y=None):
        """ Aller à la position x, y """
        _default_turtle().goto(x, y)

    def pensize(n):
        """ Changer l'épaisseur du trait (sans effet) """
        # _default_turtle().pendsize(n)
        pass

    def isdown():
        """ Retourner True si le stylet est abaissé """
        return _default_turtle().isdown()

    def clear():
        """ Effacer l'écran et remettre la tortue au centre """
        _default_turtle().reset()

    def speed(n):
        """ Changer la vitesse de déplacement (sans effet) """
        pass

    def listen():
        """ Ecouter les événements (sans effet) """
        pass

    def _turtle_not_implemented():
        print("gestion d'événements non implémentée sous Jupyter")

    def onkey(fun, key):
        """ Appeler fun lorsque la touche key est appuyée (sans effet) """
        _turtle_not_implemented()

    def onkeypress(fun, key=None):
        """ Appeler fun lorsque l'on enfonce la touche key (sans effet) """
        _turtle_not_implemented()

    def onkeyrelease(fun, key):
        """ Appeler fun lorsque l'on relâche la touche key (sans effet) """
        _turtle_not_implemented()

    def onscreenclick(fun, btn=1, add=None):
        """ Appeler fun lorsque l'on clique avec la souris sur la fenêtre de la tortue (sans effet) """
        _turtle_not_implemented()

    def onclick(fun, btn=1, add=None):
        """ Appeler fun lorsque l'on clique avec la souris sur la tortue (sans effet) """
        _turtle_not_implemented()

    def ondrag(fun, btn=1, add=None):
        """ Appeler fun lorsque l'on clique avec la souris sur la fenêtre de la tortue (sans effet) """
        _turtle_not_implemented()

    def onrelease(fun, btn=1, add=None):
        """ Appeler fun lorsque l'on reliache le bouton de la souris (sans effet) """
        _turtle_not_implemented()

    def ontimer(fun, t=0):
        """ Appelle fun après t secondes (sans effet) """
        _turtle_not_implemented()

    def write(txt):
        """ Ecrire le texte txt (appelle print) """
        print(txt)

else:
    # On n'est pas dans Jupyter
	
    # Eviter le bug qui plante MacOS avec TkInter et Python3 !
    import platform
    if platform.mac_ver()[0] != '' and platform.python_version_tuple()[0] != '2':
        exit('TkInter est incompatible avec Python3 sur ce Macintosh. Utiliser Python 2.x')

    # Importer la bonne version de TkInter
    if (platform.python_version_tuple()[0] == '2'):
        import Tkinter as tk
    else:
        import tkinter as tk

    from turtle import *
    import turtle

    # Redéfinition du `ondrag` de `turtle` pour éviter les appels réentrants a la callback
    _dragging = False

    def ondrag(f):
        """ Appelle f avec comme paramètre la position x,y du curseur lorsque l'on déplace la souris avec le bouton appuyé """
        def myf(x, y):
            global _dragging
            if _dragging:
                return
            _dragging = True
            f(x, y)
            _dragging = False
        turtle.ondrag(myf)

    turtle.listen()
    turtle.speed(0)

    # Fonctions pour écrire du texte dans la fenêtre tortue et contrôler son style
    _style = {
        'turtle': False,
        'font': 'Times',
        'size': 10,
        'style': 'normal',
        'align': 'left'
    }

    def write_text(s):
        """ Afficher le texte s à la position de la tortue """
        turtle.write(s, _style['turtle'], _style['align'],
            (_style['font'], _style['size'], _style['style']))

    def set_font(f):
        """ Changer la police d'affichage du texte """
        _style['font'] = f

    def set_size(s):
        """ Changer la taille de l'affichage de texte """
        _style['size'] = int(s)

    def set_style(s):
        """ Changer le style (normal/bold/italid) de l'affichage de texte """
        _style['style'] = s

    def set_align(a):
        """ Changer l'alignement (left/center/right) de l'affichage de texte par rapport à la position de la tortue """
        _style['align'] = a
