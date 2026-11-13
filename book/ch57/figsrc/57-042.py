import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
text(ax, 44, 83, r'$s$ : un geste $g$ devient « $g$ puis $g$ »', 'fixe', 's')
# ligne 1 : x puis y sur trois cartes
box(ax, 2, 62, 24, 10, 'fixe', label='A  B  C', size='s')
arrow(ax, (26.5, 67), (55.5, 67), 'varie', lw=1.2)
text(ax, 41, 71, 'x puis y', 'varie', 's')
box(ax, 56, 62, 24, 10, 'sujet', label='C  A  B', size='s')
# ligne 2 : deux façons de calculer l'image de « x puis y » par s
arrow(ax, (14, 61.5), (14, 47.5), 'fixe', lw=1.0)
arrow(ax, (68, 61.5), (68, 47.5), 'varie', lw=1.2)
text(ax, 72, 54.5, r'$s$', 'varie', 's', ha='left')
box(ax, 2, 28, 40, 19, 'fixe', label='si s respectait +,\ns(x) puis s(y) =\nne rien faire : A B C', size='s')
box(ax, 46, 28, 40, 19, 'autre', label='s(x puis y) :\nC A B deux fois\ndonne B C A', size='s')
text(ax, 44, 37.5, r'$\neq$', 'limite', 'xl', weight='bold')
text(ax, 44, 19, "A B C ≠ B C A", 'limite', 'm')
text(ax, 44, 11, "s n'est pas un endomorphisme", 'limite', 's')
save(fig, '57-042')
