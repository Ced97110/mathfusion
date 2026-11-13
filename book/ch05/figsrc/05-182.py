import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 44, 46, 'entier = produit de premiers', 'encre', 'm', weight='bold')
xs = [30, 39, 48, 57]
box(ax, 25.8, 13.5, 26.4, 23, 'resultat', fill=False, dash=True)
for y, n, fs in ((32, '60', [2, 2, 3, 5]), (18, '84', [2, 2, 3, 7])):
    text(ax, 22, y, n + ' =', 'encre', 'm', ha='right')
    for x, p in zip(xs, fs):
        disc(ax, x, y, 3.2, 'sujet', label=str(p), size='m')
text(ax, 76, 32, r'$60\div12=5$', 'encre', 's')
text(ax, 76, 18, r'$84\div12=7$', 'encre', 's')
text(ax, 39, 8, r'$2\times2\times3=12$', 'resultat', 'm', weight='bold')
save(fig, '05-182')
