import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(64)
P = {1: (22, 9), 2: (9, 31), 3: (35, 31), 6: (22, 53)}
def seg(a, b, role, r=5.2, curve=0.0):
    (x0, y0), (x1, y1) = P[a], P[b]; d = math.hypot(x1 - x0, y1 - y0); ux, uy = (x1 - x0) / d, (y1 - y0) / d
    arrow(ax, (x0 + ux * r, y0 + uy * r), (x1 - ux * r, y1 - uy * r), role, curve=curve)
seg(1, 2, 'sujet'); seg(2, 6, 'sujet'); seg(1, 3, 'autre'); seg(3, 6, 'autre'); seg(1, 6, 'varie')
for k, (x, y) in P.items(): disc(ax, x, y, 4.6, 'fixe', label=str(k), size='m')
text(ax, 66, 60, 'chemins de 1 à 6', 'encre', 's')
text(ax, 50, 50, r"$1\to6$ : $-1$", 'varie', 'm', ha='left')
text(ax, 50, 40, r"$1\to2\to6$ : $+1$", 'sujet', 'm', ha='left')
text(ax, 50, 30, r"$1\to3\to6$ : $+1$", 'autre', 'm', ha='left')
text(ax, 50, 14, r"$\mu(1,6)=-1+1+1=1$", 'resultat', 's', ha='left')
save(fig, '80-418')
