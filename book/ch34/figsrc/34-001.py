import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
k = 60
text(ax, 6, 47, r'addition : sin 30° + sin 45°', 'encre', 'm', ha='left')
box(ax, 6, 36, 0.5*k, 8, 'sujet', label='0,5')
box(ax, 6 + 0.5*k, 36, 0.7071*k, 8, 'autre', label='0,7071')
brace(ax, 6, 6 + 1.2071*k, 36, 'limite', label='somme : 1,2071')
text(ax, 6, 25, r'calculatrice : sin 75°', 'encre', 'm', ha='left')
box(ax, 6, 14, 0.9659*k, 8, 'resultat', label='0,9659')
line(ax, [(6 + k, 10), (6 + k, 50)], 'fixe', dash=True)
text(ax, 6 + k, 53, '1', 'fixe', 'm')
save(fig, '34-001')
