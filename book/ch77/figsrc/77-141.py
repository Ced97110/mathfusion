import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 60, 'trace de xy, base 1 et √2', 'encre', 's')
text(ax, 32, 50, '1', 'sujet', 'm'); text(ax, 60, 50, '√2', 'sujet', 'm'); text(ax, 6, 38, '1', 'autre', 'm'); text(ax, 6, 22, '√2', 'autre', 'm')
cells = [(0, 0, r'$T(1\cdot1)=2$', 'resultat'), (1, 0, r'$T(1\cdot\sqrt{2})=0$', 'fixe'), (0, 1, r'$T(\sqrt{2}\cdot1)=0$', 'fixe'), (1, 1, r'$T(2)=4$', 'resultat')]
for i, j, s, r in cells:
    box(ax, 12 + i * 38, 32 - j * 16 , 36, 12, r, label=s, size='s')
box(ax, 22, 2, 44, 10, 'varie', label='déterminant 8', size='m')
save(fig, '77-141')
