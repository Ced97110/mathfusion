import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
cx = [41.5, 59.5, 77.5]
for c, h in zip(cx, ['ensemble', 'opération', 'neutre']):
    text(ax, c, 50, h, 'encre', 's', weight='bold')
rows = [(34, '(ℕ, +, 0)', ['ℕ', '+', '0'], ['sujet'] * 3),
        (16, '(ℕ, ×, 1)', ['ℕ', '×', '1'], ['sujet', 'autre', 'autre'])]
for y, tri, labs, roles in rows:
    text(ax, 4, y, tri, 'encre', 'm', ha='left', weight='bold')
    for c, l, r in zip(cx, labs, roles):
        box(ax, c - 7.5, y - 5, 15, 10, r, label=l, size='l')
text(ax, 44, 5, 'même ensemble, autre triplet', 'autre', 's')
save(fig, '44-059')
