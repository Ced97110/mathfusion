import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
f = numberline(ax, 6, 76, 24, 0, 420, step=60, every=3)
text(ax, 44, 52, 'deux passages de α à 180° − α', 'varie', 'm')
P = [(40, 'sujet', '40° = α'), (140, 'varie', '140° = 180° − α'), (400, 'sujet', '400° = α + 360°')]
for v, r_, s in P:
    disc(ax, f(v), 24, 1.3, r_)
    text(ax, f(v), 13.5, s, r_, 's')
for (a, b), lab in zip([(40, 140), (140, 400)], ['+ 180° et α devient −α', '+ 180° et −α devient α']):
    d = f(b) - f(a)
    arrow(ax, (f(a), 26.5), (f(b), 26.5), 'varie', curve=-0.5)
    text(ax, (f(a) + f(b)) / 2, 26.5 + 0.25 * d + 3.6, lab, 'varie', 's')
brace(ax, f(40), f(400), 9, 'resultat', label='2 × 180° = 360° = un tour entier')
save(fig, '32-055')
