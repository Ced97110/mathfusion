import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(94)
cx = 58
ys = [80, 58, 36, 14]
rows = [('haut', 'sujet', r'$\frac{1}{4} + \frac{3}{8} = \frac{2}{8} + \frac{3}{8} = \frac{5}{8}$'),
        ('bas', 'autre', r'$\frac{1}{2} + \frac{5}{24} = \frac{12}{24} + \frac{5}{24} = \frac{17}{24}$'),
        ('diviser', 'varie', r'$\frac{5}{8} \div \frac{17}{24} = \frac{5}{8} \times \frac{24}{17}$'),
        ('simplifier', 'resultat', r'$\frac{5 \times 3}{17} = \frac{15}{17}$')]
for y, (lab, role, expr) in zip(ys, rows):
    text(ax, 3, y, lab, role, 'm', ha='left', weight='bold')
    text(ax, cx, y, expr, role, 'm' if role != 'resultat' else 'l')
for a, b in [(0, 1), (1, 2), (2, 3)]:
    arrow(ax, (10, ys[a] - 7), (10, ys[b] + 7), 'fixe')
text(ax, cx - 5, ys[3] - 11 + 2, '8 et 24 : facteur 8', 'varie', 's')
save(fig, '07-070')
