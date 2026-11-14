import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
def grid(x0, cols, rows, hl=()):
    box(ax, x0 - 2, 42 - (rows - 1) * 6 - 2, cols * 6 + 3, rows * 6 + 3, 'fixe', fill=False, r=0.8)
    for n in range(cols * rows):
        c, r = n % cols, n // cols
        box(ax, x0 + c * 6, 42 - r * 6, 5, 5, 'sujet' if n in hl else 'fixe', r=0.3)
grid(8, 2, 3); grid(38, 6, 4, hl=(3, 8, 15, 20))
text(ax, 14, 50, r'$S_3$ : 6', 'sujet', 'l'); text(ax, 56, 50, r'$S_4$ : 24', 'sujet', 'l')
text(ax, 14, 23, '3 objets', 'fixe', 's'); text(ax, 56, 15.5, '4 objets', 'fixe', 's')
text(ax, 56, 8, "4 = copie de l'horloge", 'sujet', 's')
save(fig, '45-092')
