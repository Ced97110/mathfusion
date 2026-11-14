import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
for i, b in enumerate('0110'):
    box(ax, 4 + i * 10.5, 28, 9, 9, 'autre', label=b, size='l')
brace(ax, 4, 44.5, 38.5, 'autre', label='4 bits utiles : le message', down=False)
box(ax, 58, 28, 26, 9, 'sujet', label='bits de contrôle', size='s')
arrow(ax, (45.2, 32.5), (57.5, 32.5), 'varie')
text(ax, 51.3, 29.2, 'calculés', 'varie', 's')
text(ax, 71, 42.2, 'sans information nouvelle', 'sujet', 's')
brace(ax, 4, 84, 26.5, 'fixe', label='mot envoyé $y$ : utiles + contrôle', down=True)
save(fig, '68-007')
