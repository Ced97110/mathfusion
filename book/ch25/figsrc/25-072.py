import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(ax, c, r, a0, a1, role="limite", n=24):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=1.1)
fig, ax = canvas(54)
s = 4.0
def tri(x0, y0, hl, vl):
    C = (x0, y0); A = (x0 + 4 * s, y0); B = (x0, y0 + 3 * s)
    poly(ax, [C, A, B], 'fixe')
    line(ax, [C, A], 'sujet', lw=2.0); line(ax, [C, B], 'varie', lw=2.0); line(ax, [A, B], 'fixe', lw=1.2)
    text(ax, x0 + 2 * s, y0 - 3.2, hl, 'sujet', 's'); text(ax, x0 - 5.2, y0 + 1.5 * s, vl, 'varie', 's')
tri(14, 24, '4 m', '3 m'); tri(58, 24, '400 cm', '3 m')
text(ax, 22, 46, 'même unité', 'resultat', 'm'); text(ax, 66, 46, 'unités mélangées', 'limite', 'm')
text(ax, 22, 13, r'$\dfrac{3\ \mathrm{m}}{4\ \mathrm{m}} = 0{,}75$', 'resultat', 'm')
text(ax, 22, 3.5, 'sans unité', 'resultat', 's')
text(ax, 66, 13, r'$\dfrac{3}{400} = 0{,}0075$', 'limite', 'm')
text(ax, 66, 3.5, 'dépend de l’unité', 'limite', 's')
line(ax, [(44, 2), (44, 50)], 'fixe', dash=True, lw=0.7)
save(fig, '25-072')
