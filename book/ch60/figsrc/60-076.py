import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
cx, cy, r = 44, 34, 17
def P(h, rr=r):
    a = math.radians(90 - 30 * h)
    return (cx + rr * math.cos(a), cy + rr * math.sin(a))
text(ax, 2, 70, 'M₂ : premier 2\ntué par 4 = 2²\n(4 × h = 0)', 'sujet', 's', ha='left')
text(ax, 86, 70, 'M₃ : premier 3\ntué par 3 = 3¹\n(3 × h = 0)', 'autre', 's', ha='right')
line(ax, [P(0), P(3), P(6), P(9), P(0)], 'sujet', lw=1.1)
line(ax, [P(0), P(4), P(8), P(0)], 'autre', lw=1.1)
for h in range(12):
    if h == 0:
        disc(ax, *P(h), 2.2, 'resultat')
    elif h % 3 == 0:
        disc(ax, *P(h), 2, 'sujet')
    elif h % 4 == 0:
        disc(ax, *P(h), 2, 'autre')
    else:
        disc(ax, *P(h), 1.2, 'fixe')
text(ax, *P(0, 23), '0', 'resultat', 'm')
for h in (3, 6, 9):
    text(ax, *P(h, 23), str(h), 'sujet', 'm')
for h in (4, 8):
    text(ax, *P(h, 23), str(h), 'autre', 'm')
text(ax, cx, cy, 'ℤ/12', 'fixe', 's')
text(ax, 44, 4, '0 est dans M₂ et dans M₃', 'resultat', 's')
save(fig, '60-076')
