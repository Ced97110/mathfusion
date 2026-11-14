import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def wv(ax, fn, xa, xb, yc, amp, role, t0, t1, n=240, lw=1.2, dash=False):
    pts = [(xa + (xb - xa) * i / n, yc + amp * fn(t0 + (t1 - t0) * i / n)) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
pi = math.pi
def arc(ax, c, r, a0, a1, role, n=60, dash=False, lw=1.0):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)

fig, ax = canvas(58)
u = 2.4
text(ax, 44, 54, r'amplitude de $3\sin x+4\sin(x+\beta)$', 'encre', 's')
# beta = 0
ox, oy = 8, 40
arrow(ax, (ox, oy), (ox + 3 * u, oy), 'sujet', lw=1.3); arrow(ax, (ox + 3 * u, oy), (ox + 7 * u, oy), 'autre', lw=1.3)
arrow(ax, (ox, oy - 7), (ox + 7 * u, oy - 7), 'resultat', lw=1.5)
text(ax, ox + 1.5 * u, oy + 3.5, '3', 'sujet', 's'); text(ax, ox + 5 * u, oy + 3.5, '4', 'autre', 's'); text(ax, ox + 3.5 * u, oy - 11, '7', 'resultat', 's')
text(ax, ox + 3.5 * u, 18, r'$\beta=0^\circ$', 'fixe', 's')
# beta = 90
ox, oy = 40, 30
arrow(ax, (ox, oy), (ox + 3 * u, oy), 'sujet', lw=1.3); arrow(ax, (ox + 3 * u, oy), (ox + 3 * u, oy + 4 * u), 'autre', lw=1.3)
arrow(ax, (ox, oy), (ox + 3 * u, oy + 4 * u), 'resultat', lw=1.5)
text(ax, ox + 1.5 * u, oy - 3.5, '3', 'sujet', 's'); text(ax, ox + 3 * u + 3, oy + 2 * u, '4', 'autre', 's'); text(ax, ox - 1.5, oy + 2 * u + 2, '5', 'resultat', 's')
text(ax, ox + 3.5 * u, 18, r'$\beta=90^\circ$', 'fixe', 's')
# beta = 180
ox, oy = 70, 40
arrow(ax, (ox, oy), (ox + 3 * u, oy), 'sujet', lw=1.3); line(ax, [(ox + 3 * u, oy), (ox + 3 * u, oy - 3)], 'fixe', dash=True, lw=0.6)
arrow(ax, (ox + 3 * u, oy - 3), (ox - u, oy - 3), 'autre', lw=1.3)
arrow(ax, (ox, oy - 12), (ox - u, oy - 12), 'resultat', lw=1.5)
text(ax, ox + 1.5 * u, oy + 3.5, '3', 'sujet', 's'); text(ax, ox + 1.5 * u, oy - 7, '4', 'autre', 's'); text(ax, ox - 0.5 * u, oy - 16, '1', 'resultat', 's')
text(ax, ox + 1.5 * u, 18, r'$\beta=180^\circ$', 'fixe', 's')
text(ax, 44, 8, 'la somme est la flèche qui ferme', 'resultat', 's')
save(fig, '35-114')
