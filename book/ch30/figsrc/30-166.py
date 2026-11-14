import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
x0, W_, a = 14, 66, 11
for yb, fn, role, title, val in [(60, math.cos, 'sujet', 'départ à 5 : cosinus', '5'), (22, math.sin, 'autre', 'départ à 0 : sinus', '0')]:
    line(ax, [(x0, yb), (x0 + W_, yb)], 'fixe')
    line(ax, [(x0 + W_ * i / 100, yb + a * fn(2 * math.pi * i / 100)) for i in range(101)], role, lw=1.6)
    y_start = yb + a * fn(0)
    disc(ax, x0, y_start, 1.4, 'resultat')
    text(ax, 9, y_start, val, 'resultat', 's')
    text(ax, 2, yb + 16, title, role, 'm', ha='left')
save(fig, '30-166')
