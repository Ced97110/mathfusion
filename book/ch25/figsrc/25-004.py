import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arc(ax, c, r, a0, a1, role, lw=0.9):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / 120)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / 120))) for i in range(121)]
    line(ax, pts, role, lw)

fig, ax = canvas(60)
text(ax, 30, 38, '40', 'sujet', 34, weight='bold')
text(ax, 45, 44, '°', 'varie', 34, weight='bold')
brace(ax, 21, 38, 28, 'sujet', label='nombre de parts')
brace(ax, 41, 49, 52, 'varie', label='degré', down=False)
text(ax, 44, 14, 'se lit : quarante degrés', 'encre', 's')
text(ax, 44, 7, '360° : le tour complet', 'fixe', 's')
save(fig, '25-004')
