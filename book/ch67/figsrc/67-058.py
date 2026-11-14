import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
box(ax, 14, 62, 60, 10, 'sujet', label=r'$u=1+i$ dans $\mathbb{F}_9$')
box(ax, 4, 44, 32, 10, 'varie', label=r'$1+i$')
box(ax, 52, 44, 32, 10, 'varie', label=r'$1-i$')
text(ax, 44, 49, r'$\times$', 'varie', 'l')
arrow(ax, (30, 62), (20, 54.5), 'fixe')
arrow(ax, (58, 62), (68, 54.5), 'fixe')
arrow(ax, (44, 44), (10, 28), 'fixe')
labs = [r'$1-i^2$', r'$1-(-1)$', r'$1+1$', '2']
for k, s in enumerate(labs):
    box(ax, 2 + 22 * k, 18, 16, 10, 'resultat' if k == 3 else 'fixe', label=s, size='s')
    if k:
        arrow(ax, (18 + 22 * (k - 1), 23), (2 + 22 * k, 23), 'fixe')
text(ax, 44, 11, r'$i^2=2=-1$ dans $\mathbb{F}_3$', 'varie', 's')
text(ax, 44, 4, r'$N_{E/F}(u)=2$', 'sujet', 'm')
save(fig, '67-058')
