import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
# ligne du haut : deux listes et leur somme
xs = [3, 32, 61]; w = 24
box(ax, xs[0], 56, w, 11, 'sujet', label='(3, (1, 2))', size='s')
box(ax, xs[1], 56, w, 11, 'autre', label='(1, (0, 5))', size='s')
box(ax, xs[2], 56, w, 11, 'fixe', label='(4, (1, 7))', size='s')
text(ax, 29.5, 61.5, '+', 'encre', 'l', weight='bold')
text(ax, 58.5, 61.5, '=', 'encre', 'l', weight='bold')
# l'assemblage s'applique
for x, r in zip(xs, ['sujet', 'autre', 'resultat']):
    arrow(ax, (x + w / 2, 55), (x + w / 2, 33), r)
    text(ax, x + w / 2 + 3, 44, r'$\eta$', r, 'm')
box(ax, xs[0], 21, w, 11, 'sujet', label='9', weight='bold')
box(ax, xs[1], 21, w, 11, 'autre', label='7', weight='bold')
box(ax, xs[2], 21, w, 11, 'resultat', label='16', weight='bold')
text(ax, 29.5, 26.5, '+', 'encre', 'l', weight='bold')
text(ax, 58.5, 26.5, '=', 'encre', 'l', weight='bold')
text(ax, 44.5, 10, r'$\eta$ de la somme = somme des $\eta$', 'resultat', 's', weight='bold')
save(fig, '58-243')
