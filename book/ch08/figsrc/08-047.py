import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 22, 54, 'à droite : faux', 'limite', 's')
text(ax, 66, 54, 'virgules alignées : juste', 'resultat', 's')
text(ax, 34, 42, '4,37', 'sujet', 'l', ha='right'); text(ax, 34, 33, '3,2', 'autre', 'l', ha='right')
text(ax, 15, 33, '+', 'encre', 'l')
line(ax, [(12, 28), (36, 28)], 'fixe'); text(ax, 34, 21, '4,69', 'limite', 'l', ha='right')
cx = 70
text(ax, cx, 42, '4', 'sujet', 'l', ha='right'); text(ax, cx, 42, ',37', 'sujet', 'l', ha='left')
text(ax, cx, 33, '3', 'autre', 'l', ha='right'); text(ax, cx, 33, ',20', 'autre', 'l', ha='left')
text(ax, 55, 33, '+', 'encre', 'l')
line(ax, [(52, 28), (84, 28)], 'fixe')
text(ax, cx, 21, '7', 'resultat', 'l', ha='right'); text(ax, cx, 21, ',57', 'resultat', 'l', ha='left')
save(fig, '08-047')
