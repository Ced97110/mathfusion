import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
f = lambda v: 44 + v * 14
arrow(ax, (4, 38), (84, 38), 'fixe', lw=0.9, both=True)
for v in (-1, 0, 1):
    ax.plot([f(v)] * 2, [36.8, 39.2], color=COL['fixe'], lw=0.8)
    text(ax, f(v), 33.5, f'{v}'.replace('-', '−'), 'fixe', 's')
line(ax, [(f(-1), 38), (f(1), 38)], 'sujet', lw=4.5)
text(ax, 44, 46, 'sinus et cosinus : de −1 à 1', 'sujet', 'm')
arrow(ax, (4, 16), (84, 16), 'resultat', lw=1.4, both=True)
for v, s in ((0.08, '0,08'), (1, '1')):
    disc(ax, f(v), 16, 1.2, 'resultat')
text(ax, f(0.08) - 1.5, 11, '0,08', 'resultat', 's', ha='right')
text(ax, f(1) + 1, 11, '1', 'resultat', 's')
disc(ax, 74, 16, 1.2, 'resultat'); text(ax, 74, 11, '1 000', 'resultat', 's')
text(ax, 44, 22, 'tangente : tous les nombres', 'resultat', 'm')
save(fig, '33-065')
