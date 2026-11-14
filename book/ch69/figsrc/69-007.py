import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
labels = ['Partie 1 : corps ordonnés', 'Partie 2 : proches de ℝ', 'Partie 3 : théorème de Sturm', 'Partie 4 : avec des lettres']
for i, lab in enumerate(labels):
    x, y = 2 + 12 * i, 64 - 16 * i
    box(ax, x, y, 46, 10, 'sujet', label=lab, size='s')
    if i < 3:
        arrow(ax, (x + 30, y), (x + 30, y - 6), 'varie')
save(fig, '69-007')
