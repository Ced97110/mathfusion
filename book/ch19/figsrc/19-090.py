import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
# general form: slope and start are not readable
text(ax, 44, 63, 'forme générale', 'autre', 's')
box(ax, 22, 47, 44, 12, 'autre', label=r'$2x-y=-1$', size='l')
text(ax, 44, 42, 'pente ?   départ ?', 'autre', 's')
arrow(ax, (44, 38), (44, 32), 'fixe'); text(ax, 48, 35, 'même droite', 'fixe', 's', ha='left')
# slope-intercept form: y alone, then slope and start read directly
text(ax, 44, 29.5, 'forme pente-ordonnée', 'sujet', 's')
yy = 19
box(ax, 17, yy - 6, 12, 12, 'sujet', label=r'$y$', size='l')
text(ax, 33.5, yy, r'$=$', 'sujet', 'l')
box(ax, 38, yy - 6, 12, 12, 'resultat', label=r'$2$', size='l')
text(ax, 55, yy, r'$x$', 'sujet', 'l'); text(ax, 61, yy, r'$+$', 'sujet', 'l')
box(ax, 66, yy - 6, 12, 12, 'resultat', label=r'$1$', size='l')
for cx, r, t in [(23, 'sujet', r'$y$ seul'), (44, 'resultat', 'pente'), (72, 'resultat', 'départ')]:
    arrow(ax, (cx, yy - 7), (cx, yy - 10), r); text(ax, cx, yy - 13, t, r, 's')
save(fig, '19-090')
