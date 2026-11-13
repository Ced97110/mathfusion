import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 72, r'$x=3$', 'varie', 'l')
box(ax, 14, 56, 60, 10, 'sujet', label=r'$x^4-16=81-16=65$', size='s')
arrow(ax, (44, 56), (44, 50), 'fixe')
text(ax, 44, 44, r'$(x^2+4)(x+2)(x-2)$', 'resultat', 'l')
for xc, a, b in [(18, r'$13$', r'$x^2+4$'), (44, r'$5$', r'$x+2$'), (70, r'$1$', r'$x-2$')]:
    text(ax, xc, 33, b, 'resultat', 's')
    box(ax, xc - 9, 18, 18, 10, 'resultat', label=a)
text(ax, 31, 23, r'$\times$', 'encre'); text(ax, 57, 23, r'$\times$', 'encre')
text(ax, 44, 8, r'$13\times5\times1=65$', 'resultat', 's')
save(fig, '18-092')
