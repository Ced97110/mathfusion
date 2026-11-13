import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
def panel(ox, oy, role_res, t, res, verdict):
    arrow(ax, (ox - 17, oy), (ox + 17, oy), 'fixe', lw=0.6); arrow(ax, (ox, oy - 13), (ox, oy + 28), 'fixe', lw=0.6)
    u = 8
    arrow(ax, (ox, oy), (ox + u, oy + 2 * u), 'sujet', lw=1.3)
    arrow(ax, (ox, oy), (ox + 2 * u, oy - u), 'autre', lw=1.3)
    text(ax, ox + u + 3, oy + 2 * u, r'$x$', 'sujet', 'm')
    text(ax, ox + 2 * u + 3, oy - u, r'$y$', 'autre', 'm')
    text(ax, ox, 76, t, 'encre', 's')
    text(ax, ox, 17, res, role_res, 's')
    text(ax, ox, 8, verdict, role_res, 'm')
panel(22, 38, 'resultat', 'produit scalaire', r'$1\times2+2\times(-1)=0$', r'$x\perp y$')
panel(66, 38, 'limite', 'première coordonnée', r'$1\times2=2\neq0$', 'pas orthogonaux pour $B$')
save(fig, '71-071')
