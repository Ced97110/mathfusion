import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
disc(ax, 44, 40, 28, 'autre')
disc(ax, 44, 32, 13, 'sujet')
text(ax, 44, 62, '(3) : multiples de 3', 'autre', 's', weight='bold')
for x, y, t in [(24, 46, '3'), (64, 46, '6'), (22, 32, '9'), (66, 32, '15'), (44, 53, '18')]:
    text(ax, x, y, t, 'autre', 'm')
text(ax, 44, 40, '(12)', 'sujet', 's', weight='bold')
text(ax, 44, 32, '12', 'sujet', 'm')
text(ax, 44, 24, '24', 'sujet', 'm')
text(ax, 44, 5, r'$(12)\subseteq(3)$', 'resultat', 'l')
save(fig, '56-082')
