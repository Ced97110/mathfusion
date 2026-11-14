import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)

def bits(ax, x, y, s, roles, cw, ch=6.5, size='m'):
    for i, c in enumerate(s):
        box(ax, x + i * cw, y, cw, ch, roles if isinstance(roles, str) else roles[i], label=c, size=size, r=0.5)

cw = 8.0
x = 44 - 4 * cw
word = '01000001'
roles = ['varie'] + ['sujet' if c == '1' else 'fixe' for c in word[1:]]
text(ax, 44, 56, 'lettre A : 8 bits envoyés', 'encre', 'm', weight='bold')
bits(ax, x, 36, word, roles, cw)
brace(ax, x, x + 8 * cw, 43, 'resultat', label='deux 1 en tout : nombre pair', down=False, depth=2.0)
brace(ax, x, x + cw, 36, 'varie', label='bit de parité', depth=1.6)
brace(ax, x + cw, x + 8 * cw, 36, 'fixe', label='message : 7 bits')
text(ax, 44, 8, 'bit en tête, choisi pour que le total soit pair', 'varie', 's')
save(fig, '68-037')
