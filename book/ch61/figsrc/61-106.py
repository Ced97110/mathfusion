import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
box(ax, 4, 68, 80, 11, 'sujet', label=r'$b_1+b_2\sqrt{2}+b_3\sqrt{3}+b_4\sqrt{6}=0$', size='s')
box(ax, 4, 40, 38, 11, 'varie', label=r'$b_1+b_2\sqrt{2}=0$', size='s')
box(ax, 46, 40, 38, 11, 'varie', label=r'$b_3+b_4\sqrt{2}=0$', size='s')
box(ax, 4, 8, 80, 11, 'resultat', label=r'$b_1=b_2=b_3=b_4=0$', size='m')
for x in (23, 65):
    arrow(ax, (x, 68), (x, 51), 'varie')
    arrow(ax, (x, 40), (x, 19), 'resultat')
text(ax, 44, 59.5, r'regrouper par 1 et $\sqrt{3}$', 'varie', 's')
text(ax, 44, 29.5, 'briques libres : tout est nul', 'resultat', 's')
save(fig, '61-106')
