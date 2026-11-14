import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 2, 68, 'écriture 1', 'sujet', 's', ha='left')
text(ax, 2, 18, 'écriture 2, rangée', 'varie', 's', ha='left')
xs = [18, 38, 58]
top = ['$2$', '$2$', '$3$']; bot = [r'$-2$', r'$-2$', '$3$']
for x, a, b in zip(xs, top, bot):
    box(ax, x, 46, 14, 12, 'sujet', label=a)
for x, b, r in zip(xs, bot, ['varie', 'varie', 'sujet']):
    box(ax, x, 4, 14, 12, r, label=b)
for x, lab, r in zip(xs, [r'$\times(-1)$', r'$\times(-1)$', r'$\times 1$'], ['varie', 'varie', 'resultat']):
    arrow(ax, (x + 7, 45), (x + 7, 17.5), r, both=True)
    text(ax, x + 8, 31, lab, r, 's', ha='left')
text(ax, 44, 64, '3 facteurs de chaque côté', 'resultat', 'm')
save(fig, '56-068')
