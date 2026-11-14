import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
u = 5.0; s = 7 * u
poly(ax, [(4, 14), (4 + s, 14), (4 + s, 14 + s), (4, 14 + s)], 'sujet')
text(ax, 4 + s / 2, 14 + s / 2, 'aire 49', 'sujet', 'm')
text(ax, 4 + s / 2, 14 + s + 4, r'côté $a = 7$', 'sujet', 's')
disc(ax, 4 + s, 14 + s, 1.0, 'varie')
text(ax, 44, 54, r'$b = 0$ : rien à retirer', 'varie', 's', ha='left')
arrow(ax, (50, 52.5), (4 + s + 1.5, 14 + s + 0.5), 'varie')
text(ax, 65, 40, r'$(7+0)(7-0) = 49$', 'sujet', 's')
text(ax, 65, 33, '=', 'resultat', 'l')
text(ax, 65, 26, r'$7^2 - 0^2 = 49$', 'resultat', 's')
save(fig, '15-132')
