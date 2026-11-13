import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(55)
cy = 26
poly(ax, [(6, cy - 7), (22, cy - 7), (14, cy + 7)], 'sujet'); text(ax, 14, cy - 11, 'triangle', 'sujet', 's')
box(ax, 26, cy - 5, 20, 10, 'sujet', r=0.1); text(ax, 36, cy - 11, 'rectangle', 'sujet', 's')
poly(ax, [(52, cy - 6), (64, cy - 6), (64, cy + 6), (52, cy + 6)], 'sujet'); text(ax, 58, cy - 11, 'carré', 'sujet', 's')
poly(ax, [(68, cy - 6), (80, cy - 6), (76, cy + 6), (71, cy + 6)], 'sujet'); text(ax, 74, cy - 11, 'trapèze', 'sujet', 's')
text(ax, 44, 45, 'bord fermé, côtés droits', 'sujet', 'm')
save(fig, '11-074')
