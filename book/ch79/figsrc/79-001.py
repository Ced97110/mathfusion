import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
def pair(y, vmin, vmax, a, b, la, lb, cap):
    f = numberline(ax, 8, 78, y, vmin, vmax, step=(vmax - vmin) / 8, labels=False, arrow_right=False)
    disc(ax, f(a), y, 2.6, 'sujet'); disc(ax, f(b), y, 2.6, 'autre')
    text(ax, f(a), y - 6, la, 'sujet', 'm'); text(ax, f(b), y - 6, lb, 'autre', 'm')
    arrow(ax, (f(a) + 3, y + 5), (f(b) - 3, y + 5), 'resultat', curve=0.0)
    text(ax, (f(a) + f(b)) / 2, y + 9, cap, 'resultat', 's')
pair(46, 0, 8, 3.5, 7, '3,5', '7', 'à gauche : 3,5 < 7')
pair(16, 0.15, 0.30, 0.2, 0.25, '0,2', '0,25', 'à gauche : 0,2 < 0,25')
text(ax, 44, 59, 'toute paire se compare', 'encre', 'm')
save(fig, '79-001')
