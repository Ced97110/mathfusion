import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
h = 2.718 * 7
ay = 34
text(ax, 44, 62, r'$u_1=u_2=1$', 'sujet', 'l')
line(ax, [(6, ay), (82, ay)], 'fixe')
box(ax, 14, ay, 22, h, 'sujet', label=r'$1\cdot e^{1}$')
box(ax, 52, ay - h, 22, h, 'autre', label=r'$-1\cdot e^{1}$')
text(ax, 25, ay + h + 3, '2,718', 'sujet', 's')
text(ax, 63, ay - h - 3, '2,718', 'autre', 's')
text(ax, 44, 5, r'$2{,}718-2{,}718=0$', 'resultat', 'm')
save(fig, '66-133')
