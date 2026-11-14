import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(cx, cy, r, a0, a1, n=60):
    return [(cx + r * math.cos(a0 + (a1 - a0) * i / n), cy + r * math.sin(a0 + (a1 - a0) * i / n)) for i in range(n + 1)]
fig, ax = canvas(60)
poly(ax, [(6, 34), (30, 34), (36, 48.8), (12, 48.8)], 'sujet')
poly(ax, [(56, 34), (80, 34), (80, 50), (56, 50)], 'fixe')
line(ax, [(56, 38), (60, 38), (60, 34)], 'encre')
text(ax, 18, 31, '6', 'sujet', 's'); text(ax, 4, 41.5, '4', 'sujet', 's')
text(ax, 68, 31, '6', 'fixe', 's'); text(ax, 84, 42, '4', 'fixe', 's')
arrow(ax, (38, 41), (53, 41), 'varie'); text(ax, 46, 46, 'angle droit', 'varie', 's')
text(ax, 21, 24, 'formule nouvelle', 'sujet', 's'); text(ax, 68, 24, 'aire connue', 'fixe', 's')
text(ax, 21, 15, 'doit donner 24', 'resultat'); text(ax, 68, 15, r'$6\times 4 = 24$', 'resultat')
text(ax, 44, 15, r'$=$', 'resultat', 'xl')
save(fig, '29-102')
