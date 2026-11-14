import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arc(ax, c, r, a0, a1, role, lw=0.9):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / 120)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / 120))) for i in range(121)]
    line(ax, pts, role, lw)

T = math.tan(math.radians(40)); u = 1.4
fig, ax = canvas(92)
A = (8, 22); P = lambda d: (A[0] + d * u, A[1])
S1 = (P(20)[0], 22 + 20 * T * u); S2 = (P(50)[0], 22 + 50 * T * u)
line(ax, [A, P(50)], 'sujet', lw=1.6)
line(ax, [P(20), S1], 'varie', lw=1.6); line(ax, [P(50), S2], 'varie', lw=1.6)
line(ax, [A, S2], 'encre', lw=1.0)
arc(ax, A, 12, 0, 40, 'fixe', 1.0)
text(ax, 24, 25.5, '40°', 'fixe', 's')
text(ax, 34, 30, '20 × ?', 'varie', 'm', ha='right')
text(ax, 76, 40, '50 × ?', 'varie', 'm', ha='right')
brace(ax, A[0], P(20)[0], 20, 'sujet', label='20 m')
brace(ax, A[0], P(50)[0], 11, 'sujet', label='50 m')
box(ax, 4, 76, 36, 11, 'autre', label='un seul nombre ?', size='m')
save(fig, '25-012')
