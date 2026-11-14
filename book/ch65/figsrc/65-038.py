import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import itertools

def D(v):
    p = 1
    for i, j in itertools.combinations(range(len(v)), 2):
        p *= v[i] - v[j]
    return p

def sg(n):
    return '%d' % n if n >= 0 else '−%d' % -n

a, b = [1, 2, 3, 4], [3, 2, 1, 4]
assert D(a) == 12 and D(b) == -12
fig, ax = canvas(80)
text(ax, 44, 75, 'n’importe quelle paire échangée', 'encre', 'm', weight='bold')
for vals, y, tag, role in [(a, 52, 'avant', 'sujet'), (b, 14, 'après', 'varie')]:
    for k, v in enumerate(vals):
        x = 11 + k * 15.5
        sw = tag == 'après' and k in (0, 2)
        disc(ax, x, y + 6, 4.2, 'varie' if sw else 'sujet', label='%d' % v, size='m')
        text(ax, x, y - 2, r'$r_%d$' % (k + 1), 'fixe', 's')
    text(ax, 77, y + 6, 'D = %s' % sg(D(vals)), role, 'm', weight='bold')
# arc between positions 1 and 3 (indexes 0 and 2)
arrow(ax, (11, 63), (42, 63), 'varie', lw=1.1, curve=-0.4, both=True)
arrow(ax, (42, 40), (42, 28), 'varie', lw=1.2)
text(ax, 59, 34, r'$r_1\leftrightarrow r_3$', 'varie', 's')
save(fig, '65-038')
