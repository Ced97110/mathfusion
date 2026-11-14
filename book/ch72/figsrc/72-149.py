import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 22, 66, r'$O(V,B)$', 'sujet', 'l'); text(ax, 66, 66, 'groupe du carré', 'autre', 'm')
cy = 42
disc(ax, 22, cy, 13, 'sujet'); box(ax, 55, cy - 11, 22, 22, 'autre')
for c in (22, 66):
    line(ax, [(c - 16, cy - 4), (c + 16, cy - 4)], 'varie', dash=True)
    arrow(ax, (c + 6, cy + 3), (c - 6, cy + 3), 'varie', curve=0.6)
text(ax, 22, 21, 'conserve la mesure $B$', 'sujet', 's')
text(ax, 66, 21, 'conserve la forme', 'autre', 's')
text(ax, 66, 14, '8 symétries', 'autre', 's')
text(ax, 44, 5, 'même genre : on compose, on défait', 'encre', 's')
save(fig, '72-149')
