import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
S = 48 / 230; xb = 28
rows = [('plan : ponctuels', 10, 'autre', 44), ('plan : groupes', 17, 'autre', 34), ('espace : ponctuels', 32, 'sujet', 20), ('espace : groupes', 230, 'sujet', 10)]
for (l, n, r, y) in rows:
    text(ax, 2, y, l, r, 's', ha='left')
    w = n * S
    box(ax, xb, y - 3, max(w, 1.8), 6, r, lw=0.7, r=0.5)
    text(ax, xb + w + 2.5, y, str(n), r, 'm', ha='left', weight='bold')
text(ax, 44, 52, 'le nombre dépend de la dimension', 'encre', 's')
save(fig, '74-180')
