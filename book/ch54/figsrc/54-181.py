import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 60, r'$x^2(3+2x)=3x^2+2x^3$', 'sujet', 'l')
base = 14
line(ax, [(4, base), (84, base)], 'fixe')
vals = [0, 0, 3, 2, 0]
for k, v in enumerate(vals):
    cx = 13 + 15 * k
    text(ax, cx, 9, f'rang {k}', 'fixe', 's')
    if v:
        box(ax, cx - 4.5, base, 9, 6 * v, 'sujet')
        text(ax, cx, base + 6 * v + 3, str(v), 'sujet', 'm')
    else:
        text(ax, cx, base + 3.5, '0', 'fixe', 'm')
brace(ax, 6.5, 35.5, 36, 'fixe', label='toujours 0', down=False)
brace(ax, 38.5, 77.5, 36, 'varie', label='libres', down=False)
save(fig, '54-181')
