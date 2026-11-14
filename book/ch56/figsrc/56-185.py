import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 65, r'dans le corps $\mathbb{Q}$', 'sujet', 'm')
disc(ax, 25, 36, 22, 'sujet')
text(ax, 25, 56, 'unités', 'sujet', 's')
for (x, y, s) in [(16, 40, r'$3$'), (32, 42, r'$\frac{1}{3}$'), (17, 26, r'$\frac{5}{3}$'), (33, 29, r'$-2$')]:
    text(ax, x, y, s, 'sujet', 'm')
disc(ax, 25, 36, 22, 'sujet', fill=False)
disc(ax, 70, 52, 5, 'fixe', label='0')
text(ax, 70, 43, 'seul non-unité', 'fixe', 's')
box(ax, 50, 10, 36, 22, 'resultat')
text(ax, 68, 26, r'$5=3\times\frac{5}{3}+0$', 'resultat', 's')
text(ax, 68, 17, 'reste toujours 0', 'resultat', 's')
save(fig, '56-185')
