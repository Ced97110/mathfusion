import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
box(ax, 3, 18, 82, 26, 'sujet')
for x, l in zip([20, 44, 68], [r'$e$', r'$r$', r'$r^2$']):
    disc(ax, x, 31, 5, 'sujet', label=l)
text(ax, 44, 22, r"$G'$ : les 3 rotations", 'sujet', 's')
arrow(ax, (66, 36.5), (46, 36.5), 'varie', curve=0.6)
text(ax, 56, 52, 'conjugué par une réflexion', 'varie', 's')
box(ax, 14, 3, 60, 9, 'resultat', label=r"conjugué : encore dans $G'$", size='s')
save(fig, '50-212')
