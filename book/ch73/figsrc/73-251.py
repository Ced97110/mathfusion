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
fig, ax = canvas(76)
u = 6.5
F = [(1, 0), (2, 0), (1, 1)]
panels = [  # (cx, cy, image, titre, axe de miroir)
    (2, 38, [(3, 0), (4, 0), (3, 1)], 'translation', False),
    (46, 38, [(0, 1), (0, 2), (-1, 1)], 'rotation', False),
    (2, 6, [(1, 0), (2, 0), (1, -1)], 'réflexion', True),
    (46, 6, [(3, 0), (4, 0), (3, -1)], 'symétrie glissée', True)]
for px, py, img, name, mir in panels:
    ox, oy = px + 8, py + 10
    P = lambda x, y: (ox + x * u, oy + y * u)
    arrow(ax, P(-1.2, 0), P(4.6, 0), 'fixe', lw=0.5)
    arrow(ax, P(0, -1.2), P(0, 2.4), 'fixe', lw=0.5)
    poly(ax, [P(*q) for q in F], 'fixe')
    poly(ax, [P(*q) for q in img], 'sujet')
    text(ax, px + 22, py + 29, name, 'sujet', 's')
save(fig, '73-251')
