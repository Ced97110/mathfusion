import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(85)
def row(y, head, hrole, els):
    text(ax, 3, y + 11, head, hrole, 'm', ha='left', weight='bold')
    for i, e in enumerate(els):
        last = i == len(els) - 1
        box(ax, 4 + i * 17, y, 13, 8, 'resultat' if last else hrole, label=str(e), size='m')
        if not last: arrow(ax, (18 + i * 17, y + 4), (20 + i * 17, y + 4), 'fixe')
row(62, r'$\mathbb{Z}/4$ : ordre 4 (pas 1, 2, 3, 0)', 'sujet', [1, 2, 3, 0])
row(38, r'$U(5)$ : ordre 4 (2, 4, 3, 1)', 'autre', [2, 4, 3, 1])
text(ax, 3, 27, r'$U(8)$ : jamais d’ordre 4', 'limite', 'm', ha='left', weight='bold')
for i, e in enumerate([3, 5, 7]):
    x = 4 + i * 28
    box(ax, x, 11, 10, 8, 'limite', label=str(e), size='m')
    arrow(ax, (x + 11, 15), (x + 13, 15), 'fixe')
    box(ax, x + 14, 11, 10, 8, 'resultat', label='1', size='m')
text(ax, 44, 5, 'deux pas suffisent', 'limite', 's')
save(fig, '45-236')
