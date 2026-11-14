import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
box(ax, 8, 61, 5, 5, 'sujet'); text(ax, 15, 63.5, 'atteintes : 12', 'sujet', 's', ha='left')
box(ax, 46, 61, 5, 5, 'limite'); text(ax, 53, 63.5, 'jamais : 12', 'limite', 's', ha='left')
x0, y0, cw, ch = 22, 20, 9, 7
for a in range(4):
    for b in range(6):
        ok = (a - b) % 2 == 0
        lab = '0, 12' if (a, b) == (0, 0) else None
        box(ax, x0 + b * cw, y0 + (3 - a) * ch, cw, ch, 'sujet' if ok else 'limite', label=lab, size='s', r=0.5)
text(ax, 11, y0 + 14, 'reste par 4', 'fixe', 's')
text(ax, x0 + 27, 14, 'reste par 6', 'fixe', 's')
text(ax, 44, 5, '4 × 6 = 24 paires', 'encre', 's')
save(fig, '52-182')
