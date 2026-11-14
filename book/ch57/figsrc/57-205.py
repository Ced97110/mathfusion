import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, r'$\mathbb{Z}$ agit sur $x=(0\,;\,0)$', 'encre', 'm')
text(ax, 44, 51, r'$n\cdot(0\,;\,0)=(0\,;\,0)$ pour tout $n$', 'varie', 's')
# côté gauche : Rx
box(ax, 4, 14, 32, 30, 'sujet')
disc(ax, 20, 32, 3.5, 'sujet', label='0', size='s')
text(ax, 20, 22, r'$\mathbb{Z}x=\{(0\,;\,0)\}$', 'sujet', 's')
text(ax, 20, 17.5, '1 élément', 'sujet', 's')
text(ax, 44, 29, '≅', 'encre', 'xl', weight='bold')
# côté droit : R / ann x
box(ax, 52, 14, 32, 30, 'autre')
disc(ax, 68, 32, 3.5, 'autre', label='0', size='s')
text(ax, 68, 22, r'$\mathbb{Z}/\mathbb{Z}=0$', 'autre', 's')
text(ax, 68, 17.5, '1 classe', 'autre', 's')
text(ax, 44, 6, r'ann $x=\mathbb{Z}$ : tous les $n$', 'fixe', 's')
save(fig, '57-205')
