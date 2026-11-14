import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)

def bits(ax, x, y, s, roles, cw, ch=6.5, size='m'):
    for i, c in enumerate(s):
        box(ax, x + i * cw, y, cw, ch, roles if isinstance(roles, str) else roles[i], label=c, size=size, r=0.5)

cw = 7.0
x0 = 28
sent = '01000001'
recv = list(sent); recv[5] = '1' if recv[5] == '0' else '0'; recv = ''.join(recv)
assert recv == '01000101' and recv.count('1') == 3
text(ax, 3, 63.25, 'envoyé', 'encre', 'm', ha='left', weight='bold')
bits(ax, x0, 60, sent, ['sujet' if c == '1' else 'fixe' for c in sent], cw)
arrow(ax, (x0 + 5.5 * cw, 58.5), (x0 + 5.5 * cw, 41.5), 'varie')
text(ax, x0 + 5.5 * cw - 2, 50, 'bruit : 6ᵉ bit inversé', 'varie', 's', ha='right')
text(ax, 3, 33.25, 'reçu', 'encre', 'm', ha='left', weight='bold')
bits(ax, x0, 30, recv, ['varie' if i == 5 else ('sujet' if c == '1' else 'fixe') for i, c in enumerate(recv)], cw)
text(ax, 44, 20, 'trois 1 : nombre impair', 'limite', 'm', weight='bold')
text(ax, 44, 11, 'erreur détectée', 'limite', 'l', weight='bold')
save(fig, '68-042')
