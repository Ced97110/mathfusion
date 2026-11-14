import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
xs = (16, 44, 72)
before = [r'$a_2\,y^2$', r'$a_1\,y$', r'$a_0$']
after = [r'$a_2\,Y_2$', r'$a_1\,Y_1$', r'$a_0\,Y_0$']
rule = [r'$Y_2=y^2$', r'$Y_1=y$', r'$Y_0=1$']
text(ax, 44, 72, 'avant', 'sujet', 'm', weight='bold')
text(ax, 44, 11, 'après', 'resultat', 'm', weight='bold')
for x, b, a, r in zip(xs, before, after, rule):
    box(ax, x - 12, 56, 24, 11, 'sujet', label=b, size='m')
    arrow(ax, (x, 56), (x, 30), 'varie', lw=1.1)
    text(ax, x + 2.5, 43, r, 'varie', 's', ha='left')
    box(ax, x - 12, 19, 24, 11, 'resultat', label=a, size='m')
save(fig, '70-028')
