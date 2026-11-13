import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, r'$F$ : 3 notes ; $S$ : 2 élèves', 'encre', 'm')
x0, y0, c = 30, 8, 9
for i in range(3):
    for j in range(3):
        role = 'varie' if (i, j) == (1, 2) else 'sujet'
        box(ax, x0 + i * c, y0 + j * c, c, c, role, r=0.3)
for k in range(3):
    text(ax, x0 + k * c + c / 2, y0 + 3 * c + 3, str(k), 'encre', 's')
    text(ax, x0 - 3, y0 + k * c + c / 2, str(k), 'encre', 's')
text(ax, x0 + 13.5, y0 + 3 * c + 9, 'note de Bob', 'encre', 's')
text(ax, 11, y0 + 13.5, 'note\nd’Ana', 'encre', 's')
text(ax, 73, 28, r'$F^S$ : $3^2$', 'sujet', 'l')
text(ax, 73, 20, '= 9', 'resultat', 'l')
text(ax, 44, 3.5, 'une case = une distribution', 'encre', 's')
save(fig, '55-031')
