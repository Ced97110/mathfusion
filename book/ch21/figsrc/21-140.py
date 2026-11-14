import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
box(ax, 8, 54, 72, 20, 'sujet', label=r'$x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$')
text(ax, 44, 46, r'le bas est $2a$', 'sujet', 'm')
arrow(ax, (30, 45), (22, 33), 'fixe'); arrow(ax, (58, 45), (66, 33), 'fixe')
box(ax, 2, 8, 40, 24, 'resultat', label=r'$a=1$ : $2a=2$' + '\nla fraction existe')
box(ax, 46, 8, 40, 24, 'limite', label=r'$a=0$ : $2a=0$' + '\nla fraction n’existe pas', size='s')
save(fig, '21-140')
