import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 60, '≅', 'resultat', 'xl')
text(ax, 18, 59, r'$\mathbb{Z}/2\mathbb{Z}$', 'sujet', 'm', weight='bold')
text(ax, 70, 59, 'parité', 'autre', 'm', weight='bold')
for k, (a, b) in enumerate([('0', 'pair'), ('1', 'impair')]):
    y = 38 - k * 15
    box(ax, 8, y, 24, 10, 'sujet', label=a)
    box(ax, 56, y, 24, 10, 'autre', label=b)
    arrow(ax, (34, y + 5), (54, y + 5), 'resultat', both=True)
box(ax, 2, 4, 32, 11, 'sujet', label=r'$1 + 1 = 0$')
box(ax, 48, 4, 38, 11, 'autre', label='impair + impair = pair', size='s')
arrow(ax, (36, 9.5), (46, 9.5), 'resultat', both=True)
save(fig, '55-056')
