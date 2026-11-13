import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
# étape A : même repère
box(ax, 4, 60, 22, 9, 'sujet', label='(6 ; 1)')
box(ax, 62, 60, 22, 9, 'sujet', label='(0 ; −2)')
text(ax, 15, 56, '6 − 2 = 4', 'resultat', 's')
text(ax, 73, 56, '0 + 4 = 4', 'resultat', 's')
text(ax, 44, 64.5, 'même repère 4', 'resultat', 'm')
arrow(ax, (44, 51), (44, 44), 'fixe')
# étape B : k
box(ax, 14, 35, 60, 9, 'varie', label='k = 1 − (−2) = 3')
arrow(ax, (44, 34), (44, 27), 'fixe')
# étape C : différence
box(ax, 4, 18, 80, 9, 'sujet', label='(6 ; 3) = 3 × (2 ; 1)')
arrow(ax, (44, 17), (44, 11), 'fixe')
box(ax, 14, 2, 60, 9, 'resultat', label='dans N : même classe')
save(fig, '57-184')
