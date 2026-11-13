import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
u = 76 / 394; x0 = 6
text(ax, 44, 55, r'$r^2 + p^2 = 394$', 'sujet', 'm')
box(ax, x0, 40, 169 * u, 8, 'sujet', label='r² = 169', size='s'); box(ax, x0 + 169 * u, 40, 225 * u, 8, 'sujet', label='p² = 225', size='s')
box(ax, x0, 18, 196 * u, 8, 'resultat', label=r'$(x+y)^2$ = 196', size='s')
box(ax, x0 + 196 * u, 18, 198 * u, 8, 'varie', label='− 198', size='s', dash=True)
line(ax, [(x0 + 196 * u, 14), (x0 + 196 * u, 28)], 'fixe', dash=True); line(ax, [(x0 + 196 * u, 35), (x0 + 196 * u, 44)], 'fixe', dash=True)
text(ax, 44, 31.5, 'angle A + B aigu : on retire de r² + p²', 'varie', 's')
text(ax, 44, 9, r'$-\,2rp\cos(A+B) = -198$', 'varie', 'm')
save(fig, '34-056')
