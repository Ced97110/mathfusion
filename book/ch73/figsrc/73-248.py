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
fig, ax = canvas(74)
ox, oy, u = 10, 8, 7
P = lambda x, y: (ox + x * u, oy + y * u)
arrow(ax, P(0, 0), P(7, 0), 'fixe', lw=0.6); arrow(ax, P(0, 0), P(0, 9.2), 'fixe', lw=0.6)
arrow(ax, P(0, 0), P(3, 4), 'fixe', lw=1.2)
arrow(ax, P(0, 0), P(6, 8), 'varie', lw=1.2)
arrow(ax, P(0, 0), P(2, 0), 'sujet', lw=1.6); arrow(ax, P(0, 0), P(0, 2), 'sujet', lw=1.6)
line(ax, [P(0.6, 0), P(0.6, 0.6), P(0, 0.6)], 'resultat', lw=0.8)
text(ax, ox + 2 * u + 3, oy - 3.5, '(2, 0)', 'sujet', 's')
text(ax, ox - 1, oy + 2 * u + 2, '(0, 2)', 'sujet', 's', ha='left')
text(ax, 36, 33, '(3, 4) : longueur 5', 'fixe', 's', ha='left')
text(ax, 56, 62, '(6, 8) : longueur 10', 'varie', 's', ha='left')
text(ax, 36, 21, 'colonnes perpendiculaires', 'resultat', 's', ha='left')
text(ax, 36, 15, 'mais de longueur 2, pas 1', 'limite', 's', ha='left')
save(fig, '73-248')
