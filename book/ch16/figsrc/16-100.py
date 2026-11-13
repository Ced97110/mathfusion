import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
text(ax, 44, 49, '« 10 de moins que 30 »', 'encre', 'l')
f = numberline(ax, 6, 78, 18, -20, 30, 10, arrow_right=False)
disc(ax, f(30), 18, 1.5, 'sujet')
disc(ax, f(10), 18, 1.5, 'limite')
arrow(ax, (f(30), 21), (f(20), 21), 'resultat', lw=1.2, curve=0.5)
arrow(ax, (f(10), 21), (f(-20), 21), 'limite', lw=1.2, curve=0.35)
text(ax, 70, 33, r'$30 - 10 = 20$', 'resultat', 'm')
text(ax, 28, 38, r'$10 - 30 = -20$', 'limite', 'm')
text(ax, 70, 38.5, 'on part de 30', 'sujet', 's') if False else None
text(ax, 44, 5, 'on part de 30, pas de 10', 'resultat', 's')
save(fig, '16-100')
