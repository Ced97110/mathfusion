import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
text(ax, 44, 74, r'$x^3-x$ dans ℤ/3', 'sujet', 'm')
xs = [16, 44, 72]
calc = [r'$0-0=0$', r'$1-1=0$', r'$8-2=6\equiv0$']
for x, v, c in zip(xs, [0, 1, 2], calc):
    assert (v ** 3 - v) % 3 == 0
    text(ax, x, 62, rf'$x={v}$', 'varie', 'm')
    text(ax, x, 52, c, 'varie', 's')
    arrow(ax, (x, 48.5), (x, 42), 'resultat')
    box(ax, x - 7, 31, 14, 10, 'resultat', label='0', size='m')
brace(ax, 9, 79, 28, 'resultat', label='3 racines, degré 3')
text(ax, 44, 8, r'$x^3-x$ n’est pas le polynôme nul', 'sujet', 's')
save(fig, '54-272')
