import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
text(ax, 44, 88, r'$\alpha^3=\alpha+1$', 'fixe', 'm')
text(ax, 44, 80, r'$c+d\alpha+e\alpha^2$', 'sujet', 'l')
for i, s in enumerate((r'$c$ = 0 ou 1', r'$d$ = 0 ou 1', r'$e$ = 0 ou 1')):
    box(ax, 4 + i * 27.5, 62, 26, 9, 'varie', label=s, size='s')
brace(ax, 4, 85.5, 62, 'varie', label=r'$2\times2\times2=8$', down=True)
els = ['0', '1', r'$\alpha$', r'$\alpha+1$', r'$\alpha^2$', r'$\alpha^2+1$', r'$\alpha^2+\alpha$', r'$\alpha^2+\alpha+1$']
for i, s in enumerate(els):
    r, c = divmod(i, 4)
    box(ax, 3 + c * 21.5, 22 - r * 13, 20, 9.5, 'sujet', label=s, size='s')
arrow(ax, (44, 46), (44, 33), 'fixe')
save(fig, '67-093')
