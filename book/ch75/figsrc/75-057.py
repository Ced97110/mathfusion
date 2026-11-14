import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
s = 18; ox, oy = 8, 12; sh = 12
poly(ax, [(ox, oy), (ox + s, oy), (ox + s, oy + s), (ox, oy + s)], 'fixe')
poly(ax, [(ox + 36, oy), (ox + 36 + s, oy), (ox + 36 + s + sh, oy + s), (ox + 36 + sh, oy + s)], 'sujet')
for f in (0.5, 1.0):
    arrow(ax, (ox + s * 0.5 + 0.0, oy + s * f), (ox + s * 0.5 + 36 + sh * f, oy + s * f), 'varie')
text(ax, ox + 9, oy - 5, 'avant', 'fixe', 's')
text(ax, ox + 36 + 15, oy - 5, 'après', 'sujet', 's')
arrow(ax, (ox, oy - 9), (ox + 14, oy - 9), 'sujet', lw=1.3)
text(ax, ox + 20, oy - 9, r'$u$', 'sujet', 'm')
text(ax, 44, 50, 'chaque point glisse selon u', 'encre', 'm')
text(ax, 44, 42, r'$c$ règle de combien', 'varie', 'm')
save(fig, '75-057')
