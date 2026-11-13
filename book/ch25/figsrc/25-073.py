import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(ax, c, r, a0, a1, role="encre", n=24):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=1.1)
fig, ax = canvas(52)
def tri(x0, y0, s, hl, vl):
    C = (x0, y0); A = (x0 + 4 * s, y0); B = (x0, y0 + 3 * s)
    poly(ax, [C, A, B], 'fixe')
    line(ax, [C, A], 'sujet', lw=2.0); line(ax, [C, B], 'varie', lw=2.0); line(ax, [A, B], 'fixe', lw=1.2)
    text(ax, x0 + 2 * s, y0 - 3.2, hl, 'sujet', 's'); text(ax, x0 - 5.2, y0 + 1.5 * s, vl, 'varie', 's')
    arc(ax, A, 0.8 * s, 143.13, 180)
    text(ax, x0 + 2 * s, y0 - 9.5, '3 ÷ 4 = 0,75', 'resultat', 'm', weight='bold')
tri(13, 18, 6, '4 km', '3 km'); tri(62, 18, 3, '4 cm', '3 cm')
text(ax, 22, 44, 'colline', 'encre', 'm'); text(ax, 68, 44, 'carte réduite', 'encre', 'm')
text(ax, 45, 26, 'même angle', 'encre', 's')
save(fig, '25-073')
