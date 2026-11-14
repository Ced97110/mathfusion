import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def dot(ax, x, y, r=1.0, role='encre'):
    ax.add_patch(Circle((x, y), r, fc=COL[role], ec=COL[role], zorder=6))

def mat(ax, x, y, rows, role='sujet', h=5.4, w=8.0, hl=None, size='m'):
    """Matrice : coin bas-gauche (x, y), colonnes écrites en blocs ; hl = {(ligne, col): rôle} pour le fond."""
    n, m = len(rows), len(rows[0]); hl = hl or {}
    for (r, c), ro in hl.items():
        ax.add_patch(Rectangle((x + c * w, y + (n - 1 - r) * h), w, h, fc=FILL[ro], ec='none', zorder=1))
    for sx, dx in ((x - 1.0, 1.2), (x + m * w + 1.0, -1.2)):
        line(ax, [(sx + dx, y - 0.4), (sx, y - 0.4), (sx, y + n * h + 0.4), (sx + dx, y + n * h + 0.4)], role, lw=0.9)
    fig = ax.figure; rd = fig.canvas.get_renderer(); fs = SIZE[size]
    t1 = ax.text(0, 0, '0', fontsize=fs); t2 = ax.text(0, 0, '0\n0', fontsize=fs)
    pitch = t2.get_window_extent(rd).height - t1.get_window_extent(rd).height
    t1.remove(); t2.remove()
    ls = 1.2 * (h * fig.dpi / 25.4) / pitch
    for c in range(m):
        t = text(ax, x + c * w + w / 2, y + n * h / 2, '\n'.join(rows[r][c] for r in range(n)), role, size)
        t.set_linespacing(ls)
    return x + m * w
fig, ax = canvas(56)
u = 9; oy = 20
def para(ox, b, role):
    P = lambda x, y: (ox + (x + b * y) * u, oy + y * u)
    poly(ax, [P(0, 0), P(1, 0), P(1, 1), P(0, 1)], role)
    return P
poly(ax, [(4, oy), (4 + u, oy), (4 + u, oy + u), (4, oy + u)], 'fixe', fill=False)
para(4, 0.01, 'sujet')
text(ax, 4 + u / 2, oy - 5, 'b = 0,01', 'sujet', 's')
text(ax, 14, oy + u + 9, 'presque', 'sujet', 's'); text(ax, 14, oy + u + 5, 'égal au carré', 'sujet', 's')
poly(ax, [(28, oy), (28 + u, oy), (28 + u, oy + u), (28, oy + u)], 'fixe', fill=False)
para(28, 5, 'varie')
text(ax, 28 + u / 2, oy - 5, 'b = 5', 'varie', 's')
text(ax, 58, oy + u + 8, 'très loin du carré', 'varie', 's')
text(ax, 44, 5, 'carré gris : l’identité', 'fixe', 's')
save(fig, '73-256')
