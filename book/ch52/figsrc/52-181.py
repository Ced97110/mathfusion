import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 21, 52, r'$\mathbb{Z}/2\mathbb{Z}\times\mathbb{Z}/2\mathbb{Z}$', 'sujet', 'm')
text(ax, 66, 52, r'$\mathbb{Z}/4\mathbb{Z}$', 'autre', 'm')
for i, (p, q) in enumerate(((0, 0), (0, 1), (1, 0), (1, 1))):
    role = 'resultat' if (p, q) == (1, 1) else 'sujet'
    box(ax, 4 + (i % 2) * 18, 32 - (i // 2) * 12, 16, 9, role, label=f'({p}, {q})', size='s')
for i in range(4):
    role = 'varie' if i == 1 else 'autre'
    box(ax, 46 + i * 10, 32, 9, 9, role, label=str(i))
arrow(ax, (50.5, 41.5), (70.5, 41.5), 'limite', curve=-0.5)
text(ax, 21, 12, '(1, 1) + (1, 1) = (0, 0)', 'resultat', 's')
text(ax, 66, 12, '1 + 1 = 2 ≠ 0', 'limite', 's')
save(fig, '52-181')
