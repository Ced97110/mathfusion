import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
def bk(cx, cy, w, h, role):
    for sgn in (-1, 1):
        xx = cx + sgn * w
        line(ax, [(xx - sgn * 1.5, cy + h), (xx, cy + h), (xx, cy - h), (xx - sgn * 1.5, cy - h)], role, lw=0.9)
text(ax, 44, 54, 'UA = AU donne b = c et a = d', 'encre', 's')
y = 34
text(ax, 12, y, 'a  b\nb  a', 'sujet', 'l'); bk(12, y, 8, 5.5, 'sujet')
text(ax, 25, y, '=', 'encre', 'l')
text(ax, 33, y, 'a ×', 'varie', 'm')
text(ax, 45, y, '1  0\n0  1', 'fixe', 'l'); bk(45, y, 8, 5.5, 'fixe')
text(ax, 58, y, '+', 'encre', 'l')
text(ax, 65, y, 'b ×', 'varie', 'm')
text(ax, 77, y, '0  1\n1  0', 'autre', 'l'); bk(77, y, 8, 5.5, 'autre')
text(ax, 12, 22, 'U', 'sujet', 's')
text(ax, 45, 22, 'identité', 'fixe', 's')
text(ax, 77, 22, 'A', 'autre', 's')
text(ax, 44, 10, 'dimension 2 = degré de f', 'resultat', 's')
save(fig, '60-198')
