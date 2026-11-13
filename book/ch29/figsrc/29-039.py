import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arc(ax, cx, cy, R, a0, a1, role='sujet', lw=1.0, n=80):
    line(ax, [(cx + R * math.cos(a0 + (a1 - a0) * i / n), cy + R * math.sin(a0 + (a1 - a0) * i / n)) for i in range(n + 1)], role, lw)

def rad(ax, cx, cy, R, a, role='fixe', lw=0.9, r0=0.0):
    line(ax, [(cx + r0 * math.cos(a), cy + r0 * math.sin(a)), (cx + R * math.cos(a), cy + R * math.sin(a))], role, lw)

def pol(cx, cy, R, a):
    return (cx + R * math.cos(a), cy + R * math.sin(a))

fig, ax = canvas(62)
text(ax, 4, 54, 'en centimètres', 'encre', 's', ha='left')
box(ax, 4, 41, 32, 8, 'varie', label='6 cm'); box(ax, 40, 41, 20, 8, 'fixe', label='3 cm')
text(ax, 72, 45, r'$=2$', 'resultat', 'l')
text(ax, 4, 34, 'en pouces', 'encre', 's', ha='left')
box(ax, 4, 21, 32, 8, 'varie', label='≈ 2,36 pouces'); box(ax, 40, 21, 20, 8, 'fixe', label='≈ 1,18 pouce')
text(ax, 72, 25, r'$=2$', 'resultat', 'l')
text(ax, 44, 8, 'même résultat, sans unité', 'resultat', 's')
save(fig, '29-039')
