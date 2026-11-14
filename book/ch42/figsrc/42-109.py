import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def lens(cx1, cx2, cy, r):
    a = math.acos((cx2 - cx1) / (2 * r)); n = 24
    right = [(cx1 + r * math.cos(-a + 2 * a * i / n), cy + r * math.sin(-a + 2 * a * i / n)) for i in range(n + 1)]
    left = [(cx2 + r * math.cos(math.pi - a + 2 * a * i / n), cy + r * math.sin(math.pi - a + 2 * a * i / n)) for i in range(n + 1)]
    return right + left
fig, ax = canvas(66)
disc(ax, 30, 38, 18, 'autre'); disc(ax, 58, 38, 18, 'autre')
poly(ax, lens(30, 58, 38, 18), 'sujet')
text(ax, 22, 38, 'Sara', 'autre', 's'); text(ax, 66, 38, 'Max', 'autre', 's')
text(ax, 44, 42, 'Lina', 'sujet', 's'); text(ax, 44, 34, 'Tom', 'sujet', 's')
text(ax, 24, 61, 'judo', 'fixe', 'm'); text(ax, 64, 61, 'guitare', 'fixe', 'm')
box(ax, 2, 4, 40, 9, 'sujet', label='intersection : 2 élèves', size='s')
box(ax, 46, 4, 40, 9, 'autre', label='union : 4 élèves', size='s')
save(fig, '42-109')
