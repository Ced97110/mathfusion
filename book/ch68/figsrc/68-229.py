import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)

def bits(ax, x, y, s, roles, cw, ch=6.5, size='m'):
    for i, c in enumerate(s):
        box(ax, x + i * cw, y, cw, ch, roles if isinstance(roles, str) else roles[i], label=c, size=size, r=0.5)

cw = 6.5
x0 = 3
text(ax, 3, 56, 'trois mots binaires, même taille de case', 'encre', 's', ha='left')
bits(ax, x0, 40, '0', 'fixe', cw)
text(ax, 62, 43.25, '1 bit', 'fixe', 's', ha='left')
bits(ax, x0, 26, '1000001', 'fixe', cw)
text(ax, 62, 29.25, 'mot ASCII : 7 bits', 'fixe', 's', ha='left')
bits(ax, x0, 12, '01000001', ['varie'] + ['sujet'] * 7, cw)
text(ax, 62, 15.25, 'octet : 8 bits', 'sujet', 's', ha='left', weight='bold')
text(ax, x0, 6, 'bit de parité', 'varie', 's', ha='left')
save(fig, '68-229')
