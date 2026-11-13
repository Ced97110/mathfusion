import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
text(ax, 22, 80, 'polynôme', 'sujet', 'm', weight='bold')
text(ax, 67, 80, r'valeur en $(2, 3)$', 'resultat', 'm', weight='bold')
rows = [('sujet', r'$f = x_1 + x_2$', '5'), ('autre', r'$g = x_1 x_2$', '6'),
        ('varie', r'$f + g$', r'$11 = 5 + 6$'), ('varie', r'$f\,g$', r'$30 = 5 \times 6$')]
for k, (role, a, b) in enumerate(rows):
    y = 62 - k * 16
    box(ax, 3, y, 38, 11, role, label=a)
    arrow(ax, (43, y + 5.5), (51, y + 5.5), 'fixe')
    box(ax, 52, y, 34, 11, 'resultat' if k >= 2 else role, label=b)
text(ax, 44, 7, r'$f(x_1,x_2) \mapsto f(s_1,s_2)$', 'varie', 'm')
save(fig, '55-049')
