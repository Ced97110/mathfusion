import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
cs, x0, y0 = 11, 6, 14
for i in range(4):
    for j in range(3):
        box(ax, x0 + i * cs, y0 + j * cs, cs, cs, 'resultat' if (i < 3 and j < 2) else 'fixe', r=0.2)
brace(ax, x0, x0 + 3 * cs, y0, 'resultat', label=r'$a=3$ colonnes prises')
brace(ax, x0, x0 + 4 * cs, y0 + 3 * cs, 'sujet', label=r'$b=4$ colonnes', down=False)
text(ax, 70, 52, r'lignes : $c=2$ sur $d=3$', 'encre', 's')
text(ax, 70, 40, r'$b\times d=4\times3=12$', 'sujet', 'm')
text(ax, 70, 30, r'$a\times c=3\times2=6$', 'resultat', 'm')
text(ax, 70, 18, r'aire $=\frac{6}{12}$', 'encre', 'l')
save(fig, '06-052')
