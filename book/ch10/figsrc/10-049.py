import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
f = numberline(ax, 8, 80, 40, 25, 75, step=5, labels=False, arrow_right=False)
for v in (29, 32, 68, 73):
    disc(ax, f(v), 40, 1.5, 'sujet')
    text(ax, f(v), 45, str(v), 'sujet', 's')
for c in (30, 70):
    box(ax, f(c) - 7, 22, 14, 7, 'varie', label=f'{c}')
for v, c in ((29, 30), (32, 30), (68, 70), (73, 70)):
    arrow(ax, (f(v), 38), (f(c) + (v - c) * 0.3, 29.5), 'varie')
text(ax, f(30), 17, 'groupe 1', 'varie', 's'); text(ax, f(70), 17, 'groupe 2', 'varie', 's')
text(ax, 44, 8, r'$2 \times 30 + 2 \times 70 = 200$', 'resultat', 'l')
text(ax, 44, 55, 'somme vraie : 202', 'fixe', 's')
save(fig, '10-049')
