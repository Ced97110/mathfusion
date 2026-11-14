import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 65, r'$u_1v_1$', 'sujet', 'xl')
text(ax, 44, 59.5, 'le produit des $x$', 'fixe', 's')
box(ax, 4, 44, 36, 9, 'sujet', label=r'$u_1=1$ : 1re composante de $u$', size='s')
box(ax, 48, 44, 36, 9, 'autre', label=r'$v_1=4$ : 1re composante de $v$', size='s')
# rectangle 1 colonne x 4 lignes : largeur u1, hauteur v1
c = 6.0
x0, y0 = 40, 3
for j in range(4):
    poly(ax, [(x0, y0 + j * c), (x0 + c, y0 + j * c), (x0 + c, y0 + (j + 1) * c), (x0, y0 + (j + 1) * c)], 'resultat')
brace(ax, x0, x0 + c, y0 + 4 * c, 'sujet', label='1', down=False, depth=1.4)
text(ax, x0 + c + 5, y0 + 2 * c, '4', 'autre', 'm')
line(ax, [(x0 + c + 2, y0), (x0 + c + 2, y0 + 4 * c)], 'autre', lw=0.8)
text(ax, 70, y0 + 2 * c, r'$1\times4=4$ cases', 'resultat', 'm')
arrow(ax, (22, 43), (36, 32), 'fixe')
arrow(ax, (66, 43), (51, 32), 'fixe')
save(fig, '41-076')
