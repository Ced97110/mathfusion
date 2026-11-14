import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def wave(ax, f, x0, w, y0, k, role, lw=1.1, dash=False, n=400, t1=2 * math.pi):
    line(ax, [(x0 + w * i / n, y0 + k * f(t1 * i / n)) for i in range(n + 1)], role, lw, dash)

fig, ax = canvas(80)
a = math.atan2(4, 3)
box(ax, 26, 64, 36, 12, 'sujet', label='une somme d’ondes', size='s')
arrow(ax, (36, 63), (22, 52), 'varie'); arrow(ax, (52, 63), (66, 52), 'varie')
wave(ax, lambda t: 5 * math.sin(t + a), 6, 36, 38, 2.2, 'resultat', 1.3)
text(ax, 24, 22, 'une seule onde', 'resultat', 'm'); text(ax, 24, 15, 'on lit la hauteur : 5', 'resultat', 's')
wave(ax, lambda t: 2 * abs(math.cos(t)), 48, 36, 38, 2.6, 'varie', 0.8, True)
wave(ax, lambda t: -2 * abs(math.cos(t)), 48, 36, 38, 2.6, 'varie', 0.8, True)
wave(ax, lambda t: math.sin(12 * t) + math.sin(14 * t), 48, 36, 38, 2.6, 'resultat', 0.9)
text(ax, 66, 22, 'un produit', 'resultat', 'm'); text(ax, 66, 15, 'on lit le facteur lent', 'varie', 's')
text(ax, 44, 5, 'mêmes valeurs dans les deux écritures', 'fixe', 's')
save(fig, '35-007')
