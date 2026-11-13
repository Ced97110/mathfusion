import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
x0, cw = 14, 15
text(ax, 14, 66, r'$N = \frac{1}{2}$ : 2 quarts', 'sujet', 'm', ha='left')
for i in range(4):
    box(ax, x0 + i * cw, 50, cw, 9, 'sujet' if i < 2 else 'fixe', fill=i < 2, r=0.2)
text(ax, 14, 41, r'$M = \frac{3}{4}$ : 3 quarts', 'autre', 'm', ha='left')
for i in range(3):
    box(ax, x0 + i * cw, 28, cw, 9, 'resultat' if i < 2 else 'limite', fill=i < 2, r=0.2, dash=i == 2)
text(ax, x0 + 2.5 * cw, 32.5, 'hors N', 'limite', 's')
line(ax, [(x0 + 2 * cw, 61), (x0 + 2 * cw, 47)], 'fixe', dash=True)
brace(ax, x0 + 1, x0 + 2 * cw - 1, 26, 'resultat', label='2 parts de M sur 3')
text(ax, 44, 8, r'$M$ tient $\frac{2}{3}$ de fois dans $N$', 'resultat', 'm', weight='bold')
save(fig, '07-067')
