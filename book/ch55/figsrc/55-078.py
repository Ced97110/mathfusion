import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
vals = [1, 2, 3, 4]
x0, w, step = 6, 9, 11
for i, v in enumerate(vals):
    text(ax, x0 + i * step + w / 2, 68, str(v), 'sujet', 'm', weight='bold')
triples = [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
total = 0
for r, t in enumerate(triples):
    y = 50 - r * 12
    for i in range(4):
        if i in t: box(ax, x0 + i * step, y, w, 9, 'sujet', r=0.5)
        else: box(ax, x0 + i * step, y, w, 9, 'fixe', fill=False, dash=True, r=0.5)
    p = vals[t[0]] * vals[t[1]] * vals[t[2]]; total += p
    text(ax, 54, y + 4.5, f'{vals[t[0]]}×{vals[t[1]]}×{vals[t[2]]} = {p}', 'varie', 'm', ha='left')
assert total == 50
text(ax, 44, 6, '6 + 8 + 12 + 24 = 50', 'resultat', 'l', weight='bold')
save(fig, '55-078')
