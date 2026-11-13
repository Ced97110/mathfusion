import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def pts(x, n, yc, sp):
    return [(x, yc + (n - 1) / 2 * sp - i * sp) for i in range(n)]
def link(ax, p, q, role, r=3.2, curve=0.0, both=False, lw=1.0):
    dx, dy = q[0] - p[0], q[1] - p[1]; d = math.hypot(dx, dy); ux, uy = dx / d, dy / d
    arrow(ax, (p[0] + ux * (r + 0.3), p[1] + uy * (r + 0.3)), (q[0] - ux * (r + 0.6), q[1] - uy * (r + 0.6)), role, lw=lw, curve=curve, both=both)
def dots(ax, P, labels, roles, r=3.2, size='m'):
    for p, l, ro in zip(P, labels, roles):
        disc(ax, p[0], p[1], r, ro, label=l, size=size)
def panel(ax, cx, ns, nt, E, rs, rt, dx=8, r=2.4, yc=34, sp=12, ls=None, lt=None, ar=None):
    S = pts(cx - dx, ns, yc, sp); T = pts(cx + dx, nt, yc, sp)
    dots(ax, S, ls or [None] * ns, rs, r, 's'); dots(ax, T, lt or [None] * nt, rt, r, 's')
    for k, (i, j) in enumerate(E):
        link(ax, S[i], T[j], (ar[k] if ar else 'sujet'), r)
    return S, T

fig, ax = canvas(70)
y1, y2 = 56, 22
S = [(8, y1 + 6), (8, y1 - 6)]; T = [(28, y1 + 6), (28, y1 - 6)]
dots(ax, S, [r'$s_1$', r'$s_2$'], ['sujet', 'varie'], 3.0, 's')
dots(ax, T, ['a', 'b'], ['sujet', 'varie'], 3.0, 's')
link(ax, S[0], T[0], 'sujet', 3.0); link(ax, S[1], T[1], 'varie', 3.0)
box(ax, 36, y1 - 6, 50, 12, 'sujet', label=r'$s_1\neq s_2\Rightarrow\alpha(s_1)\neq\alpha(s_2)$', size='s')
box(ax, 1, y2 - 4.5, 14, 9, 'autre', label=r'$s_1=s_2$', size='s')
disc(ax, 28, y2, 3.0, 'autre', label='a', size='s')
arrow(ax, (16.2, y2), (24.4, y2), 'autre')
box(ax, 36, y2 - 6, 50, 12, 'autre', label=r'$\alpha(s_1)=\alpha(s_2)\Rightarrow s_1=s_2$', size='s')
text(ax, 44, 39, r'$\Leftrightarrow$', 'varie', 'xl'); text(ax, 54, 39, 'même vérité', 'varie', 's', ha='left')
text(ax, 44, 6, 'jamais deux flèches vers un même point', 'encre', 's')
save(fig, '42-208')
