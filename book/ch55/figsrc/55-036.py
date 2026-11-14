import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
text(ax, 22, 80, 'polynôme', 'sujet', 'm', weight='bold')
text(ax, 67, 80, 'valeur en 2', 'resultat', 'm', weight='bold')
rows = [('sujet', r'$f = s^2$', '4'), ('autre', r'$g = s + 1$', '3'),
        ('varie', r'$f + g$', r'$7 = 4 + 3$'), ('varie', r'$f \times g$', r'$12 = 4 \times 3$')]
for k, (role, a, b) in enumerate(rows):
    y = 62 - k * 17
    box(ax, 3, y, 38, 11, role, label=a, size='l')
    arrow(ax, (43, y + 5.5), (51, y + 5.5), 'fixe')
    box(ax, 52, y, 34, 11, 'resultat' if k >= 2 else role, label=b, size='l')
text(ax, 44, 7, 'la valeur de la somme est la somme des valeurs', 'encre', 's')
save(fig, '55-036')
