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
fig, ax = canvas(92)
box(ax, 14, 80, 60, 9, 'sujet', label=r'$M_2(\mathbb{R})$ : un seul ensemble', size='m')
ops = [('somme', r'$M+N$', 'case par case'), ('produit', r'$MN$', 'ligne par colonne'), ('par un nombre', r'$3M$', 'chaque case × 3')]
for i, (a, b, c) in enumerate(ops):
    cx = 15 + i * 29
    box(ax, cx - 13.5, 55, 27, 18, 'sujet', fill=False, lw=0.7)
    text(ax, cx, 69, a, 'sujet', 's'); text(ax, cx, 64, b, 'sujet', 'm'); text(ax, cx, 58.5, c, 'fixe', 's')
    arrow(ax, (44, 80), (cx, 73.6), 'sujet', lw=0.8)
# cas chiffré : M N puis x3
y = 45
mat(ax, 12, y, (1, 2, 0, 1), 'sujet'); text(ax, 21.5, y, r'$\times$', 'encre')
mat(ax, 31, y, (1, 0, 3, 1), 'autre'); text(ax, 40.5, y, '=', 'encre')
mat(ax, 50, y, (7, 2, 3, 1), 'fixe')
arrow(ax, (58, y), (65, y), 'varie'); text(ax, 61.5, y + 4.5, r'$\times 3$', 'varie', 's')
mat(ax, 76, y, (21, 6, 9, 3), 'resultat')
text(ax, 12, y - 8, r'$M$', 'sujet', 's'); text(ax, 31, y - 8, r'$N$', 'autre', 's'); text(ax, 50, y - 8, r'$MN$', 'fixe', 's')
text(ax, 76, y - 8, r'$3MN$', 'resultat', 's')
text(ax, 44, 27, 'Un cas chiffré : les trois opérations', 'encre', 's')
save(fig, '76-001')
