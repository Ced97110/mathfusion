import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
h = 10
def sq(cx, cy):
    poly(ax, [(cx-h,cy-h),(cx+h,cy-h),(cx+h,cy+h),(cx-h,cy+h)], 'fixe')
sq(20, 48); sq(68, 48)
line(ax, [(20, 48-h-3), (20, 48+h+3)], 'sujet', lw=1.6)
line(ax, [(68-h-3, 48), (68+h+3, 48)], 'sujet', lw=1.6)
text(ax, 20+6, 48-h-5, r'$rs$', 'sujet', 'l')
text(ax, 68, 48-h-5, r'$r^3s$', 'sujet', 'l')
arrow(ax, (35, 48), (53, 48), 'varie')
text(ax, 44, 53, 'conjuguer', 'varie', 's')
text(ax, 44, 43, 'par une diagonale', 'varie', 's')
x = 2.0
for i, n in enumerate([1, 1, 2, 2, 2]):
    w = 8 if n == 1 else 18
    role = 'sujet' if i == 4 else 'fixe'
    box(ax, x, 6, w, 8, role, label=str(n))
    x += w + 2.5
text(ax, 44, 20, 'la dernière classe : 1 + 1 + 2 + 2 + 2 = 8', 'sujet', 's')
save(fig, '49-278')
