import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 8, 50, r'$f$', 'sujet', 'l')
text(ax, 8, 20, r'$f^{\prime}$', 'resultat', 'l')
tops = [r'$x^3$', r'$-3x$', r'$+1$']
bots = [(r'$3x^2$', 'resultat'), (r'$-3$', 'resultat'), (r'$0$', 'fixe')]
for k in range(3):
    cx = 30 + 22 * k
    box(ax, cx - 9, 44, 18, 12, 'sujet', label=tops[k])
    box(ax, cx - 9, 14, 18, 12, bots[k][1], label=bots[k][0])
    arrow(ax, (cx, 43), (cx, 27), 'varie')
text(ax, 44, 5, 'règle sur les coefficients', 'varie', 's')
save(fig, '69-055')
