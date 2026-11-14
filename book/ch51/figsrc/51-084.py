import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
box(ax, 2, 2, 84, 64, 'fixe')
text(ax, 6, 62, r'$R$ : les fractions', 'fixe', 's', ha='left')
box(ax, 8, 6, 72, 50, 'sujet')
text(ax, 12, 52, r'$S$ : les entiers', 'sujet', 's', ha='left')
disc(ax, 20, 40, 4, 'resultat', label='0'); disc(ax, 34, 40, 4, 'resultat', label='1')
text(ax, 60, 40, 'contient 0 et 1', 'resultat', 's')
text(ax, 43, 28, 'reste dans S :', 'varie', 's')
for i, n in enumerate(['somme', 'différence', 'produit']):
    box(ax, 12 + i * 22, 12, 19, 10, 'resultat', label=n, size='s')
save(fig, '51-084')
