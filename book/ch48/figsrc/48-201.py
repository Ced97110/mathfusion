import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
def mat(x, y, d, role):
    for i in range(2):
        for j in range(2):
            on = i == j
            box(ax, x + j * 7, y + (1 - i) * 7, 7, 7, role if on else 'fixe', lw=0.6, r=0.3,
                label=str(d[i]) if on else None)
mat(8, 40, (2, 1), 'sujet'); mat(36, 40, (3, 1), 'sujet'); mat(66, 40, (6, 1), 'resultat')
text(ax, 29, 47, r'$\times$', 'encre', 'l'); text(ax, 58, 47, '=', 'encre', 'l')
for x, v, r in ((15, '2', 'sujet'), (43, '3', 'sujet'), (73, '6', 'resultat')):
    arrow(ax, (x, 38.5), (x, 25), r)
    text(ax, x, 19, v, r, 'xl', weight='bold')
text(ax, 29, 19, r'$\times$', 'encre', 'l'); text(ax, 58, 19, '=', 'encre', 'l')
text(ax, 44, 31, 'det', 'varie', 'm') if False else text(ax, 25, 32, 'det', 'varie', 'm')
text(ax, 44, 8, 'cases grises : 0', 'fixe', 's')
text(ax, 44, 58, 'matrices', 'sujet', 's') if False else None
save(fig, '48-201')
