import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arcpts(c, r, a0, a1, n=48):
    return [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]

def rmark(ax, p, d1, d2, s=2.5, role="fixe"):
    a = (p[0] + d1[0] * s, p[1] + d1[1] * s); b = (a[0] + d2[0] * s, a[1] + d2[1] * s); c = (p[0] + d2[0] * s, p[1] + d2[1] * s)
    line(ax, [a, b, c], role, lw=0.7)

fig, ax = canvas(52)
u = 30; O = (22, 6)
B = (O[0], O[1] + u); S = (O[0] + 1.4281 * u, O[1] + u)
A = (O[0] + u, O[1]); T = (A[0], O[1] + 0.7002 * u)
line(ax, arcpts(O, u, 0, 90), 'fixe')
line(ax, [O, A, T], 'fixe', dash=True)
poly(ax, [O, B, S], 'sujet')
text(ax, O[0] - 3, O[1] - 2, 'O', 'encre', 's'); text(ax, B[0] - 3, B[1] + 2, 'B', 'sujet', 's')
text(ax, S[0] + 3, S[1] + 2, 'S', 'sujet', 's'); text(ax, A[0], A[1] - 3, 'A', 'fixe', 's'); text(ax, T[0] + 3.5, T[1], 'T', 'fixe', 's')
text(ax, B[0] - 2, (O[1] + B[1]) / 2, 'OB = 1', 'sujet', 's', ha='right')
text(ax, (B[0] + S[0]) / 2, B[1] + 4, 'BS = tan(90° − θ)', 'sujet', 's')
text(ax, 56, 16, 'OS = sec(90° − θ)', 'sujet', 's', ha='left')
line(ax, arcpts(O, 9, 35, 90), 'varie', lw=1.0); line(ax, arcpts(S, 8, 180, 215), 'autre', lw=1.0)
text(ax, O[0] + 5, O[1] + 15, '90° − θ = 55°', 'varie', 's', ha='left'); text(ax, S[0] + 1, S[1] - 8, 'θ = 35°', 'autre', 's', ha='left')
save(fig, '31-034')
