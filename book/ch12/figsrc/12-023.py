import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
for g in range(3):
    gx = 6 + g * 27
    box(ax, gx, 34, 23, 20, 'sujet')
    for k in range(4):
        disc(ax, gx + 4.5 + k * 4.7, 44, 1.8, 'sujet')
    text(ax, gx + 11.5, 38, '4', 'sujet', 's')
text(ax, 44, 59, '3 groupes de 4', 'sujet', 'm')
text(ax, 44, 27, '$4 + 4 + 4 = 12$', 'resultat', 'm')
box(ax, 20, 5, 48, 14, 'varie', label=r'$3 \cdot 4$ : 3 fois 4', size='m')
arrow(ax, (44, 21), (44, 25), 'varie') if False else None
save(fig, '12-023')
