import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
# digits of 32,116
xs = [8, 19, 37, 48, 63]; ds = ['3', '2', '1', '1', '6']
for x, d in zip(xs, ds):
    r = 'varie' if d == '6' and x == 63 else ('sujet')
    box(ax, x, 44, 10, 11, r, label=d, size='l')
text(ax, 32, 47, ',', 'encre', 'l')
text(ax, 42.5, 60, 'centièmes', 'sujet', 's')
text(ax, 68, 60, 'à regarder', 'varie', 's')
brace(ax, 8, 58, 42, 'sujet', 'on garde', down=True)
arrow(ax, (68, 43), (68, 31), 'varie')
box(ax, 40, 22, 40, 9, 'varie', label=r'$6 \geq 5$ : on ajoute 1', size='s')
arrow(ax, (50, 22), (50, 14), 'resultat')
text(ax, 50, 9, '32,12', 'resultat', 'l')
save(fig, '08-042')
