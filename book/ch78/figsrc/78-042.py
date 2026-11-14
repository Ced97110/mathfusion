import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 59, r'$i,\ j,\ k$ : produit vectoriel', 'fixe', 'm')
terms = [(r'$(i\times i)\times j=0$', 'fixe'), (r'$(i\times j)\times i=j$', 'varie'), (r'$(j\times i)\times i=-j$', 'autre')]
for k, (l, r) in enumerate(terms):
    box(ax, 2 + k * 29, 38, 26, 11, r, label=l, size='s')
text(ax, 28, 43.5, r'$+$', 'encre', 'l'); text(ax, 57, 43.5, r'$+$', 'encre', 'l')
arrow(ax, (44, 31), (44, 22), 'resultat')
box(ax, 14, 9, 60, 12, 'resultat', label=r'$0 + j + (-j) = 0$')
save(fig, '78-042')
