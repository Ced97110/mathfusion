import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 58, r'$\sigma$ : 3-cycle, d’ordre 3', 'sujet', 'm')
labs = [(r'$\sigma$', 'sujet'), (r'$\sigma^2$', 'sujet'), (r'$\sigma^3 = e$', 'fixe'), (r'$\sigma^4 = \sigma$', 'resultat')]
xs = [4 + i * 21 for i in range(4)]
for x, (s, r) in zip(xs, labs): box(ax, x, 36, 17, 10, r, label=s, size='s')
for x in xs[:3]:
    arrow(ax, (x + 17.4, 41), (x + 20.6, 41), 'varie')
ax.add_patch(FancyArrowPatch((xs[3] + 8.5, 47), (xs[0] + 8.5, 47), arrowstyle='<|-|>', mutation_scale=7, lw=0.9, color=COL['resultat'], connectionstyle='arc3,rad=-0.35', zorder=4))
text(ax, 44, 51.5, 'même élément', 'resultat', 's')
brace(ax, xs[1] + 8.5, xs[3] + 8.5, 35, 'varie', r'$(\sigma^2)^2 = \sigma^4$')
box(ax, 20, 5, 48, 9, 'resultat', label=r'$\sigma = (\sigma^2)^2$ : un carré', size='s', weight='bold')
save(fig, '50-156')
