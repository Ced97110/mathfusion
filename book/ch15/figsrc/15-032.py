import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
xs = [42, 58, 74]
text(ax, 14, 56, r'$x$', 'varie', 'm')
for v, x in zip(['1', '2', '3'], xs): box(ax, x - 6, 51, 12, 9, 'varie', label=v)
text(ax, 14, 41, r'$7x$', 'varie', 'm')
for v, x in zip(['7', '14', '21'], xs): box(ax, x - 6, 36, 12, 9, 'varie', label=v)
text(ax, 14, 26, r'$12$', 'sujet', 'm')
for v, x in zip(['12', '12', '12'], xs): box(ax, x - 6, 21, 12, 9, 'sujet', label=v)
text(ax, 44, 12, '$7x$ change avec $x$', 'varie', 's')
text(ax, 44, 5, '12 ne change pas : constante', 'sujet', 's')
save(fig, '15-032')
