import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 56, r'$|Z(G)|=12-3-3=6$', 'resultat', 'l')
x = 5; w = 6.4
for n, role, lab in ((6, 'resultat', 'centre : 6'), (3, 'varie', 'classe : 3'), (3, 'varie', 'classe : 3')):
    x0 = x
    for i in range(n):
        box(ax, x, 30, w, 8, role, r=0.6); x += w
    brace(ax, x0, x, 30, role, label=lab)
    x += 1.6
text(ax, 44, 44, '12 éléments en trois parts', 'encre', 's')
text(ax, 44, 8, '12, 3 et 3 : multiples de 3', 'varie', 's')
text(ax, 44, 2.8, '3 divise donc 6', 'resultat', 's')
save(fig, '50-137')
