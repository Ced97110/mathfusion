import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
y = 54
text(ax, 40, y, '20', 'fixe', 'l'); text(ax, 48, y, '÷', 'sujet', 'l'); text(ax, 55, y, '2', 'sujet', 'l')
text(ax, 62, y, '=', 'encre', 'l'); text(ax, 70, y, '10', 'resultat', 'l')
for c in range(4):
    for r in range(5):
        box(ax, 8 + 5*c, 12 + 5*r, 5, 5, 'resultat' if r <= c else 'fixe', r=0.2, lw=0.5)
line(ax, [(8,17),(13,17),(13,22),(18,22),(18,27),(23,27),(23,32),(28,32)], 'sujet', lw=2)
text(ax, 40, 36, '20 : tout le rectangle', 'fixe', 's', ha='left')
text(ax, 40, 26, '÷ 2 : en 2 parts égales', 'sujet', 's', ha='left')
text(ax, 40, 16, "10 : une part (l'escalier)", 'resultat', 's', ha='left')
text(ax, 23, 17, '10', 'resultat', 's')
text(ax, 13, 30, '10', 'fixe', 's')
text(ax, 18, 6, '10 + 10 = 20', 'fixe', 's')
save(fig, '01-185')
