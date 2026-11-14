import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
box(ax, 1.5, 1.5, 85, 63, 'fixe', fill=False, dash=True)
text(ax, 44, 59, 'règle suggérée, pas prouvée', 'fixe', 'm')
box(ax, 4, 10, 39, 44, 'resultat'); box(ax, 45, 10, 39, 44, 'limite')
text(ax, 23.5, 49, 'un seul premier', 'resultat', 's')
text(ax, 64.5, 49, 'deux premiers différents', 'limite', 's')
for i, (v, p) in enumerate([('2', 2), (r'$2^2$', 2), ('3', 3)]):
    box(ax, 6 + i * 12.3, 28, 10, 9, 'sujet' if p == 2 else 'autre', label=v)
# 6 = 2 x 3 : the two different primes, each in its own color
text(ax, 54, 32.5, '6 =', 'limite', 'l', weight='bold')
disc(ax, 64, 32.5, 4, 'sujet', label='2', size='m')
text(ax, 71, 32.5, r'$\times$', 'limite', 'm')
disc(ax, 78, 32.5, 4, 'autre', label='3', size='m')
text(ax, 23.5, 18, 'garanti', 'resultat', 'l', weight='bold')
text(ax, 64.5, 18, 'non garanti', 'limite', 'l', weight='bold')
save(fig, '50-020')
