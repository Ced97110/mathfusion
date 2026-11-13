import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
names = [r'$H$', r'$rH$', r'$r^2H$', r'$r^3H$']
els = [['1', r'$s$'], [r'$r$', r'$rs$'], [r'$r^2$', r'$r^2s$'], [r'$r^3$', r'$r^3s$']]
roles = ['sujet', 'varie', 'varie', 'varie']
for i in range(4):
    x0 = 2.25 + i * 21.5
    text(ax, x0 + 9.5, 33, names[i], roles[i], 'l')
    for j in range(2):
        box(ax, x0 + j * 10, 20, 9, 9, roles[i], label=els[i][j], size='s')
brace(ax, 2.25, 21.25, 20, 'fixe', label='2')
brace(ax, 2.25, 85.75, 10, 'resultat', label=r'$4\times 2=8$', size='m')
save(fig, '47-177')
