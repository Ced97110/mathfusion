import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 21, 56, 'polynôme', 'sujet', 'm', weight='bold')
text(ax, 69, 56, 'fonction', 'resultat', 'm', weight='bold')
rows = [(40, '(0, −1, 0, 1)', r'$s \mapsto s^3 - s$'), (12, '(0, 0, 0, 0)', r'$s \mapsto 0$')]
for y, a, b in rows:
    box(ax, 4, y, 34, 11, 'sujet', label=a)
    box(ax, 52, y, 34, 11, 'resultat', label=b)
    arrow(ax, (39, y + 5.5), (51, y + 5.5), 'varie')
text(ax, 44, 31, r'$f(x) \mapsto f(s)$', 'varie', 'm')
save(fig, '55-035')
