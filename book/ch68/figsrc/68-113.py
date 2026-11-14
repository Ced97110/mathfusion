import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
for i, x in enumerate([6, 30, 54]):
    box(ax, x, 28, 14, 9, 'sujet', label=rf'$x_{i + 1}$')
brace(ax, 6, 44, 37, 'varie', label=r'$x_1+x_2=0$', down=False)
brace(ax, 30, 68, 28, 'varie', label=r'$x_2+x_3=0$', down=True)
text(ax, 4, 7, 'solutions :', 'encre', 'm', ha='left')
box(ax, 34, 2, 16, 9, 'resultat', label='000')
box(ax, 56, 2, 16, 9, 'resultat', label='111')
save(fig, '68-113')
