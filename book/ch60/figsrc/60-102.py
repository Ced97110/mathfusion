import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
xs = [4, 34, 64]
for k, x in enumerate(xs):
    box(ax, x, 44, 20, 10, 'sujet', label=r'$\mathbb{Z}/2$', size='l')
    if k < 2:
        text(ax, x + 25, 49, '⊕', 'encre', 'l')
sums = [('1', '1'), ('0', '0'), ('1', '1')]
for x, (a, b) in zip(xs, sums):
    arrow(ax, (x + 10, 43), (x + 10, 35), 'varie')
    box(ax, x, 22, 20, 12, 'varie', label=f'{a} + {b} = 0')
text(ax, 44, 12, r'$(1,0,1)+(1,0,1)=(0,0,0)$', 'resultat', 'm')
text(ax, 44, 4.5, 'chaque triplet non nul : ordre 2', 'resultat', 's')
save(fig, '60-102')
