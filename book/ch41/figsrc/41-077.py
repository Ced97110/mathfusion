import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, r'$u_2v_2$', 'sujet', 'xl')
text(ax, 44, 55.5, 'le produit des $y$', 'fixe', 's')
box(ax, 4, 40, 36, 9, 'sujet', label=r'$u_2=3$ : 2e composante de $u$', size='s')
box(ax, 48, 40, 36, 9, 'autre', label=r'$v_2=2$ : 2e composante de $v$', size='s')
# rectangle 3 colonnes (u2) x 2 lignes (v2)
c = 6.0
x0, y0 = 30, 3
for i in range(3):
    for j in range(2):
        poly(ax, [(x0 + i * c, y0 + j * c), (x0 + (i + 1) * c, y0 + j * c), (x0 + (i + 1) * c, y0 + (j + 1) * c), (x0 + i * c, y0 + (j + 1) * c)], 'resultat')
brace(ax, x0, x0 + 3 * c, y0 + 2 * c, 'sujet', label='3', down=False, depth=1.4)
line(ax, [(x0 + 3 * c + 2, y0), (x0 + 3 * c + 2, y0 + 2 * c)], 'autre', lw=0.8)
text(ax, x0 + 3 * c + 5, y0 + c, '2', 'autre', 'm')
text(ax, 72, y0 + c, r'$3\times2=6$' + '\ncases', 'resultat', 'm')
arrow(ax, (22, 39), (36, 29), 'fixe')
arrow(ax, (66, 39), (52, 29), 'fixe')
save(fig, '41-077')
