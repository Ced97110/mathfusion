import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
text(ax, 44, 42, 'on ajoute un bit : le total de 1 devient pair', 'encre', 'm')
rows = [('0110', '0', 26, 'deux 1 : on ajoute 0\ntotal 2, pair'),
        ('0111', '1', 8, 'trois 1 : on ajoute 1\ntotal 4, pair')]
for w, add, y, s in rows:
    for i, b in enumerate(w):
        box(ax, 4 + i * 9.5, y, 8, 8, 'autre', label=b, size='l')
    box(ax, 4 + 4 * 9.5, y, 8, 8, 'varie', label=add, size='l')
    text(ax, 55, y + 4, s, 'encre', 's', ha='left')
save(fig, '68-010')
