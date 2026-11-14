import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
cx = [52, 72]
for x, s in zip(cx, [r'$x=1$', r'$x=2$']): text(ax, x, 58, s, 'varie', 'm')
rows = [(40, r'$x^4+7x^3+6x^2+28x+8$', 'résultat juste', 'resultat', ['50', '160']),
        (14, r'$x^4+6x^3+7x^2+28x+8$', '7 et 6 échangés', 'limite', ['50', '156'])]
for y, e, lab, r, v in rows:
    text(ax, 2, y + 15, e, r, 's', ha='left'); text(ax, 2, y + 6, lab, r, 's', ha='left')
    for x, s in zip(cx, v): box(ax, x - 8, y, 16, 12, r, label=s, size='l')
text(ax, 62, 33.5, '50 = 50 : erreur non vue', 'encre', 's', ha='center')
text(ax, 72, 5, '160 ≠ 156', 'limite', 's')
text(ax, 44, 63.5, 'comparer les deux écritures', 'encre', 's') if False else None
save(fig, '15-121')
