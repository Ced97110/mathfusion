import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
def sym(y, open_right):
    tip, end = (40, 48) if open_right else (48, 40)
    line(ax, [(end, y + 5), (tip, y), (end, y - 5)], 'sujet', lw=2.2)
    line(ax, [(end, y + 5), (end, y - 5)], 'varie', lw=1.2, dash=True)
    tx = 36 if open_right else 52; ox = 56 if open_right else 32
    text(ax, tx, y - 11, 'pointe', 'fixe', 's'); text(ax, ox, y - 11, 'ouvert', 'varie', 's')
    arrow(ax, (tx + (1 if open_right else -1), y - 8), (tip, y - 2), 'fixe', lw=0.7)
    arrow(ax, (ox + (-2 if open_right else 2), y - 8), (end + (1 if open_right else -1), y - 3), 'varie', lw=0.7)
sym(58, True); sym(24, False)
text(ax, 20, 58, '3', 'autre', 'xl'); text(ax, 68, 58, '7', 'sujet', 'xl')
text(ax, 20, 24, '7', 'sujet', 'xl'); text(ax, 68, 24, '3', 'autre', 'xl')
text(ax, 44, 76, 'l’ouverture regarde le 7', 'resultat', 'm')
save(fig, '07-054')
