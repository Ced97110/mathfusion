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
u = 14; cy = 36
def panel(cx, end, title, rl, role):
    line(ax, [(cx - 1.25 * u, cy), (cx + 1.25 * u, cy)], 'fixe', dash=True)
    line(ax, [(cx - 0.9 * u, cy - 0.9 * u), (cx + 0.9 * u, cy + 0.9 * u)], 'fixe', dash=True)
    arrow(ax, (cx + u, cy), (cx, cy + end * u), role, curve=0.45 * end)
    dot(ax, cx + u, cy); dot(ax, cx, cy + end * u)
    text(ax, cx, 63, title, 'encre', 's')
    text(ax, cx + u, cy - 5, '(1, 0)', 'encre')
    text(ax, cx, cy + end * u + 5 * end, '(0, %s1)' % ('' if end > 0 else '−'), role)
    text(ax, cx, 10, rl, role, 'l', weight='bold')
panel(22, 1, 'horizontal, puis 45°', r'$R(90°)$', 'sujet')
panel(65, -1, '45°, puis horizontal', r'$R(-90°)$', 'varie')
text(ax, 44, 3, 'les deux matrices diffèrent', 'limite')
save(fig, '73-242')
