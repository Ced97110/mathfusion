import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
y = 24
f = numberline(ax, 6, 76, y, 0, 24, step=1, labels=False, arrow_right=False, tick=1.0)
for v in (0, 2, 5, 7):
    text(ax, f(v), y - 4, str(v), 'encre', 's')
text(ax, f(24), y - 4, '24', 'encre', 's')
for v in (0, 5, 7, 2):
    line(ax, [(f(v), y + 1.2), (f(v), 42)], 'fixe', lw=0.4, dash=True)
arrow(ax, (f(0), 42), (f(5), 42), 'varie'); text(ax, f(2.5), 44.3, '+5', 'varie', 'm', weight='bold')
arrow(ax, (f(5), 38), (f(7), 38), 'sujet'); text(ax, f(8.3), 38, '+2', 'sujet', 'm', weight='bold')
arrow(ax, (f(7), 34), (f(2), 34), 'varie'); text(ax, f(4.5), 31.5, '−5', 'varie', 'm', weight='bold')
disc(ax, f(2), y, 1.6, 'resultat')
text(ax, 44, 55, r'$5+2-5=2$', 'resultat', 'l')
text(ax, 44, 13, 'abélien : +5 puis −5 s’annule', 'fixe', 's')
text(ax, 44, 6, 'donc tout sous-groupe est normal', 'resultat', 's', weight='bold')
save(fig, '64-037')
