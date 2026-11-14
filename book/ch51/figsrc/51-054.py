import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 44, 46, 'cadran à 7 heures', 'fixe', 'm')
for i in range(7):
    x = 8 + i * 11.5
    if i == 0: disc(ax, x, 30, 4.6, 'fixe', fill=False, label='0', size='m')
    else: disc(ax, x, 30, 4.6, 'sujet', label=str(i), size='m')
box(ax, 13, 21, 70, 18, 'sujet', fill=False, dash=True)
brace(ax, 13, 83, 21, 'sujet', label=r'$D^*$ : 6 éléments', down=True)
text(ax, 8, 12, '0 retiré', 'fixe', 's')
save(fig, '51-054')
