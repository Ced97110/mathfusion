import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
def graphe(ox, role, la, lb):
    oy = 14; L = 30
    arrow(ax, (ox, oy), (ox + L + 5, oy), 'fixe', lw=0.8)
    arrow(ax, (ox, oy), (ox, oy + 36), 'fixe', lw=0.8)
    arrow(ax, (ox, oy), (ox + L, oy + L * 0.6), role, lw=1.3)
    arrow(ax, (ox, oy), (ox + L * 0.5, oy + L * 0.6), 'varie', lw=1.3)
    text(ax, ox + L, oy + L * 0.6 - 4, la, role, 's', ha='right')
    text(ax, ox + L * 0.5 + 1, oy + L * 0.6 + 3, lb, 'varie', 's', ha='left')
box(ax, 3, 55, 39, 9, 'sujet', label=r'$y$ fixé : linéaire en $x$', size='s')
box(ax, 46, 55, 39, 9, 'autre', label=r'$x$ fixé : linéaire en $y$', size='s')
graphe(6, 'sujet', r'$1\ \mathrm{€} \times x_1$', r'$2\ \mathrm{€} \times x_2$')
graphe(50, 'autre', r'$y_1$', r'$y_2$')
text(ax, 21, 5, r'$B = x_1 + 2\,x_2$', 'resultat', 's')
text(ax, 67, 5, 'même propriété', 'fixe', 's')
save(fig, '71-050')
