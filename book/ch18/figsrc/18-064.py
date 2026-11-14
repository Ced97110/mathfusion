import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
y = 26
for x, q in ((8, '4'), (48, '5')):
    text(ax, x, y, '(', 'encre', 'xl')
    box(ax, x + 3, y - 4.5, 9, 9, 'sujet', label=r'$x$', r=0.5, size='l')
    text(ax, x + 18, y, '+ ' + q, 'fixe', 'm')
    text(ax, x + 25, y, ')', 'encre', 'xl')
    text(ax, x + 7.5, y + 9, '1er terme', 'sujet', 's')
    arrow(ax, (x + 7.5, y - 5), (28 + (x - 8) / 40 * 24 + 4, 16.5), 'sujet')
text(ax, 38, y, '×', 'encre', 'l')
box(ax, 20, 6, 40, 10, 'resultat', label=r'$x\times x=x^2$', size='l', r=0.6, weight='bold')
text(ax, 74, 11, 'ni 4 ni 5', 'fixe', 's')
text(ax, 44, 43, 'produit des premiers termes', 'encre', 'm', weight='bold')
save(fig, '18-064')
