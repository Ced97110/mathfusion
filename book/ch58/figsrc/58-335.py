import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
# B de colonnes (1,1),(0,1), det 1 ; A de colonnes (2,1),(1,3), det 5 ; BA de colonnes (2,3),(1,4), det 5
def mat(x, y, cols, role, c=9.0):
    for j in range(2):
        for i in range(2):
            box(ax, x + c * j, y + c * (1 - i), c, c, role, label=str(cols[j][i]), size='m')
y = 24
mat(4, y, [(1, 1), (0, 1)], 'autre')
mat(31, y, [(2, 1), (1, 3)], 'sujet')
mat(62, y, [(2, 3), (1, 4)], 'resultat')
text(ax, 13, y + 22, r'$B$', 'autre', 'l')
text(ax, 40, y + 22, r'$A$', 'sujet', 'l')
text(ax, 71, y + 22, r'$BA$', 'resultat', 'l')
text(ax, 26.5, y + 9, r'$\times$', 'encre', 'l')
text(ax, 57, y + 9, '=', 'encre', 'l')
text(ax, 13, y - 5, r'$\det B = 1$', 'autre', 's')
text(ax, 40, y - 5, r'$\det A = 5$', 'sujet', 's')
text(ax, 71, y - 5, r'$\det(BA) = 5$', 'resultat', 's')
text(ax, 44, 7, r'$5 = 1 \times 5$', 'resultat', 'l', weight='bold')
save(fig, '58-335')
