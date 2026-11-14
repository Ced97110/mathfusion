import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
vals = ['2', '3', '4', '5']; bw, g = 14, 4; x0 = (88 - (4 * bw + 3 * g)) / 2
for k, v in enumerate(vals):
    box(ax, x0 + k * (bw + g), 36, bw, 12, 'varie' if k == 3 else 'sujet', label=v, size='l')
brace(ax, x0, x0 + 2 * (bw + g) + bw, 49.5, 'sujet', label='', down=False)
text(ax, x0 + (2 * (bw + g) + bw) / 2, 58.5, r'référence des $n-1$ : $9$', 'sujet', 's')
text(ax, x0 + 3 * (bw + g) + bw / 2, 54, r'dernier $a_{n}$', 'varie', 's')
arrow(ax, (x0 + 3 * (bw + g) + bw / 2, 52.5), (x0 + 3 * (bw + g) + bw / 2, 48.5), 'varie')
arrow(ax, (44, 35), (44, 24), 'fixe')
text(ax, 62, 29.5, 'à gauche', 'fixe', 's')
box(ax, 20, 8, 48, 14, 'resultat', label=r'$9+5=14$', size='l')
save(fig, '45-105')
