import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
c = 3.0
def grid(x0, y0, cols, rows, role):
    for i in range(cols):
        for j in range(rows):
            box(ax, x0 + i * c, y0 + j * c, c, c, role, r=0.3, lw=0.5)
grid(6, 20, 8, 4, 'sujet')
grid(60, 14, 4, 8, 'autre')
text(ax, 18, 46, r'4 · 8 = 32', 'sujet', 'l')
text(ax, 66, 46, r'8 · 4 = 32', 'autre', 'l')
text(ax, 44.5, 26, '=', 'resultat', 'l', weight='bold')
text(ax, 18, 8, '4 rangées de 8', 'sujet', 's')
text(ax, 66, 8, '8 rangées de 4', 'autre', 's')
save(fig, '12-097')
