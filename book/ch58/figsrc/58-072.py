import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, cx, cy, rows, roles, hw=7.5, dy=7.0):
    h = len(rows) * dy / 2
    for s in (-1, 1):
        x = cx + s * hw
        line(ax, [(x - s * 1.6, cy + h), (x, cy + h), (x, cy - h), (x - s * 1.6, cy - h)], 'fixe', lw=0.9)
    for i, r in enumerate(rows):
        text(ax, cx, cy + h - dy / 2 - i * dy, r, roles[i], 'm')

# gauche : BA est le tableau neutre, det = 1 ; droite : A a une ligne de zéros, donc det(BA) = det(B) x 0 = 0
fig, ax = canvas(76)
box(ax, 10, 64, 20, 9, 'sujet', label='BA', weight='bold')
box(ax, 58, 64, 20, 9, 'sujet', label='A', weight='bold')
text(ax, 20, 59.5, 'tableau neutre', 'resultat', 's')
text(ax, 68, 59.5, 'ligne de zéros', 'varie', 's')
mat(ax, 20, 46, ['1   0', '0   1'], ['resultat', 'resultat'])
mat(ax, 68, 46, ['2   1', '0   0'], ['encre', 'varie'])
text(ax, 20, 32, r'$\det(BA) = 1$', 'resultat', 'm')
text(ax, 68, 32, r'$\det(A) = 0$', 'varie', 'm')
text(ax, 68, 25.5, r'$\det(BA)=\det(B)\times 0 = 0$', 'varie', 's')
arrow(ax, (20, 28.5), (30, 13), 'fixe')
arrow(ax, (68, 22.5), (58, 13), 'fixe')
box(ax, 22, 3, 44, 9, 'limite', label='impossible : 1 = 0', size='m')
save(fig, '58-072')
