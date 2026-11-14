import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
# two polynomials with the same observation, two different outcomes
cols = [(2, 'sujet', r'$x^2+1$', 'irréductible', 'resultat'),
        (46, 'autre', r'$x^4+4$', 'se casse', 'varie')]
for x, role, name, verdict, vrole in cols:
    box(ax, x, 44, 40, 12, role, label=name, size='l')
    box(ax, x, 30, 40, 8, 'fixe', label='sans racine réelle', size='s')
    arrow(ax, (x + 20, 44), (x + 20, 38.5), 'fixe')
    arrow(ax, (x + 20, 30), (x + 20, 24.5), vrole)
    box(ax, x, 16, 40, 8, vrole, label=verdict, size='m')
text(ax, 44, 20, '≠', 'encre', 'xl', weight='bold')
box(ax, 2, 2, 40, 8, 'sujet', label='degré 2 ou 3 : racine', size='s', fill=False)
box(ax, 46, 2, 40, 8, 'autre', label='degré 4 : produit 2 × 2', size='s', fill=False)
save(fig, '54-204')
