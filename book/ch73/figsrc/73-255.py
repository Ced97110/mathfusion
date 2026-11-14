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
fig, ax = canvas(52)
mat(ax, 4, 20, [['1', '2'], ['3', '4']], 'sujet')
mat(ax, 34, 20, [['0', '1'], ['1', '0']], 'autre')
mat(ax, 64, 20, [['2', '1'], ['4', '3']], 'resultat')
text(ax, 29, 25.4, '×', 'encre', 'l'); text(ax, 59, 25.4, '=', 'encre', 'l')
text(ax, 12, 40, r'$A$', 'sujet', 'l'); text(ax, 42, 40, r'$B$', 'autre', 'l'); text(ax, 72, 40, r'$AB$', 'resultat', 'l')
text(ax, 12, 12, 'det = −2', 'sujet', 's'); text(ax, 42, 12, 'det = −1', 'autre', 's'); text(ax, 72, 12, 'det = 2', 'resultat', 's')
text(ax, 44, 4, '(−2) × (−1) = 2', 'encre', 'm')
save(fig, '73-255')
