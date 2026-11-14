import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 44, 51, r'$G$ : 12 éléments', 'encre', 'm')
for gx, role, lab, sub in [(12.25, 'sujet', '2-Sylow : 4 éléments', r'$2^2=4$'), (56.25, 'autre', '3-Sylow : 3 éléments', r'$3^1=3$')]:
    for r in range(3):
        for c in range(4):
            on = (r == 0) if role == 'sujet' else (c == 0)
            disc(ax, gx + 6.5 * c, 40 - 6.5 * r, 2.4, role if on else 'fixe')
    text(ax, gx + 9.75, 19, lab, role, 'm')
    text(ax, gx + 9.75, 13, sub, role, 'm')
save(fig, '50-038')
