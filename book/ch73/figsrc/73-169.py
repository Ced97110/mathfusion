import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 44, 55, r'dans $\mathbb{R}$ : $d=2$, $d^2-1=3$', 'sujet', 'm')
for i in range(3):
    box(ax, 10 + i * 24.67, 26, 22, 12, 'varie', label='c = 2')
brace(ax, 10, 10 + 2 * 24.67 + 22, 26, 'resultat', label='b = 6')
text(ax, 44, 7, r'$c=6\div 3=2$', 'resultat', 'l')
save(fig, '73-169')
