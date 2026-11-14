import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 75, r"$K=\ker f$ : positions distinctes", 'resultat', 's')
for x, lab, pos in [(8, r"paquet $1K$", '1'), (52, r"paquet $2K$", '2')]:
    box(ax, x, 52, 28, 10, 'sujet', label=lab, size='s')
    arrow(ax, (x + 14, 52), (x + 14, 45), 'resultat')
    disc(ax, x + 14, 40, 4, 'resultat', label=pos, size='s')
text(ax, 44, 31, r"$L$ = multiples de 8 : même position", 'limite', 's')
box(ax, 4, 14, 26, 10, 'limite', label=r"$1+8$ℤ", size='s'); box(ax, 58, 14, 26, 10, 'limite', label=r"$5+8$ℤ", size='s')
arrow(ax, (17, 14), (41, 9.5), 'limite'); arrow(ax, (71, 14), (47, 9.5), 'limite')
disc(ax, 44, 6, 3.6, 'limite', label='1', size='s')
save(fig, '48-080')
