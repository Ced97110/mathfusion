import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)

def bits(ax, x, y, s, roles, cw, ch=7.0, size='l'):
    for i, c in enumerate(s):
        box(ax, x + i * cw, y, cw, ch, roles if isinstance(roles, str) else roles[i], label=c, size=size, r=0.5)

cw = 6.0
text(ax, 44, 51, r'chaque 1 de $e$ est une erreur', 'encre', 'm', weight='bold')
for y, e, w in [(30, '0000100', 1), (10, '0100100', 2)]:
    assert e.count('1') == w
    bits(ax, 3, y, e, ['varie' if c == '1' else 'fixe' for c in e], cw)
    text(ax, 52, y + 3.5, r'$w(e) = %d$' % w, 'varie', 'l', ha='left', weight='bold')
    text(ax, 52, y - 2.0, '%s erreur%s' % ('une' if w == 1 else 'deux', '' if w == 1 else 's'), 'fixe', 's', ha='left')
save(fig, '68-047')
