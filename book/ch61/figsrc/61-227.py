import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
box(ax, 14, 40, 60, 12, 'sujet', label=r'ℚ$(\sqrt{3},\sqrt{5})$ : degré 4')
f = numberline(ax, 14, 66, 22, 1, 4, 1, arrow_right=False)
for v in (1, 2, 4):
    disc(ax, f(v), 22, 3, 'resultat'); text(ax, f(v), 29, 'divise 4', 'resultat', 's')
disc(ax, f(3), 22, 3, 'limite')
text(ax, f(3), 29, r'$\sqrt[3]{2}$ : degré 3', 'limite', 's')
text(ax, f(3), 9, 'ne divise pas 4', 'limite', 's')
save(fig, '61-227')
