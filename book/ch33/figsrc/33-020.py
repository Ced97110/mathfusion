import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
for y, a, b, f in ((46, '30°', '0,5', 'sinus'), (16, '4', '16', 'carré')):
    disc(ax, 14, y, 6, 'sujet', label=a)
    disc(ax, 74, y, 6, 'resultat', label=b)
    arrow(ax, (19.2, y + 3), (68.8, y + 3), 'sujet')
    arrow(ax, (68.8, y - 3), (19.2, y - 3), 'varie')
    text(ax, 44, y + 6.5, f, 'sujet', 's')
    text(ax, 44, y - 6.5, 'réciproque', 'varie', 's')
save(fig, '33-020')
