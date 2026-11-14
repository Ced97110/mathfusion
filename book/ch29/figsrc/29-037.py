import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arc(ax, cx, cy, R, a0, a1, role='sujet', lw=1.0, n=80):
    line(ax, [(cx + R * math.cos(a0 + (a1 - a0) * i / n), cy + R * math.sin(a0 + (a1 - a0) * i / n)) for i in range(n + 1)], role, lw)

def rad(ax, cx, cy, R, a, role='fixe', lw=0.9, r0=0.0):
    line(ax, [(cx + r0 * math.cos(a), cy + r0 * math.sin(a)), (cx + R * math.cos(a), cy + R * math.sin(a))], role, lw)

def pol(cx, cy, R, a):
    return (cx + R * math.cos(a), cy + R * math.sin(a))

fig, ax = canvas(55)
text(ax, 16, 42, '6', 'encre', 'xl')
line(ax, [(9, 36), (23, 36)], 'sujet', 1.6)
text(ax, 16, 30, '3', 'encre', 'xl')
text(ax, 16, 20, '6 divisé par 3', 'sujet', 's')
brace(ax, 40, 82, 44, 'varie', label='6 cm', down=False)
box(ax, 40, 34, 21, 8, 'sujet', label='3 cm')
box(ax, 61, 34, 21, 8, 'sujet', label='3 cm')
text(ax, 61, 22, '6 ÷ 3 = 2', 'resultat', 'l')
text(ax, 61, 15, '3 cm entre 2 fois dans 6 cm', 'encre', 's')
save(fig, '29-037')
