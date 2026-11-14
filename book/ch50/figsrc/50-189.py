import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
text(ax, 44, 72, r'$H = \{0, 3, 6, 9\}$', 'sujet', 'm')
text(ax, 44, 64, r'$K = \{0, 2, 4, 6, 8, 10\}$', 'autre', 'm')
def clock(cx, cy, hi, role):
    for k in range(12):
        a = math.pi / 2 - math.pi * k / 6
        disc(ax, cx + 9 * math.cos(a), cy + 9 * math.sin(a), 1.5, role if k in hi else 'fixe', fill=k in hi)
H = {0, 3, 6, 9}; K = {0, 2, 4, 6, 8, 10}
clock(15, 38, H | K, 'autre'); clock(73, 38, set(range(12)), 'sujet')
for i in range(4):
    for j in range(6): disc(ax, 44 - 8 + j * 3.2, 38 + 4.8 - i * 3.2, 1.2, 'fixe')
text(ax, 15, 54, r'$H \cup K$', 'autre', 'm'); text(ax, 44, 54, r'couples $(h, k)$', 'fixe', 'm'); text(ax, 73, 54, r'$HK$', 'sujet', 'm')
text(ax, 15, 20, '8 éléments', 'autre', 's'); text(ax, 44, 20, '24 couples', 'fixe', 's'); text(ax, 73, 20, '12 sommes', 'sujet', 's')
text(ax, 44, 8, 'horloge à 12 heures', 'fixe', 's')
save(fig, '50-189')
