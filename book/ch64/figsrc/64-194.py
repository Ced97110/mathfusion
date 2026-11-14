import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
val = (5 ** 0.5 - 1) / 4
assert abs(val - 0.309) < 0.001
text(ax, 44, 65, r'un étage, exposant 2', 'varie', 'm')
box(ax, 8, 32, 26, 12, 'sujet', label=r'$\mathbb{Q}$')
box(ax, 54, 32, 26, 12, 'sujet', label=r'$\mathbb{Q}(\sqrt{5})$')
arrow(ax, (35, 38), (53, 38), 'varie')
text(ax, 44, 48, 'racine carrée', 'varie', 's')
f = numberline(ax, 10, 70, 12, 0, 1, step=0.5, arrow_right=False)
disc(ax, f(val), 12, 1.8, 'resultat')
arrow(ax, (f(val), 24), (f(val), 15), 'resultat')
text(ax, f(val), 28, r'$(\sqrt{5}-1)/4\approx0{,}309$', 'resultat', 's')
text(ax, 80, 12, r'cos $72^\circ$', 'fixe', 's')
save(fig, '64-194')
