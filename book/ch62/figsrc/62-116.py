import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
# top : modulo 5, a = 2 = 2^5 is a 5th power, x^5 - 2 = (x-2)^5 splits. bottom : a = t not a square, x^2 + t stays whole
text(ax, 44, 72, r'$a=2$ est une puissance 5 : $x^5-2=(x-2)^5$', 'sujet', 's')
for i in range(5):
    box(ax, 4 + i * 16.6, 52, 15, 11, 'sujet', label=r'$x-2$', size='s')
text(ax, 44, 45, 'le polynôme se casse', 'sujet', 's')
text(ax, 44, 34, r'$a=t$ n’est pas un carré : $x^2+t$', 'autre', 's')
box(ax, 4, 14, 38, 12, 'autre', label=r'$x^2+t$ irréductible', size='s')
arrow(ax, (43, 20), (50, 20), 'limite')
box(ax, 51, 14, 34, 12, 'limite', label=r'$f^{\prime}=0$ : pas parfait', size='s')
save(fig, '62-116')
