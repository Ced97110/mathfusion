import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pol(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def arc(ax, c, r, a0, a1, role='varie', lw=0.9, n=30):
    line(ax, [pol(c, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw)
def sq(ax, p, d1, d2, s=2.2, role='fixe'):
    a = (p[0] + d1[0] * s, p[1] + d1[1] * s); b = (a[0] + d2[0] * s, a[1] + d2[1] * s); c = (p[0] + d2[0] * s, p[1] + d2[1] * s)
    line(ax, [a, b, c], role, lw=0.7)
fig, ax = canvas(82)
A = (8, 48); u = 3.0
B = pol(A, 10 * u, 60); Hf = (B[0], 48)
line(ax, [(4, 48), (46, 48)], 'fixe'); line(ax, [A, B], 'sujet', lw=1.6); line(ax, [B, Hf], 'fixe', dash=True)
line(ax, [A, Hf], 'varie', lw=2.4)
arrow(ax, (A[0], 46.5), (A[0] + 1 * u, 46.5), 'autre', lw=1.8)
arc(ax, A, 8, 0, 60, 'fixe'); text(ax, 21, 51.5, '60°', 'fixe', 's')
text(ax, 11, 65, '10 cm', 'sujet', 's', rot=60)
text(ax, 17, 43.5, 'flèche 1', 'autre', 's')
text(ax, 62, 66, r'$10\times 1\times 0{,}5=5$', 'varie', 's')
text(ax, 62, 59, 'projection : 5 cm', 'varie', 's')
f1 = 6; y1 = 30; x0 = 8
arrow(ax, (x0, y1), (x0 + 3 * f1, y1), 'autre', lw=1.6); arrow(ax, (x0 + 3 * f1, y1), (x0 + 5 * f1, y1), 'varie', lw=1.6)
text(ax, x0 + 1.5 * f1, y1 - 3.5, '3', 'autre', 's'); text(ax, x0 + 4 * f1, y1 - 3.5, '2', 'varie', 's')
brace(ax, x0, x0 + 5 * f1, y1 + 3, 'fixe', '5', down=False)
k = 1.2
box(ax, x0, 8, 15 * k, 8, 'autre', label='15', size='s'); box(ax, x0 + 15 * k, 8, 10 * k, 8, 'varie', label='10', size='s')
for xx in (x0, x0 + 3 * f1, x0 + 5 * f1): line(ax, [(xx, y1 - 6), (xx, 17)], 'fixe', dash=True, lw=0.6)
text(ax, 42, 15, 'projections', 'fixe', 's', ha='left'); text(ax, 42, 9.5, '15 + 10 = 25', 'resultat', 'm', ha='left', weight='bold')
save(fig, '26-128')
