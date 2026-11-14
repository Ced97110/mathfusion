import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)

def bits(ax, x, y, s, roles, cw, ch=5.0, size='m'):
    for i, c in enumerate(s):
        box(ax, x + i * cw, y, cw, ch, roles if isinstance(roles, str) else roles[i], label=c, size=size, r=0.5)

def flip(s, i):
    return s[:i] + ('1' if s[i] == '0' else '0') + s[i + 1:]

recv = '10011000'
assert recv.count('1') == 3
text(ax, 44, 86, 'reçu : trois 1, impair', 'limite', 'm', weight='bold')
cw0 = 6.0
bits(ax, 44 - 4 * cw0, 73, recv, ['limite' if c == '1' else 'fixe' for c in recv], cw0, ch=6.0)
text(ax, 44, 64, '8 corrections possibles', 'varie', 'm', weight='bold')
cw = 4.0
for i in range(8):
    cand = flip(recv, i)
    assert cand.count('1') % 2 == 0
    col, row = i % 2, i // 2
    x = 8 + col * 42
    y = 50 - row * 10.5
    bits(ax, x, y, cand, ['varie' if j == i else ('sujet' if c == '1' else 'fixe') for j, c in enumerate(cand)], cw, size='s')
text(ax, 44, 4, 'toutes ont un nombre pair de 1 : laquelle ?', 'resultat', 'm', weight='bold')
save(fig, '68-045')
