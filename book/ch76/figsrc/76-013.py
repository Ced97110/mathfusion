import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def mat(ax, cx, cy, v, role='sujet', size='m'):
    """Matrice 2x2 : quatre nombres alignés, crochets."""
    a, b, c, d = [str(t) for t in v]
    w0, w1 = max(len(a), len(c)), max(len(b), len(d))
    p = lambda s, w: s.rjust(w, ' ')
    text(ax, cx, cy, f"{p(a, w0)}  {p(b, w1)}\n{p(c, w0)}  {p(d, w1)}", role, size)
    hw = ((w0 + w1) * 1.65 + 1.7) / 2 + 1.4; hh = 4.2
    for s in (-1, 1):
        line(ax, [(cx + s * (hw - 1.1), cy + hh), (cx + s * hw, cy + hh), (cx + s * hw, cy - hh), (cx + s * (hw - 1.1), cy - hh)], role, lw=0.8)

def arcarrow(ax, c, r, a0, a1, role='varie', n=24):
    """Arc fléché de centre c, rayon r, de l'angle a0 à a1 (degrés)."""
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts[:-2], role, lw=1.0); arrow(ax, pts[-4], pts[-1], role)
fig, ax = canvas(70)
u = 3.6
text(ax, 43, 64, 'aire ordinaire', 'autre', 's'); text(ax, 71, 64, r'$u\wedge v$', 'sujet', 'm')
for i, (a, b) in enumerate([('u', 'v'), ('v', 'u')]):
    y = 42 - i * 24
    text(ax, 12, y + 4, f'{a} puis {b}', 'fixe', 's')
    for ox, num, role, rot in [(34, '5', 'autre', None), (62, '+5' if i == 0 else '−5', 'sujet', i)]:
        poly(ax, [(ox + u * p[0], y + u * p[1]) for p in [(0, 0), (3, 1), (4, 3), (1, 2)]], role)
        text(ax, ox + 19, y + 5, num, role, 'm')
        if rot is not None:
            c = (ox, y)
            if rot == 0: arcarrow(ax, c, 5.5, 24, 58, 'varie')
            else: arcarrow(ax, c, 5.5, 58, 24, 'varie')
save(fig, '76-013')
