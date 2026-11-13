import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arc(ax, c, r, a0, a1, role, lw=0.9):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / 120)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / 120))) for i in range(121)]
    line(ax, pts, role, lw)

T = math.tan(math.radians(40))
fig, ax = canvas(70)
A = (12, 14); g = 50; B = (A[0] + g, 14); S = (B[0], 14 + g * T)
line(ax, [A, B], 'sujet', lw=1.6)
line(ax, [B, S], 'varie', lw=1.6)
line(ax, [A, S], 'fixe', dash=True)
line(ax, [(B[0] - 3, 14), (B[0] - 3, 17), (B[0], 17)], 'fixe', lw=0.7)
arc(ax, A, 10, 0, 40, 'sujet')
disc(ax, A[0], A[1], 1.3, 'fixe'); disc(ax, S[0], S[1], 1.3, 'fixe')
text(ax, 24, 17.5, '40°', 'sujet', 'm')
text(ax, 37, 9, '20 m', 'sujet', 'm')
text(ax, B[0] + 2.5, 34, 'hauteur ?', 'varie', 'm', ha='left')
text(ax, 4, 65, 'connus : 20 m et 40°', 'sujet', 's', ha='left')
text(ax, 4, 60, 'cherché : la hauteur', 'varie', 's', ha='left')
save(fig, '25-001')
