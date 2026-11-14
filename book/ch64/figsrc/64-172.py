import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 68, r'$f(x)=x^5-6x^3-27x-3$', 'sujet', 'l')
f = lambda x: x ** 5 - 6 * x ** 3 - 27 * x - 3
assert (f(0), f(3), f(4)) == (-3, -3, 529)
rows = ((46, '0', r'$f(0)=-3$', -3), (28, '3', r'$f(3)=243-162-81-3=-3$', -3), (10, '4', r'$f(4)=1024-384-108-3=529$', 529))
for y, x, calc, v in rows:
    box(ax, 3, y, 15, 13, 'varie', label=f'$x={x}$', size='s')
    box(ax, 21, y, 51, 13, 'sujet', label=calc, size='s')
    neg = v < 0
    box(ax, 75, y, 11, 13, 'fixe' if neg else 'resultat', label='−' if neg else '+', size='xl', weight='bold')
save(fig, '64-172')
