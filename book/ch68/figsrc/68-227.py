import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)

def bits(ax, x, y, s, roles, cw, ch=6.5, size='m'):
    for i, c in enumerate(s):
        box(ax, x + i * cw, y, cw, ch, roles if isinstance(roles, str) else roles[i], label=c, size=size, r=0.5)

cw = 7.0
x0 = 36
weights = [64, 32, 16, 8, 4, 2, 1]
text(ax, 44, 61, 'chaque lettre : un mot de 7 bits', 'encre', 'm', weight='bold')
for i, wgt in enumerate(weights):
    text(ax, x0 + i * cw + cw / 2, 50, str(wgt), 'fixe', 's')
text(ax, 3, 50, 'valeur du bit', 'fixe', 's', ha='left')
for y, name, sub, word in [(30, 'A = 65', '64 + 1', '1000001'), (10, 'C = 67', '64 + 2 + 1', '1000011')]:
    text(ax, 3, y + 5.5, name, 'sujet', 'l', ha='left', weight='bold')
    text(ax, 3, y + 0.5, sub, 'fixe', 's', ha='left')
    bits(ax, x0, y, word, ['sujet' if c == '1' else 'fixe' for c in word], cw)
save(fig, '68-227')
