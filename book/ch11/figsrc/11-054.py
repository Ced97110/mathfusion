import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def frac(ax, x, y, top, bot, rt, rb, w=11, size="m", dy=2.8):
    text(ax, x, y + dy, top, rt, size); text(ax, x, y - dy, bot, rb, size); line(ax, [(x - w / 2, y), (x + w / 2, y)], "encre", lw=0.8)
fig, ax = canvas(62)
# left: ordinary fraction 1/12 (one part of twelve)
text(ax, 21, 55, 'fraction ordinaire', 'fixe', 's')
frac(ax, 21, 41, '1', '12', 'fixe', 'fixe', w=8, size='l')
for i in range(12):
    box(ax, 4 + i * 2.8, 20, 2.8, 6, 'varie' if i == 0 else 'fixe', r=0.2, lw=0.5)
text(ax, 21, 14, 'vaut un douzième', 'fixe', 's')
# right: unit factor
text(ax, 66, 55, 'facteur unité', 'sujet', 's')
frac(ax, 66, 41, '1 pied', '12 po', 'sujet', 'autre', w=15, size='l')
box(ax, 50, 22, 33.6, 5, 'sujet', label=None)
text(ax, 66.8, 24.5, 'pied', 'sujet', 's')
for i in range(12):
    box(ax, 50 + i * 2.8, 14, 2.8, 5, 'autre', r=0.2, lw=0.5)
text(ax, 68.2, 16.5, 'po', 'autre', 's')
text(ax, 66, 7, 'même longueur : vaut 1', 'resultat', 's')
save(fig, '11-054')
