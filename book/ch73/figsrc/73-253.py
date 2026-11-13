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
fig, ax = canvas(70)
box(ax, 2, 8, 38, 54, 'fixe', fill=False, dash=True)
text(ax, 21, 66, 'la méthode', 'encre', 's')
for i, s in enumerate(['1. transvections', '2. action sur les droites', '3. critère d’Iwasawa']):
    box(ax, 5, 40 - i * 16, 32, 12, 'sujet', label=s, size='s')
for y, ro, s in [(48, 'fixe', 'GL, O (ch. 73)'), (32, 'sujet', 'symplectique (ch. 75)'), (16, 'sujet', 'unitaire (ch. 75)')]:
    box(ax, 56, y, 30, 11, ro, label=s, size='s')
    arrow(ax, (40, 35), (55.5, y + 5.5), ro if ro != 'fixe' else 'fixe', lw=0.9)
for i in range(2): arrow(ax, (21, 40 - i * 16), (21, 40 - i * 16 - 4), 'sujet')
text(ax, 44, 3, r'même comptage sur $\mathbb{F}_3$ : 48 = 8 × 6', 'resultat', 's')
save(fig, '73-253')
