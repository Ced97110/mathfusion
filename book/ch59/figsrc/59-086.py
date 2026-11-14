import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 4, 58, r'dans $\mathbb{Z}$ : taille = valeur absolue', 'fixe', 's', ha='left')
box(ax, 4, 42, 18, 11, 'sujet', label='12')
arrow(ax, (23, 47.5), (31, 47.5), 'varie')
box(ax, 32, 42, 28, 11, 'resultat', label=r'$|12|=12$')
text(ax, 4, 32, 'sans division : longueur', 'fixe', 's', ha='left')
box(ax, 4, 14, 18, 11, 'sujet', label='12')
arrow(ax, (23, 19.5), (31, 19.5), 'varie')
for i, (v, r) in enumerate([('2', 'autre'), ('2', 'autre'), ('3', 'autre')]):
    box(ax, 32 + i * 14, 14, 12, 11, r, label=v)
brace(ax, 32, 74, 13, 'resultat', label='longueur 3', down=True)
save(fig, '59-086')
