import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
text(ax, 44, 95, r'on multiplie chacun par $\sqrt{2}+\sqrt{3}$', 'varie', 's')
fam = [r'$1$', r'$\sqrt{2}$', r'$\sqrt{3}$', r'$\sqrt{6}$']
res = [r'$\sqrt{2}+\sqrt{3}$', r'$2+\sqrt{6}$', r'$3+\sqrt{6}$', r'$3\sqrt{2}+2\sqrt{3}$']
for i in range(4):
    y = 80 - i * 12.5
    box(ax, 2, y, 16, 9, 'sujet', label=fam[i], size='m')
    arrow(ax, (18, y + 4.5), (40, y + 4.5), 'varie')
    box(ax, 40, y, 46, 9, 'sujet', label=res[i], size='s', fill=False)
text(ax, 44, 35, 'on reste dans la famille', 'sujet', 's')
arrow(ax, (44, 32), (44, 27.3), 'varie')
box(ax, 16, 18, 56, 9, 'varie', label='déterminant', size='s')
arrow(ax, (44, 18), (44, 11.3), 'varie')
box(ax, 16, 2, 56, 9, 'resultat', label=r'polynôme annulé par $u+v$', size='s')
save(fig, '66-082')
