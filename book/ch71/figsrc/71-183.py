import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
line(ax, [(4, 8), (84, 8)], 'fixe', lw=0.8)
box(ax, 12, 8, 14, 8, 'sujet', label='16', size='m')
box(ax, 54, 8, 14, 32, 'varie', label='64', size='l')
text(ax, 19, 4, '$u_1$', 'sujet', 's') if False else None
arrow(ax, (12, 52), (24, 52), 'sujet', lw=1.4); text(ax, 18, 57, '$u_1$', 'sujet', 'm')
arrow(ax, (54, 52), (78, 52), 'varie', lw=1.4); text(ax, 66, 57, '$2u_1$', 'varie', 'm')
text(ax, 40, 46, 'vecteur ×2', 'varie', 's')
arrow(ax, (28, 14), (50, 30), 'varie', curve=-0.2)
text(ax, 30, 35, 'coefficient', 'varie', 's'); text(ax, 30, 31.5, '× 4', 'varie', 's')
save(fig, '71-183')
