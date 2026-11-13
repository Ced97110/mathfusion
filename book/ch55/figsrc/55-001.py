import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 13, 57, r'nombre $a$', 'varie', 's')
text(ax, 44, 57, r'règle $f$', 'sujet', 's')
text(ax, 76, 57, r'$f(a)$', 'resultat', 's')
box(ax, 30, 8, 28, 44, 'sujet', label=r'$a^3-a$', size='l')
for y, a, lab in ((38, '2', r'$8-2=6$'), (20, '3', r'$27-3=24$')):
    box(ax, 4, y - 6, 18, 12, 'varie', label=a)
    arrow(ax, (22, y), (30, y), 'varie')
    arrow(ax, (58, y), (66, y), 'resultat')
    box(ax, 66, y - 6, 20, 12, 'resultat', label=lab, size='s')
save(fig, '55-001')
