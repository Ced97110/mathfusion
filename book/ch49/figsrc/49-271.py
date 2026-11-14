import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
labs = ['00', '01', '10', '11']
xs = [14 + 20 * i for i in range(4)]
def row(y, kind, title, colour):
    text(ax, 44, y + 11, title, colour, 's')
    for i, (x, l) in enumerate(zip(xs, labs)):
        moved = kind == 'swap' and i in (1, 2)
        box(ax, x - 7, y - 4, 14, 8, 'varie' if moved else 'resultat', label=l, size='m')
    if kind == 'swap':
        arrow(ax, (xs[1] + 7.5, y), (xs[2] - 7.5, y), 'varie', both=True, lw=1.1)
row(58, 'id', 'neutre : 4 cycles, 16 fixes', 'resultat')
row(34, 'swap', 'échange : 3 cycles, 8 fixes', 'varie')
text(ax, 44, 10, r'$(16+8)\div2=12$', 'resultat', 'xl', weight='bold')
save(fig, '49-271')
