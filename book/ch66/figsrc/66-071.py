import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(75)
vals = ['3', '5', '17', '257', '65 537']
for i, v in enumerate(vals):
    box(ax, 3 + i * 17, 62, 15, 9, 'resultat', label=v, size='s')
text(ax, 44, 57, r'$F_0$ à $F_4$ : premiers', 'resultat', 's')
box(ax, 14, 38, 60, 11, 'limite', label=r'$F_5=4\,294\,967\,297$', size='m')
arrow(ax, (44, 54), (44, 49.3), 'varie')
box(ax, 8, 12, 28, 11, 'fixe', label='641', size='m')
box(ax, 52, 12, 28, 11, 'fixe', label='6 700 417', size='m')
text(ax, 44, 17.5, r'$\times$', 'encre', 'l')
arrow(ax, (30, 38), (22, 23.3), 'varie')
arrow(ax, (58, 38), (66, 23.3), 'varie')
text(ax, 44, 4, r'$F_5$ n’est pas premier', 'limite', 's')
save(fig, '66-071')
