import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

rows = [(r'$x^3-3x+1$', -3, 1), (r'$x^3-2$', 0, -2), (r'$x^3-3x+2$', -3, 2)]
exp = [81, -108, 0]
fig, ax = canvas(74)
text(ax, 44, 69, r'$x^3+px+q$ :  $d=-4p^3-27q^2$', 'sujet', 'm', weight='bold')
text(ax, 15, 60, 'polynôme', 'fixe', 's'); text(ax, 47, 60, r'$p$ et $q$', 'fixe', 's'); text(ax, 74, 60, r'$d$', 'fixe', 's')

def sg(n):
    return '%d' % n if n >= 0 else '−%d' % -n

for k, ((name, p, q), e) in enumerate(zip(rows, exp)):
    assert -4 * p ** 3 - 27 * q ** 2 == e
    y = 44 - k * 16
    box(ax, 2, y, 26, 10, 'fixe', label=name, size='s')
    box(ax, 32, y, 30, 10, 'varie', label='p=%s, q=%s' % (sg(p), sg(q)), size='s')
    box(ax, 66, y, 20, 10, 'resultat', label=sg(e), size='m', weight='bold')
    text(ax, 64, y + 5, '→', 'fixe', 's') if False else None
    text(ax, 47, y - 3.5, '%s − %s' % (sg(-4 * p ** 3), sg(27 * q ** 2).lstrip('−')) if False else '%s %s %s' % (sg(-4 * p ** 3), '−', sg(27 * q ** 2)), 'fixe', 's')
save(fig, '65-054')
