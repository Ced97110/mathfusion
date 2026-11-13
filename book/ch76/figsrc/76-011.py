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
fig, ax = canvas(44)
u = 6.5
P = lambda ox, oy, x, y: (ox + u * x, oy + u * y)
for k, (ox, first, second, sign, role) in enumerate([(5, 'u', 'v', '+5', 'resultat'), (49, 'v', 'u', '−5', 'limite')]):
    oy = 14
    for i in range(1, 4): line(ax, [P(ox, oy, 0, i), P(ox, oy, 4, i)], 'fixe', lw=0.3)
    for i in range(1, 5): line(ax, [P(ox, oy, i, 0), P(ox, oy, i, 3)], 'fixe', lw=0.3)
    poly(ax, [P(ox, oy, *p) for p in [(0, 0), (3, 1), (4, 3), (1, 2)]], 'sujet')
    arrow(ax, P(ox, oy, 0, 0), P(ox, oy, 3, 1), 'sujet', lw=1.2); arrow(ax, P(ox, oy, 0, 0), P(ox, oy, 1, 2), 'sujet', lw=1.2)
    text(ax, P(ox, oy, 3.5, 0.6)[0], P(ox, oy, 3.5, 0.6)[1], 'u', 'sujet', 'm')
    text(ax, P(ox, oy, 0.2, 2.5)[0], P(ox, oy, 0.2, 2.5)[1], 'v', 'sujet', 'm')
    c = P(ox, oy, 0, 0)
    if k == 0: arcarrow(ax, c, 8, 24, 58, 'varie')
    else: arcarrow(ax, c, 8, 58, 24, 'varie')
    text(ax, ox + 14, oy - 8, f'{first} → {second} : {sign}', role, 'm')
    text(ax, ox + 14, oy + 3 * u + 4, '5 carreaux', 'sujet', 's')
save(fig, '76-011')
