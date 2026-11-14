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
fig, ax = canvas(80)
ox, oy, u = 26, 10, 15
P = lambda x, y: (ox + x * u, oy + y * u)
arrow(ax, (ox - 1.2 * u, oy), (ox + 2.8 * u, oy), 'fixe', lw=0.7)
arrow(ax, (ox, oy), (ox, oy + 4.5 * u), 'fixe', lw=0.7)
poly(ax, [P(1, 0), P(2, 0), P(1, 1)], 'fixe')
poly(ax, [P(0, 3), P(0, 4), P(-1, 3)], 'sujet')
poly(ax, [P(2, 1), P(2, 2), P(1, 1)], 'varie')
arrow(ax, P(1, 0), P(0, 3), 'sujet', curve=-0.2)
arrow(ax, P(1, 0), P(2, 1), 'varie', curve=0.35)
for q in (P(1, 0), P(0, 3), P(2, 1)): dot(ax, *q)
text(ax, 44, 14, r'$F$', 'fixe', 'l')
text(ax, 36, 5, r'$P$ = (1, 0)', 'encre')
text(ax, 30, 66, r'$rt(F)$', 'sujet', 'l', ha='left')
text(ax, 18, 50, '(0, 3)', 'sujet')
text(ax, 66, 34, r'$tr(F)$', 'varie', 'l')
text(ax, 66, 22, '(2, 1)', 'varie')
save(fig, '73-241')
