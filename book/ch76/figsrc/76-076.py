import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
f = numberline(ax, 6, 80, 40, 0, 20, arrow_right=False, labels=False)
g = numberline(ax, 6, 80, 14, 0, 20, arrow_right=False, labels=False)
for v, lab in [(1, r'$e$'), (4, r'$4e$')]:
    disc(ax, f(v), 40, 1.3, 'sujet'); text(ax, f(v), 45, lab, 'sujet', 's')
    arrow(ax, (f(v), 38), (g(5 if v == 1 else 20), 16), 'varie')
for v, lab in [(5, r'$5e$'), (20, r'$20e$')]:
    disc(ax, g(v), 14, 1.3, 'varie'); text(ax, g(v), 8.5, lab, 'varie', 's')
text(ax, 15, 28, r'$\times5$', 'varie', 's'); text(ax, 56, 31, r'$\times5$', 'varie', 's')
text(ax, 44, 52, 'vecteurs de la droite', 'sujet', 's')
text(ax, 60, 3, 'leurs images par $L$', 'varie', 's')
save(fig, '76-076')
