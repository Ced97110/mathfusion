import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(56)
def panel(cx, ang, role, name, mark):
    o = (cx, 16); L = 17
    line(ax, [(o[0]-L, o[1]), (o[0]+L, o[1])], 'sujet', lw=1.6)
    a = math.radians(ang)
    line(ax, [(o[0]-L*math.cos(a)*0.0 - 0, o[1])] + [(o[0]+ 26*math.cos(a), o[1]+26*math.sin(a))], role, lw=1.6)
    line(ax, [(o[0]-0, o[1]), (o[0]-0, o[1])], role)
    if mark:
        k = 3.5
        line(ax, [(o[0]+k, o[1]), (o[0]+k, o[1]+k), (o[0], o[1]+k)], 'resultat', lw=0.9)
    text(ax, o[0], 5, name, role if mark else 'fixe', 'l')
panel(22, 60, 'autre', r'$U\oplus W$', False)
panel(66, 90, 'autre', r'$U\perp W$', True)
text(ax, 22, 49, 'angle quelconque', 'fixe', 's')
text(ax, 66, 49, 'angle droit', 'resultat', 's')
text(ax, 38, 21, r'$U$', 'sujet', 'm')
text(ax, 82, 21, r'$U$', 'sujet', 'm')
text(ax, 31, 36, r'$W$', 'autre', 'm')
text(ax, 71, 36, r'$W$', 'autre', 'm')
save(fig, '72-085')
