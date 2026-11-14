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
per, w, h = 11, 7, 8
def frise(y, x0=2, n=5):
    for i in range(n):
        x = x0 + i * per
        poly(ax, [(x, y - h / 2), (x, y + h / 2), (x + w, y)], 'fixe')
    return lambda i: x0 + i * per
y1, y2 = 48, 22
f = frise(y1)
arrow(ax, (f(1) + 3, y1 + 6), (f(2) + 3, y1 + 6), 'varie', curve=-0.5)
text(ax, f(1) + 7, y1 + 12, 'décalage (2, 0)', 'varie', 's')
text(ax, 72, y1, r'$A = I$', 'resultat', 'l')
frise(y2)
line(ax, [(1, y2), (58, y2)], 'autre', dash=True)
arrow(ax, (f(2) + 3, y2 + h / 2 + 2), (f(2) + 3, y2 - h / 2 - 2), 'varie', both=True)
text(ax, f(2) + 12, y2 + 9, 'miroir', 'varie', 's')
text(ax, 72, y2, r'$A$ = miroir', 'autre', 'm')
text(ax, 44, 3, 'noyau de (A, x) ↦ A : les translations', 'resultat', 's')
save(fig, '73-252')
