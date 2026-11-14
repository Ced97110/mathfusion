import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 22, 58, 'couples d’entiers', 'sujet', 's')
cx, cy = 22, 32
for i in range(-3, 4):
    for j in range(-3, 4):
        if (i, j) != (0, 0):
            disc(ax, cx + 5 * i, cy + 5 * j, 0.9, 'sujet')
disc(ax, cx, cy, 2.2, 'varie', label='0')
disc(ax, 46, 50, 2.0, 'varie')
text(ax, 50, 50, '(0, 0) : torsion', 'varie', 's', ha='left')
disc(ax, 46, 42, 0.9, 'sujet')
text(ax, 50, 42, 'tué par aucun entier ≠ 0', 'sujet', 's', ha='left')
text(ax, 67, 34, r'$M=\mathrm{tor}\,M\oplus L$', 'sujet', 's')
arrow(ax, (67, 30), (67, 22), 'varie')
text(ax, 70, 26, r'$\mathrm{tor}\,M=0$', 'varie', 's', ha='left')
box(ax, 48, 10, 36, 11, 'resultat', label=r'$M=L$ : libre')
save(fig, '60-245')
