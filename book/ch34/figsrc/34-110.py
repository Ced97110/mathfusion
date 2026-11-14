import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
rows = [(50, 'angles doubles', 'fixe', '$\\cos A$', '$\\cos 2A$', ''),
        (32, 'réduction des puissances', 'sujet', '$\\cos 2A$', '$\\cos^2 A$', 'sans √ ni ±'),
        (14, 'demi-angle', 'fixe', '$\\cos\\theta$', '$\\cos(\\theta/2)$', 'avec √ et ±')]
for y, name, r, a, b, note in rows:
    text(ax, 6, y + 14, name, r, 's', ha='left', weight='bold' if r == 'sujet' else 'normal')
    box(ax, 6, y, 28, 10, r, label=a); box(ax, 54, y, 28, 10, r, label=b)
    arrow(ax, (35, y + 5), (53, y + 5), 'varie')
    if note: text(ax, 44, y + 1.2, note, 'varie', 's')
save(fig, '34-110')
