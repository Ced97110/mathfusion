import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
u = 2.4
text(ax, 4, 56, 'e = 3 : 2 multiplications', 'sujet', 's', ha='left')
box(ax, 4, 46, 2 * u, 6, 'sujet', r=0.2)
text(ax, 4, 40, 'e = 27 : 26 multiplications', 'sujet', 's', ha='left')
box(ax, 4, 30, 26 * u, 6, 'sujet', r=0.2)
text(ax, 4, 24, 'e de 300 chiffres :', 'limite', 's', ha='left')
box(ax, 4, 12, 80, 6, 'limite', label='un nombre de 300 chiffres', size='s', r=0.2)
text(ax, 44, 5, 'impossible à faire', 'limite', 's')
save(fig, '53-110')
