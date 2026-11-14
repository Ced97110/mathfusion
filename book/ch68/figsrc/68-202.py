import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from kit_L07 import *

fig, ax = canvas(76)
xs, p = brow(fig, ax, 44, 38, '0123456', roles=['resultat' if i == 4 else 'fixe' for i in range(7)])
x4 = xs[4]
box(ax, x4 - 24, 60, 48, 10, 'sujet', label='syndrome reçu : α⁴', size='s')
arrow(ax, (x4, 59), (x4, 42.5), 'varie')
text(ax, x4 + 3, 51, 'on le cherche', 'varie', 's', ha='left')
text(ax, 2, 27, 'liste : αⁱ pour i de 0 à 6', 'fixe', 's', ha='left')
arrow(ax, (x4, 34.5), (x4, 21), 'resultat')
text(ax, x4, 13, 'i = 4 : position de l’erreur', 'resultat', 'm')
save(fig, '68-202')
