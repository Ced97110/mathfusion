import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
cy = 27
text(ax, 21, 49, 'extension algébrique', 'fixe', 's')
disc(ax, 21, cy, 14, 'resultat', label='ℂ', size='l')
text(ax, 21, 6, 'E = ℂ', 'resultat', 'm')
text(ax, 65, 52, 'ℂ(x)', 'limite', 'm')
disc(ax, 65, cy, 18, 'limite')
disc(ax, 65, cy, 9, 'sujet', label='ℂ', size='l')
text(ax, 65, cy + 13.5, r'$x$', 'limite', 'l')
text(ax, 65, 3.5, 'non algébrique', 'limite', 's')
save(fig, '61-143')
