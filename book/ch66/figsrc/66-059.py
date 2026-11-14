import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, 'dimension de ℚ(z) : autorisée ?', 'encre', 'm')
y = 34
f = numberline(ax, 8, 68, y, 0, 5, 1, arrow_right=True)
for v in (1, 2, 4):
    disc(ax, f(v), y, 2.2, 'resultat')
disc(ax, f(3), y, 2.2, 'limite')
text(ax, f(2.5), y + 8, 'vert : dimension 1, 2, 4', 'resultat', 's')
text(ax, f(2.5), y + 13, '(puissances de 2)', 'resultat', 's')
text(ax, f(3), 21, r'$\sqrt[3]{2}$ : dimension 3', 'limite', 's')
box(ax, 22, 3, 44, 9, 'limite', label='π : pas algébrique')
save(fig, '66-059')
