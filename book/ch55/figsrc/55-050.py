import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 70, r'$x_1^3 - x_1$ : polynôme non nul', 'sujet', 'm')
text(ax, 44, 63, 'vaut 0 aux 9 couples', 'limite', 'm')
for i in range(3):
    for j in range(3):
        box(ax, 22 + i * 12, 12 + j * 12, 12, 12, 'limite', r=0.3, label='0', size='s')
text(ax, 40, 7, r'$a_1$', 'fixe', 's')
text(ax, 17, 30, r'$a_2$', 'fixe', 's')
text(ax, 74, 30, r'$F$ fini :' + '\nthéorème\nfaux', 'limite', 's')
save(fig, '55-050')
