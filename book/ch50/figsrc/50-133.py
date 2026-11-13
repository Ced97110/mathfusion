import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 56, r'$|G|=2+2+2+2=8$', 'resultat', 'l')
x = 8; cw = 9; gap = 2
labs = [(r'$|Z(G)|=2$', 'fixe'), (r'$[G:C(x_1)]=2$', 'varie'), (r'$[G:C(x_2)]=2$', 'varie'), (r'$[G:C(x_3)]=2$', 'varie')]
for lab, role in labs:
    x0 = x
    for i in range(2):
        box(ax, x, 28, cw, 9, role); x += cw
    brace(ax, x0, x, 28, role, label=lab)
    x += gap
text(ax, 44, 44, 'centre + trois classes de 2', 'encre', 's')
save(fig, '50-133')
