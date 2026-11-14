import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
for y, lab, r in [(44, r'$x > 0$ : deux racines', 'sujet'), (14, r'$x = 0$ : une seule racine', 'varie')]:
    f = numberline(ax, 8, 70, y, -3, 3, 1, labels=False)
    text(ax, 44, y + 12, lab, r, 'm')
    line(ax, [(f(0), y - 4), (f(0), y + 5)], 'fixe', dash=True)
text(ax, 39, 36.5, '0', 'fixe', 's')
f = lambda v: 8 + (v + 3) / 6 * 62
disc(ax, f(-2), 44, 1.6, 'resultat'); disc(ax, f(2), 44, 1.6, 'resultat')
text(ax, f(-2), 49.5, r'$-r$', 'resultat', 's'); text(ax, f(2), 49.5, r'$r$', 'resultat', 's')
disc(ax, f(0), 14, 1.9, 'varie')
text(ax, f(0), 6, r'$0\times 0 = 0$', 'varie', 's')
text(ax, 62, 21, r'$-0 = 0$', 'varie', 's')
save(fig, '22-027')
