import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 16, 48, r'$(a\ ;\ b\ ;\ c)$', 'fixe', 'm')
text(ax, 50, 48, r'$a(b+c)$', 'sujet', 'm'); text(ax, 74, 48, r'$ab+ac$', 'autre', 'm')
for y, tr, v in [(36, '(4 ; 5 ; 2)', '28'), (24, '(2 ; 3 ; 4)', '14'), (12, '(10 ; 0 ; 7)', '70')]:
    box(ax, 3, y - 4.5, 26, 9, 'fixe', label=tr)
    box(ax, 43, y - 4.5, 14, 9, 'sujet', label=v); box(ax, 67, y - 4.5, 14, 9, 'autre', label=v)
    line(ax, [(59.5, y + 1), (64.5, y + 1)], 'resultat', lw=1.3); line(ax, [(59.5, y - 1), (64.5, y - 1)], 'resultat', lw=1.3)
text(ax, 44, 3, 'égal pour tous les choix', 'resultat', 'm')
save(fig, '12-112')
