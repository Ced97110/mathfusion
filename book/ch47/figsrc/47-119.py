import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
f = lambda v: 6 + (v + 9) / 27 * 76
y = 26
text(ax, 44, 57, 'N = multiples de 3', 'sujet', 'm')
line(ax, [(4, y), (84, y)], 'fixe', lw=0.6)
for v in range(-9, 19):
    if v % 3 == 0: disc(ax, f(v), y, 1.3, 'sujet')
    else: disc(ax, f(v), y, 0.5, 'fixe')
disc(ax, f(0), y, 1.9, 'resultat'); disc(ax, f(15), y, 1.9, 'resultat'); disc(ax, f(-6), y, 1.9, 'autre')
for v, lab, role in [(-6, '−6', 'autre'), (0, '0 : neutre', 'resultat'), (6, '6', 'sujet'), (9, '9', 'sujet'), (15, '15', 'resultat')]:
    text(ax, f(v), y - 5, lab, role, 's')
arrow(ax, (f(6), y + 2), (f(15), y + 2), 'varie', curve=-0.45)
text(ax, f(10.5), y + 11, '6 + 9 = 15', 'resultat', 's')
arrow(ax, (f(6), y + 2), (f(-6), y + 2), 'varie', curve=0.45)
text(ax, f(0), y + 16, '−6 : l’opposé de 6', 'autre', 's')
save(fig, '47-119')
