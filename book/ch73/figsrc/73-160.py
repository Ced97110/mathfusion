import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
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
fig, ax = canvas(72)
box(ax, 3, 14, 82, 54, 'fixe'); text(ax, 44, 63, 'matrices de déterminant 1', 'fixe', 's')
box(ax, 7, 40, 74, 18, 'varie'); text(ax, 44, 53, 'transvections : une pour chaque pente', 'varie', 's')
text(ax, 44, 45, r'$T(1),\ T(2),\ T(6),\ \dots$', 'varie', 'm')
mat(ax, 8, 21, [['1', '1'], ['0', '1']], 'varie')
text(ax, 28, 26.4, r'$\times$', 'varie', 'l')
mat(ax, 34, 21, [['1', '0'], ['1', '1']], 'varie')
text(ax, 55, 26.4, '=', 'resultat', 'l')
mat(ax, 62, 21, [['2', '1'], ['1', '1']], 'autre')
text(ax, 44, 17, 'un produit de transvections', 'autre', 's')
text(ax, 44, 8, 'les transvections engendrent tout :', 'resultat', 's')
text(ax, 44, 3.5, 'il suffit de les traiter', 'resultat', 's', weight='bold')
save(fig, '73-160')
