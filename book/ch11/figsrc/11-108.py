import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
s = 4.6
def rt(ax, p, u, v, k=1.6):
    # small right-angle mark at p between unit vectors u and v
    line(ax, [(p[0] + u[0] * k, p[1] + u[1] * k), (p[0] + (u[0] + v[0]) * k, p[1] + (u[1] + v[1]) * k), (p[0] + v[0] * k, p[1] + v[1] * k)], 'varie', lw=0.7)
# base 4, height 3 : A=(0,0) B=(4,0) C=(0,3)
x, y = 6, 26
poly(ax, [(x, y), (x + 4 * s, y), (x, y + 3 * s)], 'sujet')
line(ax, [(x, y), (x + 4 * s, y)], 'sujet', lw=2.0)
line(ax, [(x, y), (x, y + 3 * s)], 'varie', lw=1.1, dash=True); rt(ax, (x, y), (1, 0), (0, 1))
text(ax, x + 2 * s, y - 3.5, '$b$ = 4', 'sujet', 's'); text(ax, x - 1, y + 1.5 * s, '', 'varie', 's')
text(ax, x + 6, y + 3 * s + 2, '$h$ = 3', 'varie', 's')
# base 3, height 4
x2 = 38
poly(ax, [(x2, y), (x2 + 3 * s, y), (x2, y + 4 * s)], 'sujet')
line(ax, [(x2, y), (x2 + 3 * s, y)], 'sujet', lw=2.0)
line(ax, [(x2, y), (x2, y + 4 * s)], 'varie', lw=1.1, dash=True); rt(ax, (x2, y), (1, 0), (0, 1))
text(ax, x2 + 1.5 * s, y - 3.5, '$b$ = 3', 'sujet', 's')
text(ax, x2 + 7, y + 4 * s + 2, '$h$ = 4', 'varie', 's')
# base 5, height 2.4
x3 = 58
A = (x3, y); B = (x3 + 5 * s, y); C = (x3 + 1.8 * s, y + 2.4 * s)
poly(ax, [A, B, C], 'sujet')
line(ax, [A, B], 'sujet', lw=2.0)
line(ax, [C, (C[0], y)], 'varie', lw=1.1, dash=True); rt(ax, (C[0], y), (1, 0), (0, 1), 1.4)
text(ax, x3 + 2.5 * s, y - 3.5, '$b$ = 5', 'sujet', 's')
text(ax, C[0] + 9, y + 2.4 * s + 3, '$h$ = 2,4', 'varie', 's')
for cx, t in [(6 + 2 * s, '4 × 3 = 12'), (38 + 1.5 * s, '3 × 4 = 12'), (58 + 2.5 * s, '5 × 2,4 = 12')]:
    text(ax, cx, 12, t, 'resultat', 's')
text(ax, 44, 5, '$b$ × $h$ : même valeur, même triangle', 'fixe', 's')
text(ax, 44, 54, 'un triangle, trois bases', 'sujet', 'm')
save(fig, '11-108')
