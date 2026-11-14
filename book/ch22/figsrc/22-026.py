import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
y = 22
f = numberline(ax, 8, 76, y, -4, 4, 1, labels=False)
line(ax, [(f(0), y - 5), (f(0), y + 14)], 'fixe', dash=True)
text(ax, f(0), y - 7, '0', 'fixe', 's')
disc(ax, f(-3), y, 1.6, 'resultat'); disc(ax, f(3), y, 1.6, 'resultat')
text(ax, f(-3), y + 5, r'$-r$', 'resultat', 'm'); text(ax, f(3), y + 5, r'$r$', 'resultat', 'm')
arrow(ax, (f(-3), y + 12), (f(3), y + 12), 'varie', both=True)
text(ax, f(0) + 0.0, y + 17, 'opposés', 'varie', 's')
text(ax, f(-3), y - 5, r'$(-3)^2 = 9$', 'resultat', 's')
text(ax, f(3), y - 5, r'$3^2 = 9$', 'resultat', 's')
box(ax, 14, 44, 60, 9, 'sujet', label='9 > 0 : deux racines')
save(fig, '22-026')
