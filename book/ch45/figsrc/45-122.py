import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def row(ax, x, y, n, w, gap, role, label=None, h=None, dash=False):
    xs = []
    for i in range(n):
        xi = x + i * (w + gap); box(ax, xi, y, w, h or w, role, label=label, dash=dash); xs.append(xi + w / 2)
    return xs

fig, ax = canvas(56)
w = 14; ys = 26
def col(cx, head, role):
    text(ax, cx, 46, head, role, 'l')
col(16, '$a^{1}$', 'sujet'); col(44, '$a^{0}$', 'resultat'); col(72, '$0$', 'limite')
box(ax, 9, ys, w, w, 'sujet', label='$a$'); text(ax, 16, ys - 4, 'un facteur', 'sujet', 's')
box(ax, 37, ys, w, w, 'resultat', dash=True); text(ax, 44, ys + 7, '$1$', 'resultat', 'l'); text(ax, 44, ys - 4, 'zéro facteur', 'resultat', 's')
box(ax, 65, ys, w, w, 'limite'); line(ax, [(65, ys), (79, ys + w)], 'limite', lw=1.2); line(ax, [(65, ys + w), (79, ys)], 'limite', lw=1.2)
text(ax, 72, ys - 4, 'pas le nombre 0', 'limite', 's')
text(ax, 44, 10, '$a^{0}$ est le neutre $1$', 'resultat', 'm')
save(fig, '45-122')
