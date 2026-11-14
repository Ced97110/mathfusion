import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)

def bits(ax, x, y, s, roles, cw, ch=6.5, size='m'):
    for i, c in enumerate(s):
        box(ax, x + i * cw, y, cw, ch, roles if isinstance(roles, str) else roles[i], label=c, size=size, r=0.5)

cw = 6.0
x0 = 30
brace(ax, x0, x0 + 8 * cw, 52, 'sujet', label=r'$n = 8$', down=False)
for y, name, word in [(40, 'A', '01000001'), (24, 'C', '11000011')]:
    text(ax, 10, y + 3.25, name, 'sujet', 'l', weight='bold')
    bits(ax, x0, y, word, ['varie'] + ['sujet'] * 7, cw)
brace(ax, x0 + cw, x0 + 8 * cw, 24, 'sujet', label=r'$k = 7$')
brace(ax, x0, x0 + cw, 24, 'varie', label='1 bit de contrôle')
text(ax, 44, 3, r'$2^7 = 128$ mots dans le code', 'sujet', 'm')
save(fig, '68-040')
