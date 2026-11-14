import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 22, 76, 'chapitre 24', 'sujet', 'm', weight='bold')
text(ax, 66, 76, 'déterminant', 'autre', 'm', weight='bold')
# left : subtract the two lines
box(ax, 4, 62, 36, 8, 'sujet', label=r'$y=2x+1$', size='s')
box(ax, 4, 51, 36, 8, 'sujet', label=r'$y=3x+4$', size='s')
arrow(ax, (22, 51), (22, 42), 'varie')
text(ax, 25, 46.5, 'soustraire', 'varie', 's', ha='left')
box(ax, 4, 33, 36, 8, 'varie', label=r'$x+3=0$', size='s')
# right : the same two lines as polynomials in y, and the determinant
box(ax, 48, 62, 36, 8, 'autre', label=r'$y-2x-1$', size='s')
box(ax, 48, 51, 36, 8, 'autre', label=r'$y-3x-4$', size='s')
arrow(ax, (66, 51), (66, 42), 'varie')
text(ax, 69, 46.5, r'$a_1b_0-a_0b_1$', 'varie', 's', ha='left')
box(ax, 48, 33, 36, 8, 'varie', label=r'$-x-3=0$', size='s')
# both give the same position
f = numberline(ax, 24, 64, 14, -5, -1, step=1, role='fixe', arrow_right=False)
arrow(ax, (22, 33), (f(-3) - 2, 17.5), 'resultat')
arrow(ax, (66, 33), (f(-3) + 2, 17.5), 'resultat')
disc(ax, f(-3), 14, 1.3, 'resultat')
text(ax, 44, 4, 'même solution : $x=-3$', 'resultat', 's')
save(fig, '70-023')
