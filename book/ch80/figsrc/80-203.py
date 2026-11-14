import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def cellrow(ax, y, label, S, role, x0=38, lab_x=35):
    text(ax, lab_x, y + 3.5, label, role if S is not None else "encre", "m", ha="right")
    for i, n in enumerate((1, 2, 3)):
        on = n in S
        box(ax, x0 + i * 9, y, 8, 7, role if on else "fixe", fill=on, dash=not on)

fig, ax = canvas(80)
for i, n in enumerate('123'):
    text(ax, 42 + i * 9, 74, n, 'encre', 'm')
cellrow(ax, 62, r'$A$', {1, 2}, 'sujet')
cellrow(ax, 52, r'$B$', {2, 3}, 'autre')
cellrow(ax, 38, r'$A\wedge B^{\prime}$', {1}, 'varie')
cellrow(ax, 28, r'$A^{\prime}\wedge B$', {3}, 'varie')
cellrow(ax, 12, r'$A+B$', {1, 3}, 'resultat')
text(ax, 68, 41.5, 'action 1', 'varie', 's', ha='left')
text(ax, 68, 31.5, 'action 2', 'varie', 's', ha='left')
text(ax, 68, 15.5, r'action 3 : $\vee$', 'resultat', 's', ha='left')
arrow(ax, (50, 26), (50, 20), 'resultat') if False else None
save(fig, '80-203')
