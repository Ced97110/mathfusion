import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)

def bits(ax, x, y, s, roles, cw, ch=6.5, size='m'):
    for i, c in enumerate(s):
        box(ax, x + i * cw, y, cw, ch, roles if isinstance(roles, str) else roles[i], label=c, size=size, r=0.5)

cw = 7.0
x0 = 30
msg = '1000001'
text(ax, 3, 66, r'$A$ en 7 bits', 'encre', 'm', ha='left', weight='bold')
bits(ax, x0 + cw, 60, msg, ['sujet' if c == '1' else 'fixe' for c in msg], cw)
k = 0
for i, c in enumerate(msg):
    if c == '1':
        k += 1
        text(ax, x0 + cw + i * cw + cw / 2, 71, str(k), 'sujet', 's')
text(ax, 3, 52, 'deux 1 : pair', 'resultat', 'm', ha='left', weight='bold')
text(ax, 3, 45, 'on ajoute 0', 'varie', 'm', ha='left', weight='bold')
word = '0' + msg
bits(ax, x0, 24, word, ['varie'] + ['sujet' if c == '1' else 'fixe' for c in msg], cw)
for i in range(7):
    cx = x0 + cw + i * cw + cw / 2
    line(ax, [(cx, 59), (cx, 31.5 + 0.0)], 'fixe', lw=0.5, dash=True)
text(ax, 44, 14, 'les 7 bits sont recopiés', 'fixe', 's')
text(ax, 3, 27.25, 'mot envoyé', 'encre', 'm', ha='left', weight='bold')
save(fig, '68-038')
