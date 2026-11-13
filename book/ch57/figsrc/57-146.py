import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 15, 58, r'$M=\mathbb{Z}^2$', 'sujet', 'm')
text(ax, 71, 58, r'$M/N$', 'resultat', 'm')
text(ax, 43, 58, r'$\pi$', 'varie', 'xl', weight='bold')
ys = [40, 25, 10]
for s, y in zip([r'$(3\,;\,2)$', r'$(1\,;\,1)$', r'$(-1\,;\,0)$'], ys):
    box(ax, 4, y, 22, 10, 'sujet', label=s)
box(ax, 58, 18, 26, 24, 'resultat')
text(ax, 71, 36, 'une seule classe', 'resultat', 's')
text(ax, 71, 30, r'$\bar{x}$', 'resultat', 'l')
text(ax, 71, 23, r'$\pi(x)=\bar{x}$', 'resultat', 's')
for y, ty in zip(ys, [37, 30, 23]):
    arrow(ax, (26.5, y + 5), (57.5, ty), 'varie', lw=1.1)
save(fig, '57-146')
