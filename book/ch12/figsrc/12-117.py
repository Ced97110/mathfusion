import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(104)
rows = [r'$4\,(a+b)$', r'$(a+b)+(a+b)+(a+b)+(a+b)$', r'$a+b+a+b+a+b+a+b$', r'$a+a+a+a+b+b+b+b$', r'$4a+4b$']
roles = ['sujet', 'fixe', 'fixe', 'varie', 'resultat']
labs = ['addition répétée', 'associativité : sans ( )', 'commutativité : étape clé', 'on compte']
lr = ['fixe', 'fixe', 'varie', 'fixe']
ys = [90, 70, 50, 30, 10]
for y, t, r in zip(ys, rows, roles):
    box(ax, 12, y, 64, 12, r, label=t, size='m')
for i, (l, r) in enumerate(zip(labs, lr)):
    arrow(ax, (14, ys[i] - 0.5), (14, ys[i + 1] + 12.5), r)
    text(ax, 18, ys[i] - 4, l, r, 's', ha='left', weight='bold' if r == 'varie' else 'normal')
save(fig, '12-117')
