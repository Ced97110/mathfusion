import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
x0, y0, x1, y1 = 22, 20, 70, 52
box(ax, x0, y0, x1 - x0, y1 - y0, 'sujet', r=0.3)
arrow(ax, (26, y0), (66, y0), 'varie'); arrow(ax, (x1, 24), (x1, 48), 'varie')
arrow(ax, (66, y1), (26, y1), 'varie'); arrow(ax, (x0, 48), (x0, 24), 'varie')
for (x, y, t) in ((x0, y0, '0'), (x1, y0, '12'), (x1, y1, '20'), (x0, y1, '32')):
    disc(ax, x, y, 3.4, 'fixe', label=t, size='s')
text(ax, 46, 15.5, '12 m', 'sujet', 's'); text(ax, 46, 57, '12 m', 'sujet', 's')
text(ax, 19, 36, '8 m', 'sujet', 's', ha='right'); text(ax, 73, 36, '8 m', 'sujet', 's', ha='left')
text(ax, 8, 14, 'départ', 'fixe', 's')
text(ax, 46, 36, r'$12+8+12+8=40$ m', 'resultat', 'm')
save(fig, '11-143')
