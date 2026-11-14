import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
w, h = 22, 10
rows = [
    ('sujet', 'homogène : tous de même degré', 54, [r'$x_1^2$', r'$x_1x_2$', r'$x_2^2$'], ['degré 2'] * 3, 'resultat'),
    ('autre', 'pas homogène : degrés différents', 24, [r'$x_1^2$', r'$x_1$'], ['degré 2', 'degré 1'], 'varie'),
]
for role, title, ytop, mons, degs, drole in rows:
    text(ax, 4, ytop, title, role, 'm', ha='left', weight='bold')
    y = ytop - 6 - h
    for i, (m, d) in enumerate(zip(mons, degs)):
        x = 4 + i * (w + 6)
        box(ax, x, y, w, h, role, label=m, size='l')
        text(ax, x + w / 2, y - 4, d, drole, 'm')
save(fig, '55-094')
