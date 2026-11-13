import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
u = 5.0
R = lambda x, y, w, h, r, lab=None, d=False: box(ax, x, y, w, h, r, label=lab, r=0.3, dash=d, fill=not d)
text(ax, 44, 56, r'$(a+b)(a-b)$', 'encre', 'l', weight='bold')
# somme : barre a + b = 5 + 3
x0, y0 = 4, 30
R(x0, y0, 5 * u, 7, 'sujet', '5'); R(x0 + 5 * u, y0, 3 * u, 7, 'varie', '3')
text(ax, x0 + 4 * u, y0 + 11, 'somme : 5 + 3 = 8', 'sujet', 's')
# différence : 5 - 3 = 2
x1 = 52
R(x1, y0, 2 * u, 7, 'autre', '2'); R(x1 + 2 * u, y0, 3 * u, 7, 'varie', '3', d=True)
text(ax, x1 + 2.5 * u, y0 + 11, 'différence : 5 − 3 = 2', 'autre', 's')
text(ax, x1 + 3.5 * u, y0 - 3.5, 'on retire 3', 'varie', 's')
text(ax, 44, 20, '×', 'encre', 'l')
# produit : rectangle 8 par 2
R(4, 3, 8 * u * 0.75, 2 * u * 0.75 + 0.01, 'resultat') 
text(ax, 4 + 4 * u * 0.75, 3 + u * 0.75, '8 × 2 = 16', 'resultat', 'l', weight='bold')
text(ax, 56, 9, 'et 25 − 9 = 16', 'resultat', 'm')
save(fig, '18-050')
