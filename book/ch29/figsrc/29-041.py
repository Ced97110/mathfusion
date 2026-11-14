import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arc(ax, cx, cy, R, a0, a1, role='sujet', lw=1.0, n=80):
    line(ax, [(cx + R * math.cos(a0 + (a1 - a0) * i / n), cy + R * math.sin(a0 + (a1 - a0) * i / n)) for i in range(n + 1)], role, lw)

def rad(ax, cx, cy, R, a, role='fixe', lw=0.9, r0=0.0):
    line(ax, [(cx + r0 * math.cos(a), cy + r0 * math.sin(a)), (cx + R * math.cos(a), cy + R * math.sin(a))], role, lw)

def pol(cx, cy, R, a):
    return (cx + R * math.cos(a), cy + R * math.sin(a))

fig, ax = canvas(46)
box(ax, 4, 14, 22, 10, 'autre', label='2 rad')
text(ax, 31, 19, '=', 'encre', 'l')
box(ax, 36, 14, 18, 10, 'autre', label=r'$2^{c}$')
text(ax, 59, 19, '=', 'encre', 'l')
box(ax, 64, 14, 20, 10, 'resultat', label=r'$2$')
text(ax, 15, 9, 'deux radians', 'autre', 's')
text(ax, 45, 9, 'c en exposant', 'autre', 's')
text(ax, 74, 9, 'écriture du livre', 'resultat', 's')
brace(ax, 4, 84, 29, 'fixe', label='même angle : 2 radians', down=False)
save(fig, '29-041')
