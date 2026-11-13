import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 24, 58, 'avant', 'fixe', 'm'); text(ax, 64, 58, 'après', 'fixe', 'm'); text(ax, 44, 58, '+ 0', 'varie', 'l')
for i in range(5):
    y = 48 - 8.5 * i
    r = 'sujet' if i == 3 else 'fixe'
    line(ax, [(27.7, y), (60.3, y)], 'resultat' if i == 3 else 'fixe', lw=1.0 if i == 3 else 0.7)
    disc(ax, 24, y, 3.5, r, label=str(i), size='s')
    disc(ax, 64, y, 3.5, 'resultat' if i == 3 else 'fixe', label=str(i), size='s')
text(ax, 44, 5, '3 + 0 ≡ 3 (mod 5)', 'resultat', 'l')
save(fig, '44-156')
