import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
s = 14
def sq(x, y, role, corner):
    box(ax, x, y, s, s, role, r=0.5)
    cx = [x + 3, x + s - 3, x + s - 3, x + 3][corner]; cy = [y + s - 3, y + s - 3, y + 3, y + 3][corner]
    disc(ax, cx, cy, 1.5, 'varie')
text(ax, 44, 78, 'rotation : même face (recto)', 'sujet', 's')
for i in range(4):
    sq(6 + i * 21, 56, 'sujet', i)
brace(ax, 6, 82, 54, 'sujet', label='4 mouvements', down=True)
text(ax, 44, 36, 'retournement : autre face (verso)', 'autre', 's')
for i in range(4):
    sq(6 + i * 21, 14, 'autre', [1, 0, 3, 2][i])
brace(ax, 6, 82, 12, 'autre', label='4 mouvements', down=True)
save(fig, '44-127')
