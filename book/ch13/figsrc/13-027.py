import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
y = 14
f = numberline(ax, 8, 64, y, 0, 7, every=7)
box(ax, f(7) - 22, 34, 12, 9, 'sujet', label='7', size='l')
box(ax, f(7) + 10, 34, 12, 9, 'sujet', label='+7', size='l')
text(ax, f(7), 38.5, '=', 'resultat', 'xl', weight='bold')
arrow(ax, (f(7) - 16, 33.5), (f(7) - 1, y + 2.5), 'sujet')
arrow(ax, (f(7) + 16, 33.5), (f(7) + 1, y + 2.5), 'sujet')
disc(ax, f(7), y, 1.8, 'resultat'); disc(ax, f(0), y, 1.3, 'fixe')
brace(ax, f(0), f(7), y - 6, 'sujet', '7 pas à droite de 0')
text(ax, f(7), 48, 'deux écritures, un point', 'encre', 's')
save(fig, '13-027')
