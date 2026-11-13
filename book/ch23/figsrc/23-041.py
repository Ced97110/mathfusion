import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
f = numberline(ax, 6, 76, 44, -4, 4, step=1, labels=False, arrow_right=False)
text(ax, 44, 57, 'k = 9 : deux solutions', 'sujet', 's')
for v, lab in ((-3, '−3'), (3, '3')):
    disc(ax, f(v), 44, 1.8, 'resultat'); text(ax, f(v), 38.5, lab, 'resultat', 'm')
f2 = numberline(ax, 6, 76, 16, -4, 4, step=1, labels=False, arrow_right=False)
text(ax, 44, 29, 'k = 0 : une solution', 'sujet', 's')
disc(ax, f2(0), 16, 2.2, 'resultat'); text(ax, f2(0), 10.5, '0', 'resultat', 'm')
text(ax, 44, 4, '√0 et −√0 : même nombre', 'fixe', 's')
save(fig, '23-041')
