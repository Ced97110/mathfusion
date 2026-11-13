import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
cw, ch, x0, y0 = 15, 11, 30, 14
hs, ns = [0, 4, 8], [0, 6]
text(ax, 20, 50, r'$H$', 'sujet', 'l')
text(ax, 24, 44.5, r'$N$', 'autre', 'l')
for j, h in enumerate(hs):
    text(ax, x0 + cw * (j + .5), 50, str(h), 'sujet', 'm')
for i, n in enumerate(ns):
    text(ax, 24, 36 - ch * i, str(n), 'autre', 'm')
for i, n in enumerate(ns):
    for j, h in enumerate(hs):
        box(ax, x0 + cw * j, 31 - ch * i - 0, cw - 1, ch - 1, 'resultat', label=str((h + n) % 12))
text(ax, 62, 10, r'$HN$ : 6 sommes', 'resultat', 'm')
text(ax, 62, 56, r'$h + n$', 'encre', 'm')
save(fig, '48-035')
