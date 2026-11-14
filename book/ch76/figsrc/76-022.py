import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
M = '1  2\n0  1'; D = '3  0\n0  3'; R = '3  6\n0  3'
def row(y, title, a, ra, b, rb):
    text(ax, 4, y + 17, title, 'varie', 'm', ha='left', weight='bold')
    if a is None: text(ax, 12, y + 6, '3', 'varie', 'l')
    else: box(ax, 3, y, 18, 12, ra, label=a)
    box(ax, 27, y, 18, 12, rb, label=b)
    arrow(ax, (49, y + 6), (60, y + 6), 'resultat'); box(ax, 63, y, 22, 12, 'resultat', label=R)
row(50, r'$3 \times M$', None, 'fixe', M, 'fixe')
row(26, r'$M \times D$ (à droite)', M, 'fixe', D, 'sujet')
row(2, r'$D \times M$ (à gauche)', D, 'sujet', M, 'fixe')
save(fig, '76-022')
