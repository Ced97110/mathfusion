import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
rows = [('fixe', r'$1+(-1)=0$'),
        ('varie', r'$(-1)\times\left(1+(-1)\right)=0$'),
        ('sujet', r'$(-1)\times1+(-1)\times(-1)=0$'),
        ('fixe', r'$-1+(-1)\times(-1)=0$'),
        ('resultat', r'$(-1)\times(-1)=1$')]
ys = [72 - 17 * i for i in range(5)]
for (r, e), y in zip(rows, ys):
    box(ax, 12, y, 64, 10, r, label=e, weight='bold' if r == 'sujet' else 'normal')
for i in range(4):
    yt, yb = ys[i], ys[i + 1] + 10
    arrow(ax, (20, yt - 0.3), (20, yb + 0.3), 'varie' if i != 1 else 'sujet')
labels = ['$\\times(-1)$ des deux côtés', 'on développe', '$-1\\times1=-1$', 'donc ? est l’opposé de $-1$']
for i in range(4):
    text(ax, 24, (ys[i] + ys[i + 1] + 10) / 2, labels[i], 'varie' if i != 1 else 'sujet', 's', ha='left')
save(fig, '13-075')
