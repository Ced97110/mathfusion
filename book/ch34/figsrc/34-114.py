import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
box(ax, 14, 62, 60, 12, 'sujet', label=r'$(\sqrt{6}+\sqrt{2})/4$', size='l')
arrow(ax, (44, 62), (44, 54), 'varie')
box(ax, 8, 42, 72, 12, 'varie', label=r'2,4495 + 1,4142 = 3,8637', size='s')
arrow(ax, (44, 42), (44, 34), 'varie')
box(ax, 24, 22, 40, 12, 'resultat', label='0,9659', size='l')
x0, x1 = 8, 70
f = numberline(ax, x0, x1, 14, 0, 1, step=0.5, arrow_right=False)
ax.plot([f(1), f(1)], [14, 17.5], color=COL['fixe'], lw=1.2)
disc(ax, f(0.9659), 14, 1.4, 'resultat')
text(ax, 40, 2, 'le nombre reste sous 1', 'resultat', 's')
text(ax, 49, 38, r'$\div 4$', 'varie', 'm', ha='left')
save(fig, '34-114')
