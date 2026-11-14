import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
# p = 5 prime : x^5 - 1 = (x-1)(x^4+x^3+x^2+x+1), second factor irreducible, degree 4
# exponent 4 not prime : x^4 - 1 = (x-1)(x+1)(x^2+1), second factor splits, field degree 2
u = 14.0; x0 = 8
text(ax, 44, 84, r'$p=5$ premier', 'sujet', 'm', weight='bold')
box(ax, x0, 64, u - 1, 12, 'fixe', label=r'$x-1$', size='s')
box(ax, x0 + u, 64, 4 * u - 1, 12, 'sujet', label=r'$x^4+x^3+x^2+x+1$', size='s')
text(ax, x0 + 3 * u, 58, 'irréductible', 'sujet', 's')
box(ax, 14, 44, 60, 9, 'resultat', label=r'corps de degré $p-1=4$', size='s')
text(ax, 44, 36, 'exposant 4, pas premier', 'limite', 'm', weight='bold')
box(ax, x0, 10, u - 1, 11, 'fixe', label=r'$x-1$', size='s')
box(ax, x0 + u, 10, u - 1, 11, 'limite', label=r'$x+1$', size='s')
box(ax, x0 + 2 * u, 10, 2 * u - 1, 11, 'limite', label=r'$x^2+1$', size='s')
brace(ax, x0 + u, x0 + 4 * u - 1, 22.5, 'limite', label=r'$x^3+x^2+x+1$ se casse', down=False)
save(fig, '62-128')
