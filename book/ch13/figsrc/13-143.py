import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
y = 34
f = numberline(ax, 14, 74, y, 12, 18, 3, arrow_right=False)
for v, r, t in [(12, 'autre', 'prévu'), (15, 'sujet', 'affiché'), (18, 'autre', 'prévu')]:
    disc(ax, f(v), y, 1.7, r)
    text(ax, f(v), y + 6, t, r, 's')
brace(ax, f(12), f(15) - 0.8, y - 8, 'resultat', label='écart 3')
brace(ax, f(15) + 0.8, f(18), y - 8, 'resultat', label='écart 3')
text(ax, 44, 8, r'$|15-12| = |15-18| = 3$', 'resultat', 'm')
text(ax, f(13.5), y + 12, 'trop bas', 'fixe', 's')
text(ax, f(16.5), y + 12, 'trop haut', 'fixe', 's')
save(fig, '13-143')
