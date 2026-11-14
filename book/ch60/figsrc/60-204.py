import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
def bk(cx, cy, w, h, role):
    for sgn in (-1, 1):
        xx = cx + sgn * w
        line(ax, [(xx - sgn * 1.5, cy + h), (xx, cy + h), (xx, cy - h), (xx - sgn * 1.5, cy - h)], role, lw=0.9)
y = 44
text(ax, 14, y, 'λ  0\n0  λ', 'varie', 'l'); bk(14, y, 7, 5.5, 'varie')
text(ax, 27, y, '−', 'encre', 'xl')
text(ax, 39, y, '3  1\n0  3', 'sujet', 'l'); bk(39, y, 7, 5.5, 'sujet')
text(ax, 52, y, '=', 'encre', 'xl')
for (dx, dy, s, role) in ((-6, 3.2, 'λ − 3', 'varie'), (6, 3.2, '−1', 'fixe'), (-6, -3.2, '0', 'fixe'), (6, -3.2, 'λ − 3', 'varie')):
    text(ax, 72 + dx, y + dy, s, role, 'm')
bk(72, y, 13, 6.5, 'resultat')
text(ax, 14, 31, 'λ1', 'varie', 's')
text(ax, 39, 31, 'A', 'sujet', 's')
text(ax, 72, 31, 'λ1 − A', 'resultat', 's')
text(ax, 44, 19, 'diagonale : λ − 3', 'varie', 's')
text(ax, 44, 11, 'hors diagonale : −1 et 0', 'fixe', 's')
save(fig, '60-204')
