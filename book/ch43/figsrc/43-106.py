import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
box(ax, 3, 28, 82, 56, 'sujet', fill=False, dash=True)
text(ax, 44, 79, 'classe du nombre 3', 'sujet', 'm')
for x0, lab, kind in ((8, 'pions', 'd'), (34, 'chaises', 's'), (60, 'lettres', 't')):
    box(ax, x0, 36, 20, 34, 'fixe')
    for k in range(3):
        y = 43 + 8 * k
        if kind == 'd': disc(ax, x0 + 10, y, 2.4, 'sujet')
        elif kind == 's': box(ax, x0 + 7.6, y - 2.4, 4.8, 4.8, 'sujet', r=0.3)
        else: poly(ax, [(x0 + 10, y + 2.6), (x0 + 7.4, y - 2), (x0 + 12.6, y - 2)], 'sujet')
    text(ax, x0 + 10, 31.5, lab, 'fixe', 's')
for x in (28.5, 54.5): arrow(ax, (x, 53), (x + 5, 53), 'varie', both=True)
box(ax, 26, 3, 36, 18, 'fixe', dash=True)
for k in range(4): disc(ax, 33 + 7.3 * k, 15, 2.2, 'fixe')
text(ax, 44, 7, '4 éléments : autre classe', 'fixe', 's')
save(fig, '43-106')
