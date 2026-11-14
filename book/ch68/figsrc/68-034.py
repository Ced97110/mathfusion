import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)

def bits(ax, x, y, s, roles, cw, ch=5.5, size='m'):
    for i, c in enumerate(s):
        box(ax, x + i * cw, y, cw, ch, roles if isinstance(roles, str) else roles[i], label=c, size=size, r=0.5)

cw = 5.2
# répétition triple : message en tête, 2 bits de contrôle
text(ax, 4, 64, 'répétition triple', 'sujet', 'm', ha='left', weight='bold')
x = 44 - 1.5 * cw
bits(ax, x, 50, '111', ['fixe', 'varie', 'varie'], cw)
brace(ax, x + cw, x + 3 * cw, 50, 'varie', label=r'$3 - 1 = 2$ bits de contrôle')
# bit de parité : 1 bit de contrôle en tête
text(ax, 4, 38, 'bit de parité', 'sujet', 'm', ha='left', weight='bold')
x = 44 - 4 * cw
bits(ax, x, 24, '01000001', ['varie'] + ['fixe'] * 7, cw)
brace(ax, x, x + cw, 24, 'varie', label=r'$8 - 7 = 1$ bit de contrôle')
# légende
box(ax, 4, 3, 7, 6, 'fixe')
text(ax, 13, 6, 'bits du message', 'fixe', 's', ha='left')
box(ax, 50, 3, 7, 6, 'varie')
text(ax, 59, 6, 'bits de contrôle', 'varie', 's', ha='left')
save(fig, '68-034')
