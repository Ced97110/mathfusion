import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
# m = 4 : x^4 - 1 has at most 4 roots, so a group whose n elements are all roots has n <= 4
box(ax, 14, 58, 60, 11, 'sujet', label=r'$x^4 - 1$ : au plus 4 racines', size='s')
f = numberline(ax, 6, 74, 24, 0, 6, labels=True, size='s')
text(ax, 85, 24, '$n$', 'encre', 's')
line(ax, [(f(0), 36), (f(4), 36)], 'resultat', lw=3)
text(ax, (f(0) + f(4)) / 2, 41, 'n possible', 'resultat', 's')
line(ax, [(f(4.5), 36), (f(6), 36)], 'limite', lw=3)
text(ax, f(5.25), 41, 'impossible', 'limite', 's')
arrow(ax, (f(4), 54), (f(4), 29), 'varie')
text(ax, f(4) - 9, 50, r'$m = 4$', 'varie', 's')
save(fig, '67-083')
