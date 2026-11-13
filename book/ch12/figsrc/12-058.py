import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 58, 'des sortes différentes', 'fixe', 's')
f = numberline(ax, 6, 74, 28, 0, 8, labels=False, arrow_right=False)
items = [('1/2', 0.5, 11), ('0,75', 0.75, 31), ('π', 3.14159, 51), ('7', 7, 71)]
for lab, v, cx in items:
    box(ax, cx - 8, 40, 16, 9, 'sujet', label=lab, size='m')
    disc(ax, f(v), 28, 1.3, 'sujet')
    arrow(ax, (cx, 39.5), (f(v), 30), 'varie')
text(ax, f(0), 22.5, '0', 'fixe', 's')
box(ax, 14, 6, 60, 9, 'resultat', label='tous : des nombres réels', size='m')
save(fig, '12-058')
