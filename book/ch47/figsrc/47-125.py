import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 74, 'écrit de gauche à droite', 'fixe', 's')
arrow(ax, (6, 68), (82, 68), 'fixe')
for x, lab, role, cap in [(8, 'g⁻¹', 'varie', 'enfin : défaire g'), (34, 'n', 'sujet', 'ensuite : n'), (60, 'g', 'varie', 'd’abord : g')]:
    box(ax, x, 46, 20, 14, role, label=lab, size='l')
    text(ax, x + 10, 40, cap, role, 's')
arrow(ax, (80, 34), (8, 34), 'varie')
text(ax, 44, 28, 'calcul de droite à gauche', 'varie', 's')
text(ax, 44, 12, 'avec + : −g + n + g = n', 'resultat', 'm')
save(fig, '47-125')
