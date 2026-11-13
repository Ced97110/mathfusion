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
fig, ax = canvas(86)
text(ax, 4, 79, r'$M$', 'sujet', 'l', ha='left'); mat(ax, 20, 79, (1, 1, 0, 1), 'sujet', 'm')
text(ax, 33, 79, r'$\times$', 'encre', 'l'); text(ax, 40, 79, r'$N$', 'autre', 'l', ha='left'); mat(ax, 56, 79, (2, 0, 0, 3), 'autre', 'm')
text(ax, 80, 79, r'$3$ : nombre', 'varie', 's')
rows = [(r'$3(MN)$', 'le 3 devant le produit'), (r'$(3M)N$', 'le 3 sur M'), (r'$M(3N)$', 'le 3 sur N')]
ys = [57, 37, 17]
for (e, t), y in zip(rows, ys):
    box(ax, 3, y - 7, 36, 14, 'sujet', label=e, size='l')
    text(ax, 21, y - 10.5, t, 'varie', 's')
    arrow(ax, (40, y), (59, 37 + (y - 37) * 0.35), 'sujet', lw=0.9)
mat(ax, 73, 37, (6, 9, 0, 9), 'resultat', 'l')
text(ax, 73, 49, 'même tableau', 'resultat', 's')
save(fig, '76-002')
