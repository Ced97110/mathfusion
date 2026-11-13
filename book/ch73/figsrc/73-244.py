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
fig, ax = canvas(88)
ys = [66, 46, 26, 6]
steps = [([['4', '1'], ['6', '2']], 'sujet', {}, '1. ad − bc = 4×2 − 1×6 = 2'),
         ([['2', '1'], ['6', '4']], 'sujet', {(0, 0): 'varie', (1, 1): 'varie'}, '2. échanger a = 4 et d = 2'),
         ([['2', '−1'], ['−6', '4']], 'sujet', {(0, 1): 'varie', (1, 0): 'varie'}, '3. changer le signe de b et de c'),
         ([['1', '−½'], ['−3', '2']], 'resultat', {(r, c): 'resultat' for r in range(2) for c in range(2)}, '4. diviser par 2')]
for y, (m, ro, hl, cap) in zip(ys, steps):
    cols = [[m[0][c], m[1][c]] for c in range(2)]
    mat(ax, 62, y, m, ro, hl=hl)
    text(ax, 2, y + 5.4, cap, 'encre', 's', ha='left')
for y in ys[:3]:
    arrow(ax, (78, y - 1.5), (78, y - 6.5), 'varie')
save(fig, '73-244')
