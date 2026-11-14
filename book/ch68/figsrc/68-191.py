import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from kit_L07 import *

def pm(a, b):
    r = [0] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            r[i + j] ^= int(u) & int(v)
    return ''.join(map(str, r))

f1, f2, f3 = '11', '1101', '1011'
p12 = pm(f1, f2); p123 = pm(p12, f3)
assert p12 == '10111' and p123 == '10000001'
fig, ax = canvas(78)
X0 = 38
text(ax, 2, 71, '1 + x', 'sujet', 's', ha='left')
lrow(fig, ax, X0, 71, f1, role='sujet', size='m', k=5, h=5.4)
text(ax, 2, 61, r'$\times\ (1 + x + x^3)$', 'sujet', 's', ha='left')
lrow(fig, ax, X0, 61, f2, role='sujet', size='m', k=5, h=5.4)
text(ax, 2, 51, r'$= 1 + x^2 + x^3 + x^4$', 'fixe', 's', ha='left')
lrow(fig, ax, X0, 51, p12, role='fixe', size='m', k=5, h=5.4)
text(ax, 2, 41, r'$\times\ (1 + x^2 + x^3)$', 'sujet', 's', ha='left')
lrow(fig, ax, X0, 41, f3, role='sujet', size='m', k=5, h=5.4)
line(ax, [(2, 34), (86, 34)], 'fixe')
text(ax, 2, 27, r'$= x^7 + 1$', 'resultat', 'm', ha='left')
lrow(fig, ax, X0, 27, p123, role='resultat', size='m', k=5, h=5.4)
text(ax, 44, 12, 'les autres termes s’annulent', 'varie', 's')
save(fig, '68-191')
