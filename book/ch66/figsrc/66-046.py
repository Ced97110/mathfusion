import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 60, r'on remplace $x$ par 3', 'sujet', 'm')
box(ax, 2, 40, 27, 10, 'fixe', label=r'$x^4-1=80$')
box(ax, 31, 40, 39, 10, 'varie', label=r'$\div\ (x^2-1)=8$')
box(ax, 73, 40, 13, 10, 'resultat', label=r'$10$')
arrow(ax, (70, 45), (73, 45), 'varie')
text(ax, 50.5, 54.5, r'$\Phi_1\Phi_2=(x-1)(x+1)$', 'varie', 's')
u = 5.0
x0 = 18.0
box(ax, x0, 14, 9 * u, 10, 'resultat', label=r'$x^2=9$', r=0.5)
box(ax, x0 + 9 * u, 14, 1 * u, 10, 'resultat', label='1', r=0.5)
brace(ax, x0, x0 + 10 * u, 12, 'fixe', label=r'$x^2+1=10$')
arrow(ax, (79, 39), (66, 25.5), 'resultat')
save(fig, '66-046')
