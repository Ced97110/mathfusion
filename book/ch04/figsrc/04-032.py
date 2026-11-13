import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 64, r"$A$ : l'aire, en carreaux", 'sujet', 'l')
# le même signe appliqué à trois figures
arrow(ax, (40, 60.5), (12, 36), 'sujet')
arrow(ax, (44, 60.5), (36, 40), 'sujet')
arrow(ax, (48, 60.5), (68, 28), 'sujet')
# premier sol : carré de 4 × 4
for i in range(4):
    for j in range(4):
        box(ax, 4 + 4*i, 18 + 4*j, 4, 4, 'fixe', r=0.1)
text(ax, 12, 12, r'$A$ = 16', 'varie', 'm')
# second sol : carré de 5 × 5
for i in range(5):
    for j in range(5):
        box(ax, 26 + 4*i, 18 + 4*j, 4, 4, 'fixe', r=0.1)
text(ax, 36, 12, r'$A$ = 25', 'varie', 'm')
# rectangle : 2 rangées × 8 colonnes
for i in range(8):
    for j in range(2):
        box(ax, 52 + 4*i, 18 + 4*j, 4, 4, 'limite', r=0.1)
text(ax, 68, 12, r'$A$ = 16', 'limite', 'm')
text(ax, 68, 5, 'A ne dit pas la forme', 'limite', 's')
save(fig, '04-032')
