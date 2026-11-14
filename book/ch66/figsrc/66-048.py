import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 62, r'on remplace $x$ par 3', 'sujet', 'm')
box(ax, 2, 42, 27, 10, 'fixe', label=r'$x^6-1=728$')
box(ax, 31, 42, 40, 10, 'varie', label=r'$\div\ (2\times4\times13)=104$')
box(ax, 74, 42, 12, 10, 'resultat', label='7')
arrow(ax, (71, 47), (74, 47), 'varie')
text(ax, 51, 56, r'$\Phi_1\,\Phi_2\,\Phi_3$', 'varie', 's')
terms = [(r'$x^2$' + '\n9', 'resultat'), (r'$-x$' + '\n−3', 'varie'), ('$+1$\n1', 'resultat')]
for i, (t, role) in enumerate(terms):
    box(ax, 10 + i * 22, 12, 18, 16, role, label=t)
box(ax, 76, 12, 10, 16, 'resultat', label='7')
text(ax, 74, 20, '=', 'encre', 'l')
text(ax, 44, 6, r'coefficients : 1, $-1$, 1', 'fixe', 's')
arrow(ax, (80, 41), (81, 29.5), 'resultat')
save(fig, '66-048')
