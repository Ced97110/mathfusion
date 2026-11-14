import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
cx, cy, R = 26, 34, 17
def P(h, r=R): a = math.radians(90 - 90 * h); return (cx + r * math.cos(a), cy + r * math.sin(a))
disc(ax, cx, cy, R, 'fixe')
text(ax, cx, cy, 'n = 4', 'fixe', 'm')
for h in range(4):
    x, y = P(h); disc(ax, x, y, 4, 'resultat' if h == 0 else 'sujet', label=str(h), size='m')
def arc(h0, h1, role):
    a0, a1 = 90 - 90 * h0 - 13, 90 - 90 * h1 + 13
    pts = [(cx + (R + 6) * math.cos(math.radians(a0 + (a1 - a0) * i / 20)), cy + (R + 6) * math.sin(math.radians(a0 + (a1 - a0) * i / 20))) for i in range(21)]
    line(ax, pts, role, lw=1.5); arrow(ax, pts[-2], pts[-1], role, lw=1.5)
arc(3, 4, 'varie'); arc(4, 5, 'varie')
text(ax, 60, 58, '3 + 2 : deux heures', 'varie', 's', ha='left')
text(ax, 60, 50, '3 + 2 = 5', 'encre', 'm', ha='left')
text(ax, 60, 43, '5 dépasse 3 : 5 − 4', 'encre', 's', ha='left')
text(ax, 60, 36, '= 1', 'sujet', 'l', ha='left')
text(ax, 60, 24, '0 : neutre', 'resultat', 's', ha='left')
text(ax, 60, 17, '1 + 3 = 4, compte 0', 'autre', 's', ha='left')
save(fig, '44-139')
