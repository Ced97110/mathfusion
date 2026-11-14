import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

a1, a2, a3 = 6, 11, 6
terms = [(r'$-4a_1^3a_3$', r'$-4\times 6^3\times 6$', -4 * a1 ** 3 * a3),
         (r'$a_1^2a_2^2$', r'$6^2\times 11^2$', a1 ** 2 * a2 ** 2),
         (r'$18a_1a_2a_3$', r'$18\times 6\times 11\times 6$', 18 * a1 * a2 * a3),
         (r'$-4a_2^3$', r'$-4\times 11^3$', -4 * a2 ** 3),
         (r'$-27a_3^2$', r'$-27\times 6^2$', -27 * a3 ** 2)]
vals = [t[2] for t in terms]
assert vals == [-5184, 4356, 7128, -5324, -972] and sum(vals) == 4 == (-2) ** 2
assert -4 * 6 ** 3 * 6 == vals[0] and 6 ** 2 * 11 ** 2 == vals[1] and 18 * 6 * 11 * 6 == vals[2]
assert -4 * 11 ** 3 == vals[3] and -27 * 6 ** 2 == vals[4]

def fr(n):
    s = '{:,}'.format(abs(n)).replace(',', ' ')
    return ('−' if n < 0 else '') + s

fig, ax = canvas(94)
text(ax, 44, 90, r'$a_1=6,\ a_2=11,\ a_3=6$', 'sujet', 'm', weight='bold')
text(ax, 44, 82, r'$d$ = somme de cinq termes', 'sujet', 's')
for k, (sym, calc, v) in enumerate(terms):
    y = 66 - k * 12
    box(ax, 2, y, 32, 10, 'sujet', label=sym, size='s')
    arrow(ax, (34.5, y + 5), (39, y + 5), 'fixe', lw=0.8)
    box(ax, 39.5, y, 46.5, 10, 'varie', label=calc + ' = ' + fr(v), size='s', weight='bold')
line(ax, [(39.5, 16), (86, 16)], 'fixe', lw=0.9)
text(ax, 20, 8.5, 'somme des cinq', 'fixe', 's')
box(ax, 39.5, 3, 46.5, 10, 'resultat', label='4 = (−2)²', size='s', weight='bold')
save(fig, '65-053')
