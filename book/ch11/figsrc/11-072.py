import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
for i in range(3):
    y = 78 - i * 12
    box(ax, 18, y, 20, 9, 'sujet', label='4 pi', size='m'); box(ax, 38, y, 28, 9, 'varie', label='9 po', size='m')
brace(ax, 18, 38, 45, 'sujet', label='3 × 4 pi'); brace(ax, 38, 66, 45, 'varie', label='3 × 9 po')
box(ax, 18, 24, 20, 9, 'sujet', label='12 pi', size='m'); box(ax, 38, 24, 28, 9, 'varie', label='27 po', size='m')
arrow(ax, (44, 22), (44, 16), 'fixe')
box(ax, 20, 4, 48, 10, 'resultat', label='14 pi 3 po', size='l')
save(fig, '11-072')
