import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
def bk(cx, cy, w, h, role):
    for sgn in (-1, 1):
        xx = cx + sgn * w
        line(ax, [(xx - sgn * 1.5, cy + h), (xx, cy + h), (xx, cy - h), (xx - sgn * 1.5, cy - h)], role, lw=0.9)
text(ax, 22, 60, 'forme de Jordan', 'sujet', 'm', weight='bold')
text(ax, 66, 60, 'forme rationnelle', 'autre', 'm', weight='bold')
text(ax, 22, 46, '2  1\n0  2', 'sujet', 'l'); bk(22, 46, 8, 6, 'sujet')
for (dx, dy, s) in ((-4.5, 3, '0'), (4.5, 3, '1'), (-4.5, -3, '−4'), (4.5, -3, '4')):
    text(ax, 66 + dx, 46 + dy, s, 'autre', 'l')
bk(66, 46, 8, 7, 'autre')
text(ax, 44, 46, '≠', 'varie', 'xl', weight='bold')
text(ax, 22, 32, 'bloc de Jordan de (λ − 2)²', 'sujet', 's')
text(ax, 66, 32, 'bloc compagnon de (λ − 2)²', 'autre', 's')
text(ax, 22, 24, 'diagonale 2, un 1 au-dessus', 'sujet', 's')
text(ax, 66, 24, 'dernière ligne : −4 et 4', 'autre', 's')
text(ax, 44, 8, 'même matrice, deux écritures', 'encre', 's')
save(fig, '60-189')
