import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)

def bits(ax, x, y, s, roles, cw, ch=6.5, size='m'):
    for i, c in enumerate(s):
        box(ax, x + i * cw, y, cw, ch, roles if isinstance(roles, str) else roles[i], label=c, size=size, r=0.5)

cw = 5.5
text(ax, 44, 58, r'$x_1 + x_2 + \cdots + x_8 = 0$ ?', 'sujet', 'l', weight='bold')
for y, word, calc, verdict, role in [(38, '01000001', '1 + 1 = 0', 'relation vraie : accepté', 'resultat'),
                                     (14, '01000101', '1 + 1 + 1 = 1', 'relation fausse : erreur', 'limite')]:
    bits(ax, 3, y, word, ['sujet' if c == '1' else 'fixe' for c in word], cw)
    text(ax, 68, y + 8.5, calc, 'encre', 'm', weight='bold')
    text(ax, 68, y + 2, verdict, role, 's')
save(fig, '68-041')
