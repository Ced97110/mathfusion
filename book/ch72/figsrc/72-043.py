import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
steps = [('sujet', r'$B(y, x) = 4$'), ('sujet', r'$B(x, x) = 5$'), ('varie', r'$p = \frac{4}{5}\, x$'),
         ('varie', r'$q = y - p$'), ('resultat', r'$B(q, x) = 4 - 4 = 0$')]
ys = [76, 61, 46, 31, 12]
for (role, t), y in zip(steps, ys):
    box(ax, 12, y, 64, 11 if y > 12 else 14, role, label=t, size='l' if role == 'resultat' else 'm')
for y0, y1 in zip(ys[:-1], ys[1:]):
    h1 = 11
    arrow(ax, (44, y0), (44, y1 + (14 if y1 == 12 else 11)), 'fixe')
text(ax, 84, 37, 'diviser par 5', 'fixe', 's', rot=90) if False else None
text(ax, 44, 5, r'possible car $B(x, x) \neq 0$', 'limite', 's')
save(fig, '72-043')
