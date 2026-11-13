import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
box(ax, 2, 28, 19, 11, 'autre', fill=False, dash=True)
box(ax, 22, 28, 19, 11, 'sujet', label='4', size='l', lw=1.4)
box(ax, 42, 28, 19, 11, 'autre', label='3', size='l')
for x, d in zip([63, 71, 79], '290'):
    box(ax, x, 28, 7, 11, 'fixe', label=d, size='l')
text(ax, 2, 48, 'centaines de mille', 'autre', 's', ha='left')
text(ax, 31.5, 44, 'dizaines de mille', 'sujet', 's')
text(ax, 51.5, 48, 'milliers', 'autre', 's')
text(ax, 11.5, 24, '100 000', 'autre', 's')
text(ax, 31.5, 24, '10 000', 'sujet', 's')
text(ax, 51.5, 24, '1 000', 'autre', 's')
for x, t in [(31.5, '40 000'), (51.5, '3 000')]:
    arrow(ax, (x, 22.5), (x, 17), 'resultat')
    text(ax, x, 14, t, 'resultat', 'm')
brace(ax, 22, 61, 11, 'resultat', label='quarante-trois mille')
save(fig, '01-068')
