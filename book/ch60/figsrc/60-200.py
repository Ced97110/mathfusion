import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
def bk(cx, cy, w, h, role):
    for sgn in (-1, 1):
        xx = cx + sgn * w
        line(ax, [(xx - sgn * 1.5, cy + h), (xx, cy + h), (xx, cy - h), (xx - sgn * 1.5, cy - h)], role, lw=0.9)
y = 64
text(ax, 8, y, 'A =', 'autre', 'm'); text(ax, 22, y, '0  1\n1  0', 'autre', 'l'); bk(22, y, 8, 5.5, 'autre')
text(ax, 50, y, 'M =', 'sujet', 'm'); text(ax, 64, y, '1  2\n2  1', 'sujet', 'l'); bk(64, y, 8, 5.5, 'sujet')
y = 44
text(ax, 8, y, 'M A', 'encre', 'm'); text(ax, 22, y, '2  1\n1  2', 'resultat', 'l'); bk(22, y, 8, 5.5, 'resultat')
text(ax, 38, y, '=', 'resultat', 'xl', weight='bold')
text(ax, 54, y, 'A M', 'encre', 'm'); text(ax, 68, y, '2  1\n1  2', 'resultat', 'l'); bk(68, y, 8, 5.5, 'resultat')
text(ax, 44, 27, 'M = 1 + 2A, un polynôme en A', 'sujet', 's')
text(ax, 44, 14, 'mais M n’est pas a × 1', 'limite', 's')
save(fig, '60-200')
