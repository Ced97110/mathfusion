import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
rows = [(48, 3, r'$|3|=3$', '3 pas', 'autre'), (28, -3, r'$|-3|=3$', '3 pas', 'sujet'), (8, 0, r'$|0|=0$', '0 pas', 'fixe')]
for y, v, lab, pas, r in rows:
    f = numberline(ax, 36, 82, y + 6, -4, 4, labels=False, arrow_right=False, tick=0.8)
    text(ax, 18, y + 6, lab, 'resultat', 'l')
    line(ax, [(f(0), y + 6), (f(v), y + 6)], 'resultat', lw=2.4)
    disc(ax, f(0), y + 6, 1.4, 'fixe')
    if v: disc(ax, f(v), y + 6, 1.8, r)
    text(ax, (f(0) + f(v)) / 2 if v else f(0), y + 12, pas, 'resultat', 's')
save(fig, '13-043')
