import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
# (2, 1) + (5, 4) = (7, 5), case par case
bw, bh = 14, 9
cx = [40, 60]
text(ax, cx[0] + bw / 2, 58, 'riz', 'sujet', 's')
text(ax, cx[1] + bw / 2, 58, 'lentilles', 'autre', 's')
rows = [('client 1', 2, 1, 44, 'fixe'), ('client 2', 5, 4, 30, 'fixe'), ('ensemble', 7, 5, 12, 'resultat')]
for name, a, b, y, rl in rows:
    text(ax, 2, y + bh / 2, name, 'encre', 'm', ha='left')
    box(ax, cx[0], y, bw, bh, 'resultat' if rl == 'resultat' else 'sujet', label=str(a), size='l', weight='bold')
    box(ax, cx[1], y, bw, bh, 'resultat' if rl == 'resultat' else 'autre', label=str(b), size='l', weight='bold')
text(ax, 34, 34.5, '+', 'varie', 'xl', weight='bold')
line(ax, [(36, 26), (78, 26)], 'encre', lw=0.9)
text(ax, 34, 16.5, '=', 'resultat', 'xl', weight='bold')
save(fig, '58-003')
