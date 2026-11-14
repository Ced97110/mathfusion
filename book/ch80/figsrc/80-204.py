import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def cellrow(ax, y, label, S, role, x0=38, lab_x=35):
    text(ax, lab_x, y + 3.5, label, role if S is not None else "encre", "m", ha="right")
    for i, n in enumerate((1, 2, 3)):
        on = n in S
        box(ax, x0 + i * 9, y, 8, 7, role if on else "fixe", fill=on, dash=not on)

fig, ax = canvas(82)
for i, n in enumerate('123'):
    text(ax, 42 + i * 9, 77, n, 'encre', 'm')
cellrow(ax, 64, r'$A$', {1, 2}, 'sujet')
cellrow(ax, 54, r'$B$', {2, 3}, 'autre')
cellrow(ax, 44, r'$AB$', {2}, 'resultat')
text(ax, 68, 47.5, 'commun : 2', 'resultat', 's', ha='left')
line(ax, [(4, 40), (84, 40)], 'fixe', dash=True)
cellrow(ax, 28, r'$A$', {1}, 'sujet')
cellrow(ax, 18, r'$B$', {3}, 'autre')
cellrow(ax, 8, r'$AB$', set(), 'resultat')
text(ax, 68, 11.5, 'vide', 'resultat', 's', ha='left')
save(fig, '80-204')
