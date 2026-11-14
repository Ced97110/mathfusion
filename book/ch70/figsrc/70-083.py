import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 60, r'$x^2+y^2=-1$ : point réel ?', 'encre', 'm')
text(ax, 30, 48, 'suite finie de calculs', 'sujet', 's')
for i in range(3):
    box(ax, 2 + i * 20, 32, 15, 11, 'sujet', label='calcul', size='s')
    if i < 2:
        arrow(ax, (17.5 + i * 20, 37.5), (21.5 + i * 20, 37.5), 'varie')
arrow(ax, (30, 31.5), (30, 21), 'varie')
box(ax, 8, 8, 44, 12, 'resultat', label='oui ou non', size='m')
box(ax, 64, 32, 22, 11, 'limite', label='deviner', size='s')
text(ax, 75, 26, 'sans garantie', 'limite', 's')
save(fig, '70-083')
