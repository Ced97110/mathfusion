import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
def row(y, ann, mod, discs, tag):
    box(ax, 2, y - 6, 16, 12, 'fixe', label='R = ℤ', size='s')
    arrow(ax, (18.5, y), (25, y), 'varie', lw=1.1)
    box(ax, 25, y - 6, 24, 12, 'varie', label=ann, size='s')
    arrow(ax, (49.5, y), (53, y), 'varie', lw=1.1)
    text(ax, 71, y + 10, mod, 'sujet', 's', weight='bold')
    n = len(discs)
    for i, t in enumerate(discs):
        x = 71 + (i - (n - 1) / 2) * 8.5
        disc(ax, x, y - 1, 3.2, 'sujet', label=t, size='s')
text(ax, 44, 78, 'module cyclique = anneau ÷ annulateur', 'encre', 's', weight='bold')
row(54, 'ann x = 0', 'Rx ≅ ℤ', ['', '', ''], 'a')
text(ax, 56.5, 54 - 1, '…', 'sujet', 'l')
text(ax, 85.5, 54 - 1, '…', 'sujet', 'l')
row(22, 'ann x = 3ℤ', 'Rx : 3 éléments', ['0', '4 h', '8 h'], 'b')
text(ax, 25, 38, 'x = (2 ; 1)', 'sujet', 's')
text(ax, 25, 6, 'x = 4 h', 'sujet', 's')
save(fig, '57-168')
