import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 22, 64, r'$\exists\,y,\ y^2=x$', 'sujet', 'l')
box(ax, 2, 44, 40, 10, 'resultat', label=r'$x=9$ : $y=3$', size='s')
box(ax, 2, 28, 40, 10, 'limite', label=r'$x=-1$ : aucun $y$', size='s')
text(ax, 22, 16, 'un seul suffit', 'sujet', 's')
text(ax, 66, 64, r'$\forall x,\ x^2\geq0$', 'autre', 'l')
for i, lab in enumerate([r'$3^2\geq0$', r'$(-2)^2\geq0$', r'$0^2\geq0$']):
    box(ax, 46, 50 - i * 12, 40, 9, 'resultat', label=lab, size='s')
text(ax, 66, 16, 'tous doivent convenir', 'autre', 's')
save(fig, '70-077')
