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
fig, ax = canvas(64)
ox, oy, u = 26, 12, 22
P = lambda x, y: (ox + (x + y * 0) * u, oy + y * u)
poly(ax, [P(0, 0), P(1, 0), P(1, 1), P(0, 1)], 'fixe', fill=False)
poly(ax, [P(0, 0), P(1, 0), P(2, 1), P(1, 1)], 'sujet')
arrow(ax, P(0, 0), P(0, 1), 'fixe', lw=1.4)
arrow(ax, P(0, 0), P(1, 1), 'varie', lw=1.4)
text(ax, ox - 2, oy + u / 2, 'longueur 1', 'fixe', 's', ha='right')
text(ax, ox + u, oy + u + 4, r'longueur $\sqrt{2}$ ≈ 1,41', 'varie', 's')
text(ax, ox + 1.55 * u, oy + 0.35 * u, 'aire 1', 'sujet', 'm')
text(ax, ox + 0.5 * u, oy + 0.18 * u, 'carré', 'fixe', 's')
text(ax, 44, 5, 'l’aire est gardée, la longueur non', 'limite', 's')
save(fig, '73-247')
