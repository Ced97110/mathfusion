import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 4, 64, 'droite des nombres', 'fixe', 'm', ha='left')
f = numberline(ax, 8, 70, 50, 1, 4, arrow_right=True)
for v in (1, 2, 3): arrow(ax, (f(v), 53), (f(v + 1), 53), 'varie', curve=-0.5)
text(ax, f(1.5), 60, '+ 1', 'varie', 'm')
text(ax, 4, 34, 'droite logarithmique', 'sujet', 'm', ha='left')
g = numberline(ax, 8, 70, 20, 0, 3, labels=False, role='sujet', arrow_right=True)
for i, s in enumerate(['1', '10', '100', '1 000']):
    text(ax, g(i), 15.5, s, 'sujet', 's')
for v in (0, 1, 2): arrow(ax, (g(v), 23), (g(v + 1), 23), 'varie', curve=-0.5)
text(ax, g(0.5), 30, '$\\times$ 10', 'varie', 'm')
save(fig, '14-081')
