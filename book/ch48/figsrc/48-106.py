import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
def row(y, n, label):
    w = 6.5
    for i in range(n): box(ax, 2 + i * w, y, w, 7, 'varie', r=0.5)
    for i in range(2): box(ax, 62 + i * 12, y, 12, 7, 'resultat', r=0.5)
    arrow(ax, (3 + n * w, y + 3.5), (60, y + 3.5), 'fixe')
    text(ax, 2, y + 11, label, 'varie', 's', ha='left')
row(58, 6, r'$K=\{0,6\}$ : $G/K$ a 6')
row(36, 4, r'$K=\{0,4,8\}$ : $G/K$ a 4')
text(ax, 74, 72, r'$(G/K)/(H/K)$', 'resultat', 's')
box(ax, 62, 10, 12, 7, 'resultat', r=0.5); box(ax, 74, 10, 12, 7, 'resultat', r=0.5)
text(ax, 2, 13.5, r'$G/H$ : 2, sans $K$', 'resultat', 's', ha='left')
text(ax, 74, 25, r'$=$', 'resultat', 'xl')
save(fig, '48-106')
