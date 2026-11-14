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
fig, ax = canvas(72)
text(ax, 44, 67, r'$x^2 + y^2 + z^2$', 'sujet', 'l')
x0, k = 28, 6.0
for y, v, vec in [(52, 1, '(1, 0, 0)'), (40, 2, '(1, 1, 0)'), (28, 9, '(1, 2, 2)')]:
    text(ax, x0 - 3, y + 3, vec, 'encre', 's', ha='right')
    box(ax, x0, y, v * k, 6, 'sujet')
    text(ax, x0 + v * k + 2, y + 3, str(v), 'sujet', 'm', ha='left')
line(ax, [(x0, 24), (x0, 60)], 'limite', lw=1.2, dash=True)
text(ax, x0, 20, 'jamais 0', 'limite', 's')
box(ax, 14, 2, 60, 13, 'autre', fill=False, dash=True, label='quel ensemble remplace\nles droites isotropes ?', size='s')
save(fig, '73-259')
