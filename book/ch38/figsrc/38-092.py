import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arc(ax, cx, cy, r, a0, a1, role='varie'):
    pts = [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / 30)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / 30))) for i in range(31)]
    line(ax, pts, role)

fig, ax = canvas(84)
# échelle : 150 m = 55 mm ; AP = 162,8 m -> 59,7 mm ; angle de 51,33°
k = 55 / 150
A = (8.0, 12.0)
B = (A[0] + 150 * k, A[1])
a = math.radians(51.33)
P = (A[0] + 162.8 * k * math.cos(a), A[1] + 162.8 * k * math.sin(a))
line(ax, [A, B], 'fixe', lw=1.2)
arrow(ax, A, P, 'sujet', lw=1.6)
arc(ax, A[0], A[1], 14, 0, 51.33, 'varie')
disc(ax, A[0], A[1], 1.2, 'sujet'); disc(ax, B[0], B[1], 1.0, 'fixe'); disc(ax, P[0], P[1], 1.2, 'resultat')
text(ax, A[0] - 1, A[1] - 4, 'A (origine)', 'sujet', 's', ha='left')
text(ax, B[0], B[1] - 4, 'B', 'fixe', 's')
text(ax, P[0] + 3, P[1] + 2, 'poteau P', 'resultat', 's', ha='left')
text(ax, 21, A[1] + 3.2, r'$51{,}33°$', 'varie', 's', ha='left')
text(ax, 21, 38, r'$162{,}8$ m', 'sujet', 's', ha='right')
text(ax, 40, 78, 'une distance et un angle placent P', 'encre', 'm')
text(ax, 62, 34, r'$(162{,}8\ \mathrm{m}\ ;\ 51{,}33°)$', 'resultat', 's')
save(fig, '38-092')
