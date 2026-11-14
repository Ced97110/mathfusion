import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
text(ax, 44, 40, r'$V(-2)-V(2)=3-0=3$', 'encre', 'l')
for x in (6, 14, 22):
    box(ax, x, 24, 6, 6, 'sujet')
text(ax, 17, 17, r'$V(-2)=3$', 'sujet', 'm')
text(ax, 31, 27, '−', 'encre', 'l')
box(ax, 36, 24, 6, 6, 'fixe', fill=False, dash=True, label='0')
text(ax, 39, 17, r'$V(2)=0$', 'fixe', 'm')
text(ax, 50, 27, '=', 'encre', 'l')
for x in (60, 68, 76):
    disc(ax, x, 27, 3, 'resultat')
text(ax, 68, 17, '3 racines', 'resultat', 'm')
box(ax, 4, 2, 80, 9, 'resultat', label='trois racines distinctes entre −2 et 2')
save(fig, '69-088')
