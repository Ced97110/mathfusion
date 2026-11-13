import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 44, 52, '$z_k$ : la racine numéro k', 'sujet', 'l', weight='bold')
w, g, x0 = 20, 8, 5
subs = ['2', 'à 120°', 'à 240°']
for i in range(3):
    x = x0 + i * (w + g)
    box(ax, x, 22, w, 12, 'sujet', label=f'$z_{i}$', size='l')
    disc(ax, x + w / 2, 41, 3, 'varie', label=str(i), size='m')
    arrow(ax, (x + w / 2, 38), (x + w / 2, 35), 'varie', lw=0.9)
    text(ax, x + w / 2, 17, subs[i], 'fixe', 's')
text(ax, 85, 41, 'k', 'varie', 'm', ha='right', weight='bold')
brace(ax, x0, x0 + 3 * w + 2 * g, 12, 'varie', label='n = 3 racines : k de 0 à n − 1', down=True, size='s')
save(fig, '39-089')
