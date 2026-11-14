import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
X = lambda x: 12 + x * 8
Y = lambda y: 8 + y * 8
for i in range(0, 5):
    for j in range(0, 6):
        disc(ax, X(i), Y(j), 0.5, 'fixe')
o, q = (X(0), Y(0)), (X(3), Y(4))
arrow(ax, o, q, 'sujet', lw=1.6)
disc(ax, *o, 1.2, 'encre')
text(ax, o[0] + 7, o[1] - 3.5, 'origine', 'fixe', 's')
text(ax, q[0] + 3, q[1] + 3, r'$(3\ ;\ 4)$', 'sujet', 's', ha='left')
text(ax, 14, 31, r'$v$', 'sujet', 'l')
text(ax, 62, 46, r'$|v|=5$', 'sujet', 'l', ha='left')
text(ax, 62, 36, 'v : la flèche', 'sujet', 's', ha='left')
text(ax, 62, 25, '|v| : sa longueur,', 'sujet', 's', ha='left')
text(ax, 62, 21.5, 'de l’origine à la', 'sujet', 's', ha='left')
text(ax, 62, 18, 'pointe', 'sujet', 's', ha='left')
save(fig, '74-088')
