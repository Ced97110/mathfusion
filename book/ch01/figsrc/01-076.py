import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
NB = ' '
fig, ax = canvas(80)
text(ax, 44, 68, '×', 'sujet', 'l', weight='bold')
text(ax, 44, 48, 'se lit « fois »', 'sujet', 's')
line(ax, [(44, 64), (44, 51)], 'sujet', lw=0.6)
text(ax, 20, 68, '4', 'varie', 'l', weight='bold')
text(ax, 20, 56, 'nombre de paquets', 'varie', 's')
line(ax, [(20, 64), (20, 59)], 'varie', lw=0.6)
text(ax, 68, 68, '1' + NB + '000', 'fixe', 'l', weight='bold')
text(ax, 68, 56, 'un paquet : mille', 'fixe', 's')
line(ax, [(68, 64), (68, 59)], 'fixe', lw=0.6)
for x in (4, 25, 46, 67):
    box(ax, x, 24, 18, 10, 'fixe', label='1' + NB + '000', size='m')
brace(ax, 4, 85, 21, 'varie')
text(ax, 44.5, 13, '4 paquets égaux de 1' + NB + '000', 'varie', 's', weight='bold')
save(fig, '01-076')
