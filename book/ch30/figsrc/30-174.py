import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
X = lambda t: 10 + t * 70 / (2 * math.pi)
Y = lambda h: 10 + (h - 1.5) * 10
fn = lambda t: 4 + 2.5 * math.sin(t)
n = 200
line(ax, [(X(2 * math.pi * i / n), Y(fn(2 * math.pi * i / n))) for i in range(n + 1)], 'fixe', lw=1.6)
t1 = math.asin(0.4); t2 = math.pi - t1
line(ax, [(X(t1 + (t2 - t1) * i / 60), Y(fn(t1 + (t2 - t1) * i / 60))) for i in range(61)], 'resultat', lw=2.4)
line(ax, [(10, Y(4)), (82, Y(4))], 'fixe', dash=True, lw=0.7)
line(ax, [(10, Y(5)), (82, Y(5))], 'varie', dash=True, lw=1.1)
disc(ax, X(t1), Y(5), 1.3, 'resultat'); disc(ax, X(t2), Y(5), 1.3, 'resultat')
for h in ('6,5', '5', '4', '1,5'):
    text(ax, 5, Y(float(h.replace(',', '.'))), h, 'varie' if h == '5' else 'fixe', 's')
text(ax, 2, 73, 'hauteur (m)', 'fixe', 's', ha='left')
text(ax, 68, Y(5) + 4, 'niveau du bateau', 'varie', 's')
text(ax, 28, Y(4) - 3.5, 'ligne médiane', 'fixe', 's')
text(ax, 28, Y(5) + 4.5, r'$\sin x = 0{,}4$', 'varie', 's')
text(ax, 28, 70, 'eau assez haute', 'resultat', 's')
save(fig, '30-174')
