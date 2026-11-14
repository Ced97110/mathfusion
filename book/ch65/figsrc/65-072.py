import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 44, 79, 'le signe de d compte-t-il ?', 'encre', 'm')
k = 8.0
panels = [
    (22, r'$x^3-3x+1$', r'$d = 81 > 0$', 'resultat', [(1.532, 0), (0.347, 0), (-1.879, 0)], '3 racines réelles'),
    (66, r'$x^3-2$', r'$d = -108 < 0$', 'varie', [(1.26, 0), (-0.63, 1.09), (-0.63, -1.09)], '1 racine réelle'),
]
for cx, poly_s, d_s, role, roots, cap in panels:
    box(ax, cx - 18, 62, 36, 9, 'sujet', label=poly_s, size='m')
    text(ax, cx, 56, d_s, role, 's')
    line(ax, [(cx - 19, 36), (cx + 19, 36)], 'fixe')
    line(ax, [(cx, 22), (cx, 50)], 'fixe')
    for (a, b) in roots:
        disc(ax, cx + a * k, 36 + b * k, 1.7, 'sujet')
    text(ax, cx, 14, cap, role, 's')
text(ax, 44, 5, 'horizontale : axe des nombres réels', 'fixe', 's')
save(fig, '65-072')
