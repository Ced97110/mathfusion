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
fig, ax = canvas(62)
f = numberline(ax, 12, 72, 30, -2, 2, arrow_right=False)
for v, ro in ((1, 'resultat'), (-1, 'resultat'), (2, 'limite')): disc(ax, f(v), 30, 1.8, ro)
arrow(ax, (f(1), 34), (f(-1), 34), 'varie', curve=0.5)
text(ax, f(0), 44, r'miroir $x \mapsto -x$', 'varie', 's')
text(ax, f(0), 52, r'$O(1)$ = {1, −1}', 'resultat', 'l')
text(ax, f(1), 16, '1 × 1 = 1', 'resultat', 's')
text(ax, f(-1), 16, '(−1) × (−1) = 1', 'resultat', 's')
text(ax, f(2) - 2, 8, '2 × 2 = 4', 'limite', 's')
save(fig, '73-249')
