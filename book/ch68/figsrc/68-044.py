import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)

def bits(ax, x, y, s, roles, cw, ch=6.5, size='m'):
    for i, c in enumerate(s):
        box(ax, x + i * cw, y, cw, ch, roles if isinstance(roles, str) else roles[i], label=c, size=size, r=0.5)

cw = 7.0
x0 = 28
sent = '01000001'
recv = '11000011'
diff = [i for i in range(8) if sent[i] != recv[i]]
assert diff == [0, 6]
text(ax, 3, 67.25, 'envoyé : A', 'encre', 'm', ha='left', weight='bold')
bits(ax, x0 + 0, 64, sent, ['sujet' if c == '1' else 'fixe' for c in sent], cw)
text(ax, 3, 31.25, 'reçu : C', 'encre', 'm', ha='left', weight='bold')
bits(ax, x0, 28, recv, ['varie' if i in diff else ('sujet' if c == '1' else 'fixe') for i, c in enumerate(recv)], cw)
for i in diff:
    arrow(ax, (x0 + i * cw + cw / 2, 62.5), (x0 + i * cw + cw / 2, 35.5), 'varie')
text(ax, 44, 49.5, 'deux bits inversés', 'varie', 'm')
text(ax, 44, 18, 'quatre 1 : nombre pair', 'resultat', 'm', weight='bold')
text(ax, 44, 9, 'aucune alarme : erreur non vue', 'limite', 'm', weight='bold')
save(fig, '68-044')
