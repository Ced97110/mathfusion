import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
c = 9
text(ax, 44, 57, r'racine $r=1$ sur la diagonale', 'encre', 'm')
# ligne A : exposant 1
box(ax, 3, 36, 30, 10, 'sujet', label=r'$(\lambda-1)^1$')
arrow(ax, (34.5, 41), (49.5, 41), 'sujet')
box(ax, 52, 36.5, c, c, 'sujet', label='1', size='l')
text(ax, 77, 41, r'taille $e=1$', 'sujet', 's')
# ligne B : exposant 2
box(ax, 3, 11, 30, 10, 'varie', label=r'$(\lambda-1)^2$')
arrow(ax, (34.5, 16), (49.5, 16), 'varie')
vals = [['1', '1'], ['0', '1']]
for i in range(2):
    for j in range(2):
        box(ax, 52 + j * c, 7 + (1 - i) * c, c, c, 'varie', label=vals[i][j], size='l')
text(ax, 77, 16, r'taille $e=2$', 'varie', 's')
save(fig, '60-214')
