import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(66)
for j, d in enumerate((1, 2, 4)): text(ax, 10.5 + j * 15, 60, f'$d={d}$', 'encre', 's', weight='bold')
for j in range(3):
    for y0, y1 in ((57, 49.8), (38.2, 31.8), (20.2, 13.8)): line(ax, [(10.5 + j * 15, y0), (10.5 + j * 15, y1)], 'fixe', lw=0.5, dash=True)
rows = [([1, 1, 2], 'sujet', r'$\varphi$ : $1+1+2=4$'), ([1, 1, 2], 'autre', r'degrés : $1+1+2=4$'), ([2, 2, 12], 'varie', r'comptage : $2+2+12=16$')]
for i, (vals, role, tot) in enumerate(rows):
    y = 44 - i * 18
    for j, v in enumerate(vals):
        box(ax, 4 + j * 15, y - 5, 13, 10, role, label=str(v))
    text(ax, 52, y, tot, role, 's', ha='left')
text(ax, 52, 4, r'$16=2^4$', 'varie', 's', ha='left')
save(fig, '80-471')
