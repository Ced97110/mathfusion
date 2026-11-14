import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
h = 11
def sq(cx, cy):
    poly(ax, [(cx-h,cy-h),(cx+h,cy-h),(cx+h,cy+h),(cx-h,cy+h)], 'fixe')
sq(20, 32); sq(68, 32)
line(ax, [(20-h-3, 32-h-3), (20+h+3, 32+h+3)], 'sujet', lw=1.6)
line(ax, [(68-h-3, 32+h+3), (68+h+3, 32-h-3)], 'sujet', lw=1.6)
text(ax, 20-h-4, 32-h-5, r'$s$', 'sujet', 'l')
text(ax, 68+h+4, 32-h-5, r'$r^2s$', 'sujet', 'l')
arrow(ax, (36, 32), (52, 32), 'varie')
text(ax, 44, 38, 'conjuguer', 'varie', 's')
text(ax, 44, 26, r'par $r$', 'varie', 's')
text(ax, 44, 8, 'même classe : 2 éléments', 'sujet', 'm')
text(ax, 44, 51, 'axes diagonaux du carré', 'fixe', 's')
save(fig, '49-277')
