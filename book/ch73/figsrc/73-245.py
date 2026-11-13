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
fig, ax = canvas(66)
mat(ax, 6, 22, [['2', '1'], ['5', '3']], 'sujet', hl={(0, 0): 'varie', (1, 1): 'varie', (0, 1): 'fixe', (1, 0): 'fixe'})
mat(ax, 58, 22, [['3', '−1'], ['−5', '2']], 'resultat', hl={(0, 0): 'varie', (1, 1): 'varie', (0, 1): 'resultat', (1, 0): 'resultat'})
arrow(ax, (28, 27), (54, 27), 'varie')
text(ax, 41, 33, 'échanger 2 et 3', 'varie', 's')
text(ax, 41, 21, 'signes de 1 et 5', 'varie', 's')
text(ax, 15, 12, '6 − 5 = 1', 'sujet', 'm')
text(ax, 67, 12, 'sans division', 'resultat', 'm')
text(ax, 41, 12, r'$\div\,1$', 'fixe', 'l'); line(ax, [(36.5, 12), (45.5, 12)], 'encre', lw=1.0)
text(ax, 41, 5, 'diviser par 1 : rien à faire', 'encre', 's')
text(ax, 41, 54, 'échanger la diagonale, changer deux\nsignes, diviser par le déterminant', 'encre', 's')
text(ax, 15, 39, r'$A$', 'sujet', 'l'); text(ax, 67, 39, r'$A^{-1}$', 'resultat', 'l')
save(fig, '73-245')
