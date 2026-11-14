import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 22, 46, r'$\frac{x^2-4}{x-2}$', 'sujet', 'm'); text(ax, 22, 24, r'$x+2$', 'autre', 's')
text(ax, 47, 54, r'$x=6$', 'encre', 's'); text(ax, 72, 54, r'$x=2$', 'encre', 's')
box(ax, 38, 40, 18, 12, 'resultat', label=r'$\frac{32}{4}=8$', size='s'); box(ax, 61, 40, 22, 12, 'limite', label='bas = 0', size='s')
box(ax, 38, 18, 18, 12, 'resultat', label=r'$8$'); box(ax, 61, 18, 22, 12, 'resultat', label=r'$4$')
text(ax, 47, 35, '=', 'resultat', 'm'); text(ax, 72, 35, r'$\neq$', 'limite', 'm')
text(ax, 44, 8, r'égales, sauf en $x=2$ : on écrit $x\neq2$', 'encre', 's')
save(fig, '21-046')
