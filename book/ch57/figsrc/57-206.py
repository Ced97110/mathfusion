import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 62, 'n = 6 : 6 × chaque élément = 0 ?', 'encre', 'm')
def clock(cx, cy, k, role, hit, hitrole):
    R = 10
    disc(ax, cx, cy, R, 'fixe', fill=False)
    for j in range(k):
        a = math.radians(90 - 360 * j / k)
        r = hitrole if j == hit else role
        disc(ax, cx + R * math.cos(a), cy + R * math.sin(a), 3.0, r, label=str(j), size='s')
clock(22, 34, 3, 'sujet', 0, 'resultat')
clock(66, 34, 4, 'sujet', 2, 'limite')
text(ax, 22, 18, 'restes modulo 3', 'sujet', 's')
text(ax, 66, 18, 'restes modulo 4', 'sujet', 's')
text(ax, 22, 11, '6 × 1 = 0 : oui', 'resultat', 's')
text(ax, 66, 11, '6 × 1 = 2, pas 0 : non', 'limite', 's')
save(fig, '57-206')
