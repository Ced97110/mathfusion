import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(60)
text(ax, 44, 55, r"$a=1$ ; $\vee$ lu $\times$, $\wedge$ lu $+$ mod 2", 'encre', 's')
box(ax, 2, 20, 38, 24, 'resultat', label="$a\\vee a$\n$1\\times1=1$\n$=a$ : vrai", size='m')
box(ax, 48, 20, 38, 24, 'limite', label="$a\\wedge a$\n$1+1=0$\n$\\neq a$ : faux", size='m')
arrow(ax, (40, 32), (48, 32), 'varie')
text(ax, 44, 10, 'le résultat échangé est faux', 'limite', 's')
save(fig, '80-428')
