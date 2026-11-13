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
cl, cr = 16, 62
for y, w, lab in [(66, 28, r'6 : $GL_2(\mathbb{F}_2)$'), (50, 14, '3'), (34, 5, '1')]:
    box(ax, cl - w / 2, y, w, 6, 'sujet', label=lab, size='s')
text(ax, cl, 58, '÷ 2 : commutatif', 'resultat', 's')
text(ax, cl, 42, '÷ 3 : commutatif', 'resultat', 's')
text(ax, cl, 22, 'résoluble', 'resultat', 'm', weight='bold')
for y, lab in [(66, r'$GL_n$'), (50, r'$SL_n$'), (34, 'C'), (18, r'$\{1\}$')]:
    box(ax, cr - 8, y, 16, 6, 'autre', label=lab, size='s')
text(ax, cr, 58, 'commutatif', 'resultat', 's')
text(ax, cr, 42, 'simple, non commutatif', 'limite', 's')
text(ax, cr, 26, 'commutatif', 'resultat', 's')
text(ax, cr, 8, 'pas résoluble', 'limite', 'm', weight='bold')
save(fig, '73-254')
