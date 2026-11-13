import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def pol(c, r, a): return (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
def arc(ax, c, r, a0, a1, role='varie', lw=0.9, n=30):
    line(ax, [pol(c, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw)
def sq(ax, p, d1, d2, s=2.2, role='fixe'):
    a = (p[0] + d1[0] * s, p[1] + d1[1] * s); b = (a[0] + d2[0] * s, a[1] + d2[1] * s); c = (p[0] + d2[0] * s, p[1] + d2[1] * s)
    line(ax, [a, b, c], role, lw=0.7)
fig, ax = canvas(52)
X0, S = 8, 52
h = 8
box(ax, X0, 30, 0.5 * S, h, 'sujet', label='0,5', size='s')
box(ax, X0 + 0.5 * S, 30, 0.866 * S, h, 'autre', label='0,866', size='s')
text(ax, X0 + 0.25 * S, 43, r'$\sin 30°$', 'sujet', 's'); text(ax, X0 + 0.5 * S + 0.433 * S, 43, r'$\sin 60°$', 'autre', 's')
text(ax, 44, 49, 'somme : 1,366', 'encre', 's')
box(ax, X0, 10, S, h, 'resultat', label=r'$\sin 90°=1$', size='s')
text(ax, X0 + S / 2, 4, r'$\sin(30°+60°)=\sin 90°$', 'resultat', 's')
line(ax, [(X0 + S, 8), (X0 + S, 41)], 'limite', dash=True, lw=0.9)
text(ax, 77, 21, '≠', 'limite', 'xl', weight='bold')
text(ax, 77, 14, '1,366', 'limite', 's')
save(fig, '26-121')
