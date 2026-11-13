import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(62)
text(ax, 44, 56, '8 × 8 × 8 = 512', 'sujet', 'l')
arrow(ax, (44, 52), (44, 42), 'sujet')
# 512 = 9 blocs de 55 + un reste de 17
for i in range(9):
    box(ax, 6 + 8 * i, 28, 8, 11, 'fixe', label='55', size='s')
x9 = 6 + 8 * 9
ax.add_patch(Rectangle((x9, 28), 8 * 17 / 55, 11, ec=COL['resultat'], fc=FILL['resultat'], lw=0.8, zorder=2))
brace(ax, 6, x9, 28, 'fixe', label='9 × 55 = 495')
text(ax, 80, 46, 'reste 17', 'resultat', 's')
arrow(ax, (80, 44), (x9 + 1.2, 39.8), 'resultat')
box(ax, 26, 4, 36, 10, 'resultat', label='Bob envoie 17')
arrow(ax, (x9 + 1.2, 27), (62.5, 11), 'resultat')
save(fig, '53-130')
