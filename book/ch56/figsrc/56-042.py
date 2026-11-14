import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 22, 66, 'irréductible', 'sujet', 'm')
text(ax, 66, 66, 'premier', 'autre', 'm')
# ligne ℤ : 7
text(ax, 44, 55, 'dans ℤ : 7', 'encre', 'm')
box(ax, 6, 38, 32, 13, 'resultat', label='ne se casse pas  ✓', size='s')
box(ax, 50, 38, 32, 13, 'resultat', label='divise un facteur  ✓', size='s')
text(ax, 44, 31, 'les deux vrais : ils coïncident', 'resultat', 's')
# ligne Z[√-5] : 2
text(ax, 44, 22, r'dans $\mathbb{Z}[\sqrt{-5}]$ : 2', 'encre', 'm')
box(ax, 6, 5, 32, 13, 'resultat', label='ne se casse pas  ✓', size='s')
box(ax, 50, 5, 32, 13, 'limite', label='divise un facteur  ✗', size='s')
save(fig, '56-042')
