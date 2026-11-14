import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
# modulo 5 : f = 2 + 3x^5 ; 2 = 2^5 and 3 = 3^5 ; f = (2+3x)^5
text(ax, 2, 72, 'départ', 'sujet', 's', ha='left')
box(ax, 22, 65, 62, 12, 'sujet', label=r'$f=2+3x^5$')
arrow(ax, (54, 64.5), (54, 56), 'fixe')
text(ax, 2, 50, 'étape clé', 'varie', 's', ha='left')
box(ax, 22, 43, 62, 12, 'varie', label=r'$2=2^5$ et $3=3^5$')
arrow(ax, (54, 42.5), (54, 34), 'fixe')
text(ax, 2, 28, 'arrivée', 'resultat', 's', ha='left')
box(ax, 22, 21, 62, 12, 'resultat', label=r'$f=(2+3x)^5$')
arrow(ax, (54, 20.5), (54, 12), 'limite')
box(ax, 12, 2, 72, 10, 'limite', label='puissance 5-ième : pas irréductible', size='s')
save(fig, '62-115')
