import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 28, 57, 'cas de base', 'sujet', 'm')
text(ax, 62, 57, 'atteints à partir de lui', 'fixe', 's')
rows = [(46, 'axiomes', '0', 0.8, 'normal'), (32, 'définition', '0 ! = 1', 0.8, 'normal'),
        (18, 'preuve', r'$E(0)$ vraie', 1.6, 'bold')]
cxs = [46, 56, 66, 76]
for y, lab, case, lw, wt in rows:
    text(ax, 3, y, lab, 'encre', 's', ha='left', weight=wt)
    box(ax, 18, y - 5, 20, 10, 'sujet', label=case, size='m', lw=lw)
    for c in cxs: disc(ax, c, y, 2, 'fixe', fill=False)
    arrow(ax, (38, y), (cxs[0] - 2, y), 'fixe')
    for a, b in zip(cxs[:-1], cxs[1:]): arrow(ax, (a + 2, y), (b - 2, y), 'fixe')
save(fig, '01-117')
