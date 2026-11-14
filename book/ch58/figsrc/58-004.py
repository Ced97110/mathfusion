import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
# 3 (2, 1) = (6, 3) : trois copies de la vente (2, 1)
text(ax, 44, 52, r'$3\,(2,\ 1) = (6,\ 3)$', 'varie', 'xl', weight='bold')
s, g = 5.5, 1.0                 # côté d'un carré, écart
gw = 2 * s + g                  # largeur d'un groupe de riz
gap = 5.0
x0 = (88 - (3 * gw + 2 * gap)) / 2 + 8
yr, yl = 26, 17
text(ax, 2, yr + s / 2, 'riz', 'sujet', 's', ha='left')
text(ax, 2, yl + s / 2, 'lentilles', 'autre', 's', ha='left')
for k in range(3):
    gx = x0 + k * (gw + gap)
    box(ax, gx - 2, yl - 3.5, gw + 4, 22, 'varie', fill=False, dash=True, lw=0.6)
    text(ax, gx + gw / 2, 42, '(2, 1)', 'varie', 's')
    for i in range(2):
        box(ax, gx + i * (s + g), yr, s, s, 'sujet', r=0.4)
    box(ax, gx, yl, s, s, 'autre', r=0.4)
text(ax, x0 + 3 * gw + 2 * gap + 4, yr + s / 2, '6', 'sujet', 'l', ha='left', weight='bold')
text(ax, x0 + 3 * gw + 2 * gap + 4, yl + s / 2, '3', 'autre', 'l', ha='left', weight='bold')
text(ax, 44, 8, 'chaque case est multipliée par 3', 'encre', 's')
save(fig, '58-004')
