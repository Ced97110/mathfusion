import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
vals = [[2, 1], [1, 1]]; c = 12; ox, oy = 12, 8
for i in range(2):
    for j in range(2):
        box(ax, ox + j * c, oy + (1 - i) * c, c, c, 'sujet', label=str(vals[i][j]), size='l')
brace(ax, ox, ox + 2 * c, oy + 2 * c + 1, 'fixe', label=r'$n$ colonnes', down=False)
line(ax, [(ox - 2, oy), (ox - 2, oy + 2 * c)], 'fixe')
text(ax, ox - 6, oy + c, r'$n$ lignes', 'fixe', 's', rot=90)
arrow(ax, (ox + 2 * c + 3, oy + c), (54, oy + c), 'varie')
box(ax, 55, oy + c - 7, 28, 14, 'resultat', label=r'$GL_n$', size='l')
text(ax, 69, oy + c - 11, 'tous les tableaux', 'resultat', 's')
text(ax, 69, oy + c - 15, 'inversibles', 'resultat', 's')
text(ax, 69, oy + c + 11, r'$n=2$', 'fixe', 's')
save(fig, '75-059')
