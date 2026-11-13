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
def tour(cx, widths, quots, qroles, labs):
    ys = [58, 36, 14]
    for y, w, lab in zip(ys, widths, labs):
        box(ax, cx - w / 2, y, w, 8, 'sujet', label=lab, size='s')
    for y, q, ro in zip((51, 29), quots, qroles):
        text(ax, cx, y, '÷ %d' % q, ro, 'm', weight='bold')
tour(22, [32, 16, 5], [2, 3], ['varie', 'autre'], ['6', '3', '1'])
tour(66, [32, 11, 5], [3, 2], ['autre', 'varie'], ['6', '2', '1'])
text(ax, 22, 68, 'découpage 1', 'encre', 's'); text(ax, 66, 68, 'découpage 2', 'encre', 's')
text(ax, 44, 4, 'mêmes pièces : 2 et 3', 'resultat', 'm')
save(fig, '73-257')
