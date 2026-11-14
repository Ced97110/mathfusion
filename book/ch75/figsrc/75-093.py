import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
def line_two(y, a, b, name):
    f = numberline(ax, 8, 68, y, 0, 5, arrow_right=True)
    arrow(ax, (f(0), y + 1.5), (f(a), y + 1.5), 'varie', lw=1.0, curve=-0.5)
    arrow(ax, (f(a), y + 1.5), (f(5), y + 1.5), 'sujet', lw=1.0, curve=-0.5)
    text(ax, f(a / 2), y + 9, f'+{a}', 'varie', 's'); text(ax, f((a + 5) / 2), y + 9, f'+{b}', 'sujet', 's')
    disc(ax, f(5), y, 1.6, 'resultat')
    text(ax, 80, y + 3, name, 'encre', 's')
line_two(76, 2, 3, '2 puis 3')
line_two(54, 3, 2, '3 puis 2')
text(ax, 44, 38, 'même résultat : 5 secondes', 'resultat', 'm')
cx, cy = 12, 12
arrow(ax, (cx, cy), (cx + 16, cy), 'sujet', lw=1.3)
arrow(ax, (cx + 22, cy + 8), (cx + 40, cy + 8), 'varie', lw=1.0, curve=0.5)
arrow(ax, (cx + 52, cy), (cx + 52, cy + 16), 'sujet', lw=1.3)
text(ax, cx + 8, cy - 4.5, 'vers la droite', 'sujet', 's'); text(ax, cx + 52, cy - 4.5, 'vers le haut', 'sujet', 's')
text(ax, cx + 31, cy + 19, 'quart de tour', 'varie', 's')
save(fig, '75-093')
