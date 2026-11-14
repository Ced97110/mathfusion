import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
u = 12
def sq(ox, oy): poly(ax, [(ox, oy), (ox + u, oy), (ox + u, oy + u), (ox, oy + u)], 'sujet')
text(ax, 44, 70, 'sans frottement', 'resultat', 'm')
sq(6, 50); text(ax, 12, 56, 'aire 1', 'sujet', 's')
arrow(ax, (21, 56), (33, 56), 'varie'); text(ax, 27, 60, '2 s', 'varie', 's')
poly(ax, [(36, 50), (48, 50), (72, 62), (60, 62)], 'resultat'); text(ax, 54, 56, 'aire 1', 'resultat', 's')
text(ax, 44, 32, 'avec frottement', 'limite', 'm')
sq(6, 12); text(ax, 12, 18, 'aire 1', 'sujet', 's')
arrow(ax, (21, 18), (33, 18), 'varie'); text(ax, 27, 22, '1 s', 'varie', 's')
line(ax, [(36, 12), (48, 12)], 'limite', lw=2.2); text(ax, 42, 6.5, 'aire 0', 'limite', 's')
save(fig, '75-006')
