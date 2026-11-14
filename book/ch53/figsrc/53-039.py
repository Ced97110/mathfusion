import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
# deux sauts sur la droite 0..29 ; au-delà de 25, on retire 26 : 23+3=26 -> 0 ; 24+5=29 -> 3
x0, x1 = 4.0, 82.0
def band(y):
    f = numberline(ax, x0, x1, y, 0, 29, labels=False, arrow_right=False)
    ax.add_patch(Rectangle((f(0), y - 3.6), f(25.5) - f(0), 2.0, fc=FILL['sujet'], ec=COL['sujet'], lw=0.6, zorder=1))
    ax.add_patch(Rectangle((f(25.5), y - 3.6), f(29) - f(25.5), 2.0, fc=FILL['limite'], ec=COL['limite'], lw=0.6, zorder=1))
    return f
# ligne 1 : 23 + 3 = 26
y1 = 76
text(ax, 44, 91, '23 + 3 = 26', 'encre', 'm', weight='bold')
f = band(y1)
for v in (0, 23, 26): text(ax, f(v), y1 - 7, str(v), 'encre', 's')
arrow(ax, (f(23), y1 + 1.5), (f(26), y1 + 1.5), 'varie', curve=-0.5)
text(ax, f(24.5), y1 + 7.5, '+3', 'varie', 's')
arrow(ax, (f(26), y1 - 9.5), (f(0), y1 - 9.5), 'resultat', curve=0.12)
text(ax, f(13), y1 - 16, 'reste 0 : on revient au début', 'resultat', 's')
# ligne 2 : 24 + 5 = 29
y2 = 30
text(ax, 44, 45, '24 + 5 = 29', 'encre', 'm', weight='bold')
f = band(y2)
for v in (0, 3, 24, 29): text(ax, f(v), y2 - 7, str(v), 'encre', 's')
arrow(ax, (f(24), y2 + 1.5), (f(29), y2 + 1.5), 'varie', curve=-0.4)
text(ax, f(26.5), y2 + 7.5, '+5', 'varie', 's')
arrow(ax, (f(29), y2 - 9.5), (f(3), y2 - 9.5), 'resultat', curve=0.12)
text(ax, f(16), y2 - 16, 'reste 3 : on garde le reste', 'resultat', 's')
text(ax, f(12), y2 + 6.5, '26 cases : 0 à 25', 'sujet', 's')
save(fig, '53-039')
