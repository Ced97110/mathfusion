import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 38, 56, 'k', 'sujet', 22)
text(ax, 50, 56, 'ℤ', 'fixe', 22)
text(ax, 20, 36, 'nombre choisi', 'sujet', 's')
text(ax, 68, 36, 'facteurs entiers', 'fixe', 's')
arrow(ax, (36, 49), (24, 40), 'sujet')
arrow(ax, (52, 49), (64, 40), 'fixe')
f = numberline(ax, 8, 70, 14, -14, 21, step=7, arrow_right=True)
for v in range(-14, 22, 7):
    disc(ax, f(v), 14, 1.5, 'resultat')
text(ax, 44, 26, r'$k = 7$ : multiples de 7', 'resultat', 's')
save(fig, '52-052')
