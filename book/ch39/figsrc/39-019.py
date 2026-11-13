import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math

def pt(o, r, d):
    return (o[0] + r * math.cos(math.radians(d)), o[1] + r * math.sin(math.radians(d)))

def arc(ax, o, r, d0, d1, role='encre', dash=False):
    line(ax, [pt(o, r, d0 + (d1 - d0) * i / 60) for i in range(61)], role, dash=dash)

fig, ax = canvas(56)
O = (14, 8); R = 32                              # 40 km -> 32 mm
A = pt(O, R, 30); B = pt(O, R, 90)
arc(ax, O, R, 0, 100, 'fixe', dash=True)
arrow(ax, O, (60, 8), 'fixe', lw=0.9)
line(ax, [O, (14, 46)], 'fixe', lw=0.7, dash=True)
line(ax, [O, A], 'sujet', lw=1.8)
line(ax, [O, B], 'autre', lw=1.8)
arc(ax, O, 10, 0, 30, 'sujet'); arc(ax, O, 18, 0, 90, 'autre')
disc(ax, A[0], A[1], 1.6, 'sujet'); disc(ax, B[0], B[1], 1.6, 'autre')
disc(ax, O[0], O[1], 1.3, 'fixe')
text(ax, 11, 5.5, 'O')
text(ax, A[0] + 3, A[1] + 1, r'$(40\ \mathrm{km};\ 30°)$', 'sujet', 's', ha='left')
text(ax, B[0] + 3, B[1] + 1.5, r'$(40\ \mathrm{km};\ 90°)$', 'autre', 's', ha='left')
text(ax, 27, 11.5, '30°', 'sujet', 's')
text(ax, 25, 31, '90°', 'autre', 's')
text(ax, 66, 17, 'même r, autre θ', 'fixe', 's')
save(fig, '39-019')
