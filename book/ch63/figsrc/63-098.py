import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
box(ax, 3, 16, 38, 28, 'sujet')
labs = ['1', r'$\sigma$', r'$\tau$', r'$\sigma\tau$']
pos = [(15, 35), (29, 35), (15, 24), (29, 24)]
for l, (x, y) in zip(labs, pos):
    disc(ax, x, y, 4.5, 'encre', label=l, size='s')
text(ax, 22, 51, 'groupe : 4 éléments', 'sujet', 's')
text(ax, 65, 51, 'base : 4 éléments', 'autre', 's')
bl = ['1', r'$\sqrt{2}$', r'$\sqrt{3}$', r'$\sqrt{6}$']
for i, l in enumerate(bl):
    box(ax, 47 + i * 9.5, 28, 8, 9, 'autre', label=l, size='s')
brace(ax, 47, 84.5, 28, 'autre', label=r'$[E:\mathbb{Q}]=4$')
text(ax, 44, 33, '=', 'resultat', 'l', weight='bold')
text(ax, 44, 6, r'$4 = 4$ : aucun autre', 'resultat', 'm')
save(fig, '63-098')
