import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 66, 'symétrie par rapport à l’axe réel', 'varie', 'm', weight='bold')
cols = [('produit scalaire', 'resultat', ('0', '0')), ('aire orientée', 'limite', ('1', '−1')), (r'$H$', 'limite', (r'$-i$', r'$i$'))]
x0, wc = 20, 22.5
for j, (h, r, (a, b)) in enumerate(cols):
    x = x0 + j*wc
    text(ax, x + wc/2, 56, h, r, 's', weight='bold')
    box(ax, x+1, 36, wc-2, 14, r, label=a, size='l')
    box(ax, x+1, 18, wc-2, 14, r, label=b, size='l')
text(ax, 10, 43, 'avant', 'fixe', 's'); text(ax, 10, 25, 'après', 'fixe', 's')
text(ax, 20 + 1.5*wc, 9, 'changé : $H$ n’est pas conservée', 'limite', 's')
save(fig, '75-171')
