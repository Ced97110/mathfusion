import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def rad(ax, x, y, w, h, role='fixe', lw=1.2):
    sw = 0.45 * h
    line(ax, [(x, y + .5 * h), (x + .2 * sw, y + .6 * h), (x + .55 * sw, y), (x + sw, y + h), (x + sw + w, y + h)], role, lw)
    return x + sw

fig, ax = canvas(66)
text(ax, 44, 60, r'$\sqrt{16}=4$ : le côté', 'sujet', 'm')
box(ax, 12, 18, 32, 32, 'resultat', label='aire 16')
line(ax, [(12, 18), (44, 18)], 'sujet', lw=2.4); line(ax, [(12, 18), (12, 50)], 'sujet', lw=2.4)
text(ax, 28, 12, 'côté 4 m', 'sujet', 's'); text(ax, 6, 34, 'côté 4 m', 'sujet', 's', rot=90)
text(ax, 66, 38, r'$4\times4=16$', 'encre', 'l')
text(ax, 66, 30, 'côté × côté = aire', 'fixe', 's')
save(fig, '22-042')
