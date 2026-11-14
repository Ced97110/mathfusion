import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, r'degré 2 : un bloc ou deux blocs ?', 'encre', 'm')
x0 = 24
box(ax, x0, 42, 40, 10, 'sujet', label=r'$x^2-2$')
text(ax, 44, 37, r's’annule en $\sqrt{2}$ ; un seul bloc', 'sujet', 's')
text(ax, 44, 32, 'ne se casse pas : minimal', 'resultat', 's', weight='bold')
line(ax, [(4, 27), (84, 27)], 'fixe', lw=0.5, dash=True)
box(ax, x0, 11, 20, 10, 'fixe', label=r'$x-1$')
box(ax, x0 + 20, 11, 20, 10, 'fixe', label=r'$x+1$')
text(ax, 44, 6, r'$x^2-1$ se casse en deux blocs', 'fixe', 's')
text(ax, 44, 23, 'un bloc plus petit existe', 'fixe', 's')
save(fig, '66-051')
