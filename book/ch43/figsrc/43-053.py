import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)

def mat(ax, cx, cy, v, role='sujet', size='m', dx=3.6, pad=2.4, h=5.4):
    """Matrice 2x2 v=(a,b,c,d) centrée en (cx,cy). Renvoie la demi-largeur."""
    t1 = text(ax, cx - dx, cy, v[0] + '\n' + v[2], role, size); t1.set_linespacing(1.5)
    t2 = text(ax, cx + dx, cy, v[1] + '\n' + v[3], role, size); t2.set_linespacing(1.5)
    hw = dx + pad
    for s in (-1, 1):
        x = cx + s * hw
        line(ax, [(x - s * 1.2, cy + h), (x, cy + h), (x, cy - h), (x - s * 1.2, cy - h)], role, lw=0.9)
    return hw

cx, cy, d = 22, 31, 7
for sx, sy, s in ((-1, 1, '1'), (1, 1, '2'), (-1, -1, '−1'), (1, -1, '1')):
    text(ax, cx + sx * d, cy + sy * 7, s, 'encre', 'l')
for s in (-1, 1):
    x = cx + s * 13
    line(ax, [(x - s * 1.4, cy + 13), (x, cy + 13), (x, cy - 13), (x - s * 1.4, cy - 13)], 'encre', lw=0.9)
arrow(ax, (cx - d + 3, cy + 7 - 3), (cx + d - 3, cy - 7 + 3), 'sujet', lw=1.2)
arrow(ax, (cx + d - 3, cy + 7 - 3), (cx - d + 3, cy - 7 + 3), 'varie', lw=1.2)
text(ax, 65, 54, 'déterminant', 'resultat', 'l')
text(ax, 65, 42, r'$a\times d = 1\times 1 = 1$', 'sujet', 'm')
text(ax, 65, 32, r'$b\times c = 2\times(-1) = -2$', 'varie', 'm')
line(ax, [(44, 26), (86, 26)], 'fixe')
text(ax, 65, 17, r'$ad-bc = 1-(-2) = 3$', 'resultat', 'm')
save(fig, '43-053')
