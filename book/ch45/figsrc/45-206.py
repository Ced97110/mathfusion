import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
def group(x0, y0, w, h, elems, role, title):
    box(ax, x0, y0, w, h, role)
    n = len(elems); 
    for i, e in enumerate(elems):
        disc(ax, x0 + w * (i + 0.5) / n, y0 + h / 2, 3.0, role, label=str(e), size='s')
    text(ax, x0 + w / 2, y0 + h + 3, title, role, 'm', weight='bold')
group(3, 36, 24, 10, [0, 2, 4], 'sujet', 'H')
group(3, 10, 16, 10, [0, 3], 'autre', 'K')
box(ax, 44, 20, 41, 20, 'resultat')
els = [0, 3, 2, 5, 4, 1]
for i, e in enumerate(els):
    disc(ax, 49 + (i % 3) * 13, 34 - (i // 3) * 9, 3.6, 'resultat', label=str(e), size='s')
text(ax, 64.5, 44, 'HK', 'resultat', 'l', weight='bold')
arrow(ax, (28, 41), (43, 33), 'varie'); arrow(ax, (20, 15), (43, 26), 'varie')
text(ax, 36, 28, 'h + k', 'varie', 's') if False else None
text(ax, 64.5, 14, 'six sommes : une collection', 'resultat', 's') if False else None
text(ax, 64.5, 14, 'six sommes h + k', 'resultat', 's')
save(fig, '45-206')
