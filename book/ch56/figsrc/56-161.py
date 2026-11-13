import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 58, 70, 'anneau', 'autre', 'l', weight='bold')
text(ax, 78, 70, 'rng', 'sujet', 'l', weight='bold')
rows = ['addition', 'multiplication', 'distributivité', r'neutre $1$ pour $\times$']
for i, lab in enumerate(rows):
    y = 52 - i * 13
    text(ax, 2, y + 5, lab, 'encre', 'm', ha='left')
    box(ax, 48, y, 20, 10, 'resultat', label='✓', size='m')
    ok = i < 3
    box(ax, 70, y, 16, 10, 'resultat' if ok else 'limite', label='✓' if ok else '✗', size='m')
text(ax, 44, 7.5, r'rng : un anneau sans le $1$', 'sujet', 'm')
text(ax, 44, 2.5, r'ex. : $2\mathbb{Z}$, sans $1$ pair', 'sujet', 's')
save(fig, '56-161')
