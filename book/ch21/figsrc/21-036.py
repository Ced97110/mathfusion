import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 44, 52, r'valeurs interdites de $\frac{1}{x-2}$', 'sujet', 'm')
for i, (lab, role) in enumerate([(r'$Q=0$', 'sujet'), (r'$x-2=0$', 'varie'), (r'$x=2$', 'resultat')]):
    box(ax, 4 + 30 * i, 28, 22, 12, role, label=lab)
arrow(ax, (26, 34), (34, 34), 'fixe'); arrow(ax, (56, 34), (64, 34), 'varie')
text(ax, 60, 22.5, r'$+2$ des deux côtés', 'varie', 's')
text(ax, 15, 22.5, r'$Q=x-2$', 'sujet', 's')
box(ax, 14, 4, 60, 10, 'resultat', label=r"$x$ seul : on s'arrête", size='s')
save(fig, '21-036')
