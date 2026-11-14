import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arc(ax, c, r, a0, a1, role, lw=0.9):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / 120)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / 120))) for i in range(121)]
    line(ax, pts, role, lw)

T = math.tan(math.radians(40))
fig, ax = canvas(68)
A = (10, 12); g = 48; B = (A[0] + g, 12); S = (B[0], 12 + g * T)
line(ax, [A, B], 'sujet', lw=1.6); line(ax, [B, S], 'fixe', lw=1.6); line(ax, [A, S], 'encre', dash=True)
line(ax, [(B[0] - 3, 12), (B[0] - 3, 15), (B[0], 15)], 'fixe', lw=0.7)
arc(ax, A, 10, 0, 40, 'sujet', 1.2)
arc(ax, S, 9, 220, 270, 'limite', 1.2)
text(ax, 22.5, 15.5, '40°', 'sujet', 'm')
text(ax, 36, 6, 'élévation : depuis le sol', 'sujet', 's', weight='bold')
text(ax, 52.5, 41, '50°', 'limite', 'm')
text(ax, 73, 47, '50° : depuis', 'limite', 's')
text(ax, 73, 43.5, 'la verticale', 'limite', 's')
text(ax, 73, 40, 'pas une élévation', 'limite', 's', weight='bold')
text(ax, 24, 62, '40° + 50° = 90°', 'resultat', 'm')
save(fig, '25-007')
