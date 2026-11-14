import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)

def bits(ax, x, y, s, roles, cw, ch=7.0, size='l'):
    for i, c in enumerate(s):
        box(ax, x + i * cw, y, cw, ch, roles if isinstance(roles, str) else roles[i], label=c, size=size, r=0.5)

x, y = '10101', '11010'
s = ''.join(str((int(a) + int(b)) % 2) for a, b in zip(x, y))
assert s == '01111' and s.count('1') == 4
cw = 10.0
x0 = 28
text(ax, 44, 61, r'$x + y$ position par position', 'encre', 'm', weight='bold')
text(ax, 16, 50.5, r'$x$', 'sujet', 'l', weight='bold')
bits(ax, x0, 47, x, 'sujet', cw)
text(ax, 16, 38.5, r'$+\ y$', 'autre', 'l', weight='bold')
bits(ax, x0, 35, y, 'autre', cw)
line(ax, [(8, 31.5), (x0 + 5 * cw + 2, 31.5)], 'fixe', lw=1.0)
text(ax, 16, 24.5, r'$=$', 'encre', 'l')
bits(ax, x0, 21, s, ['resultat' if c == '1' else 'fixe' for c in s], cw)
brace(ax, x0 + cw, x0 + 5 * cw, 21, 'resultat', label=r'quatre 1 : $w(x + y) = 4$', size='m')
save(fig, '68-052')
