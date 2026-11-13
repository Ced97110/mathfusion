import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
cx = [36, 50, 64]
ax.add_patch(Rectangle((57, 9), 14, 38, fc=FILL['varie'], ec='none', zorder=1))
brace(ax, 29, 71, 49, 'sujet', label=r'$n$ = 3 chiffres', down=False)
for y, s, r in [(40, '101', 'sujet'), (28, '011', 'autre'), (14, '110', 'resultat')]:
    for x, d in zip(cx, s): text(ax, x, y, d, r, 'xl')
text(ax, 24, 28, '+', 'encre', 'xl'); line(ax, [(28, 21), (72, 21)], 'encre')
text(ax, 64, 4.5, '1 + 1 = 0', 'varie')
save(fig, '45-170')
