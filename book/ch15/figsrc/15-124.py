import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
text(ax, 44, 62, r'$(a+b)(a-b)=a^2-b^2$', 'encre', 'l')
box(ax, 8, 40, 30, 11, 'sujet', label=r'$a=30$', size='m'); box(ax, 50, 40, 30, 11, 'varie', label=r'$b=1$', size='m')
arrow(ax, (23, 58), (23, 51.5), 'sujet'); arrow(ax, (65, 58), (65, 51.5), 'varie')
text(ax, 44, 34, 'nombres connus', 'fixe', 's')
text(ax, 44, 25, r'$(30+1)(30-1)=30^2-1^2$', 'encre', 'm')
text(ax, 44, 14, r'$=900-1=899$', 'resultat', 'l', weight='bold')
save(fig, '15-124')
