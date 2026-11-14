import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
y0, s = 40, 5.2
text(ax, 24, 67, 'f : 3 réelles, 2 autres', 'sujet', 'm', weight='bold')
text(ax, 66, 67, 'si 5 réelles', 'limite', 'm', weight='bold')
arrow(ax, (3, y0), (43, y0), 'fixe', lw=0.6)
for v in (-3, -0.11, 3.01):
    disc(ax, 24 + s * v, y0, 1.5, 'fixe')
for sg, lab in ((1, '$r_4$'), (-1, '$r_5$')):
    disc(ax, 24, y0 + sg * 1.734 * 5.2, 1.5, 'varie'); text(ax, 19.5, y0 + sg * 9, lab, 'varie', 's')
arrow(ax, (28, y0 + 7.5), (28, y0 - 7.5), 'varie', both=True)
text(ax, 24, 16, r'$(r_4\ r_5)$ : une transposition', 'resultat', 's')
arrow(ax, (47, y0), (86, y0), 'fixe', lw=0.6)
for i in range(5):
    disc(ax, 53 + i * 8, y0, 1.5, 'fixe')
text(ax, 66, 16, 'identité : rien ne bouge', 'limite', 's')
save(fig, '64-185')
