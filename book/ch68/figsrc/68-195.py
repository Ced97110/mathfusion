import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from kit_L07 import *

def pm(a, b):
    r = [0] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            r[i + j] ^= int(u) & int(v)
    return ''.join(map(str, r))
assert pm('1101', '1011') == '1111111'
fig, ax = canvas(78)
text(ax, 44, 72, r'$g = 1 + x + x^2 + \cdots + x^6$', 'sujet', 'm')
text(ax, 2, 58, r'$0 \times g$', 'sujet', 's', ha='left')
xs, p = brow(fig, ax, 58, 58, '0000000', role='sujet')
text(ax, 2, 32, r'$1 \times g$', 'sujet', 's', ha='left')
brow(fig, ax, 58, 32, '1111111', role='sujet')
for x in xs:
    arrow(ax, (x, 54), (x, 36), 'varie', lw=0.7, both=True)
text(ax, 2, 45, 'd = 7', 'varie', 'm', ha='left')
text(ax, 44, 17, 'seulement 0000000 et 1111111', 'resultat', 's')
text(ax, 44, 9, 'répétition : 1 bit de message', 'fixe', 's')
save(fig, '68-195')
