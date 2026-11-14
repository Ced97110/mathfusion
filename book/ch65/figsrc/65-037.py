import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def D(v):
    return (v[0] - v[1]) * (v[0] - v[2]) * (v[1] - v[2])

def sg(n):
    return '%d' % n if n >= 0 else '−%d' % -n

rows = [([1, 2, 3], 54, 'avant'), ([2, 1, 3], 14, 'après')]
fig, ax = canvas(76)
for vals, y, name in rows:
    d1, d2, d3 = vals[0] - vals[1], vals[0] - vals[2], vals[1] - vals[2]
    assert d1 * d2 * d3 == D(vals)
    text(ax, 10, y + 8, name, 'fixe', 's', ha='center')
    for k, v in enumerate(vals):
        x = 28 + k * 16
        swapped = (name == 'après' and k < 2)
        disc(ax, x, y + 8, 4.2, 'varie' if swapped else 'sujet', label='%d' % v, size='m')
    text(ax, 44, y, '(%s)(%s)(%s) = %s' % (sg(d1), sg(d2), sg(d3), sg(D(vals))), 'resultat' if name == 'avant' else 'varie', 'm', weight='bold')
    text(ax, 80, y + 8, r'$D=%s$' % sg(D(vals)).replace('−', '-'), 'sujet' if name == 'avant' else 'varie', 'm', weight='bold')
arrow(ax, (44, 46), (44, 34), 'varie', lw=1.2)
text(ax, 60, 40, r'échange $r_1\leftrightarrow r_2$', 'varie', 's')
text(ax, 44, 70, r'$D$ devient $-D$ : $-2\to 2$', 'encre', 'm', weight='bold')
save(fig, '65-037')
