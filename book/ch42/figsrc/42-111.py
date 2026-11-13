import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def lens(cx1, cx2, cy, r):
    a = math.acos((cx2 - cx1) / (2 * r)); n = 24
    right = [(cx1 + r * math.cos(-a + 2 * a * i / n), cy + r * math.sin(-a + 2 * a * i / n)) for i in range(n + 1)]
    left = [(cx2 + r * math.cos(math.pi - a + 2 * a * i / n), cy + r * math.sin(math.pi - a + 2 * a * i / n)) for i in range(n + 1)]
    return right + left
fig, ax = canvas(66)
disc(ax, 30, 38, 18, 'sujet'); disc(ax, 58, 38, 18, 'sujet')
poly(ax, lens(30, 58, 38, 18), 'sujet')
text(ax, 22, 38, 'Sara', 'sujet', 's'); text(ax, 66, 38, 'Max', 'sujet', 's')
text(ax, 44, 42, 'Lina', 'sujet', 's'); text(ax, 44, 34, 'Tom', 'sujet', 's')
text(ax, 24, 61, 'judo', 'fixe', 'm'); text(ax, 64, 61, 'guitare', 'fixe', 'm')
brace(ax, 12, 76, 19, 'sujet', 'union : 4 élèves, chacun 1 fois', down=True)
box(ax, 14, 1, 60, 1, 'sujet') if False else None
save(fig, '42-111')
