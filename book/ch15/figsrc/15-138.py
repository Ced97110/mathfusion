import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(55)
text(ax, 44, 51, r'$3/x$', 'sujet', 'l')
f = numberline(ax, 14, 74, 14, 0, 4, arrow_right=False)
for v, role, lab in ((2, 'resultat', '1,5'), (4, 'resultat', '0,75')):
    disc(ax, f(v), 14, 1.3, role)
    arrow(ax, (f(v), 17), (f(v), 27), role)
    box(ax, f(v) - 8, 28, 16, 9, role, label=lab)
disc(ax, f(0), 14, 1.3, 'limite', fill=False)
arrow(ax, (f(0), 17), (f(0), 27), 'limite')
box(ax, f(0) - 12, 28, 24, 9, 'limite', label='pas de résultat', size='s')
text(ax, 44, 43, r'condition : $x \neq 0$', 'sujet', 'm')
save(fig, '15-138')
