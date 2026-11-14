import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
def row(y, boxes, ys):
    pass
xs = [20 + 14 * k + 6 * j for k in range(3) for j in range(2)]
def discs(y, role):
    for x in xs: disc(ax, x, y, 2.3, role)
# p = 3 : un seul bloc de 6
y1, y2 = 46, 20
text(ax, 9, y1, r'$p = 3$', 'encre', 'm'); text(ax, 9, y2, r'$p = 2$', 'encre', 'm')
box(ax, 17.5, y1 - 5.5, 39, 11, 'sujet'); discs(y1, 'sujet')
text(ax, 37, y1 - 9.5, '1 bloc', 'sujet', 's')
for k in range(3):
    r = 'sujet' if k == 0 else 'fixe'
    box(ax, 17.5 + 14 * k, y2 - 5.5, 11.6, 11, r)
    for j in range(2): disc(ax, 20 + 14 * k + 6 * j, y2, 2.3, r)
text(ax, 37, y2 - 9.5, '3 blocs', 'fixe', 's')
text(ax, 44, 59, 'indice = nombre de blocs', 'encre', 's')
text(ax, 72, y1 + 5, r'$N(P) = G$', 'resultat', 's'); text(ax, 72, y1, r'$n_3 = 1$', 'resultat', 's'); text(ax, 72, y1 - 5, 'normal', 'resultat', 's', weight='bold')
text(ax, 72, y2 + 5, r'$N(P) \neq G$', 'limite', 's'); text(ax, 72, y2, r'$n_2 = 3$', 'limite', 's'); text(ax, 72, y2 - 5, 'pas normal', 'limite', 's', weight='bold')
save(fig, '50-081')
