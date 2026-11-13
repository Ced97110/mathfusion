import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
x0, x1 = 10, 78
f = numberline(ax, x0, x1, 42, 0, 540, 60, labels=False, arrow_right=False)
g = numberline(ax, x0, x1, 12, 0, 180, 20, labels=False, arrow_right=False)
text(ax, x0, 37, '3θ = 0°', 'fixe', 's'); text(ax, x1, 37, '540°', 'fixe', 's')
text(ax, x0, 7, 'θ = 0°', 'fixe', 's'); text(ax, x1, 7, '180°', 'fixe', 's')
text(ax, 44, 52, 'cos 3θ = 0,5', 'sujet', 'm')
for v, c in ((60, '0,9397'), (300, '−0,1736'), (420, '−0,7660')):
    disc(ax, f(v), 42, 1.4, 'sujet'); disc(ax, g(v / 3), 12, 1.4, 'resultat')
    arrow(ax, (f(v), 40), (f(v), 14), 'varie')
    text(ax, f(v), 46.5, f'{v}°', 'sujet', 's')
    text(ax, g(v / 3) , 17 if False else 7, f'{v // 3}°', 'resultat', 's')
    text(ax, g(v / 3) + (-1.8 if v == 300 else 1.8), 27, c, 'resultat', 's', ha='right' if v == 300 else 'left')
save(fig, '34-186')
