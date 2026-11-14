import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
# corps de départ F (2 éléments) -> un seul ajout -> K (8 éléments) qui contient les 3 racines
box(ax, 3, 24, 24, 20, 'fixe', label='F\n2 éléments')
arrow(ax, (27, 34), (40, 34), 'varie', lw=1.2)
text(ax, 33.5, 40, r'$+\ r_1$', 'varie', 'm')
text(ax, 33.5, 27.5, '1 étage', 'varie', 's')
box(ax, 40, 6, 45, 52, 'resultat')
text(ax, 62.5, 52.5, 'K : 8 éléments', 'resultat', 'm', weight='bold')
xs = [49, 62.5, 76]
labs = [r'$r_1$', r'$r_1^{2}$', r'$r_1^{4}$']
for x, l in zip(xs, labs):
    disc(ax, x, 38, 5, 'sujet', label=l, size='m')
text(ax, 62.5, 27.5, 'les 3 racines de', 'encre', 's')
text(ax, 62.5, 23.5, r'$x^3+x+1$ sont dans K', 'encre', 's')
text(ax, 62.5, 12, '8 = 2³ : pas un ℤ/pℤ', 'resultat', 's')
save(fig, '62-133')
