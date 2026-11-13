import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 44, 77, r'$\tan(A+B)=(\tan A+\tan B)\div(1-\tan A\tan B)$', 'sujet', 's')
box(ax, 4, 56, 36, 9, 'sujet', True, label=r'$\tan A=0{,}5774$', size='s')
box(ax, 48, 56, 36, 9, 'sujet', True, label=r'$\tan B=0{,}5774$', size='s')
box(ax, 4, 32, 36, 10, 'varie', True, label='somme : 1,1547', size='s')
box(ax, 48, 32, 36, 10, 'varie', True, label='1 − produit : 0,6667', size='s')
for a in (22, 66):
    for b in (22, 66):
        arrow(ax, (a, 56), (b, 42.5), 'fixe', lw=0.7)
box(ax, 14, 8, 60, 10, 'resultat', True, label='quotient : 1,732 = tan 60°', size='s')
arrow(ax, (22, 32), (36, 18.5), 'varie')
arrow(ax, (66, 32), (52, 18.5), 'varie')
save(fig, '34-069')
