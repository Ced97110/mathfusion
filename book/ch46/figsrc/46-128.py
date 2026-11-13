import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
R = 15
def clock(cx, cy, k, role):
    P = lambda j: (cx + R * math.sin(math.radians(30 * j)), cy + R * math.cos(math.radians(30 * j)))
    vis = sorted({(k * i) % 12 for i in range(12)})
    seq = [(k * i) % 12 for i in range(len(vis) + 1)]
    line(ax, [P(j) for j in seq], role, lw=0.8)
    for j in range(12):
        x, y = P(j)
        if j in vis: disc(ax, x, y, 1.9, role)
        else: disc(ax, x, y, 0.8, 'fixe')
    return vis
clock(22, 38, 5, 'resultat')
clock(66, 38, 4, 'limite')
text(ax, 22, 14, r'$a^5$ : $d$ = 1', 'resultat', 'm')
text(ax, 22, 8, '12 éléments : engendre 𝐺'.replace('𝐺', r'$G$'), 'resultat', 's')
text(ax, 66, 14, r'$a^4$ : $d$ = 4', 'limite', 'm')
text(ax, 66, 8, '3 éléments : n’engendre pas', 'limite', 's')
text(ax, 44, 61, r'$a^k$ engendre $G$ quand $d$ = 1', 'encre', 'm')
save(fig, '46-128')
