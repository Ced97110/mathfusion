import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
text(ax, 44, 82, r'si $g^2 \in gH$, alors :', 'varie', 'm')
def trio(y, parts):
    for x, s, r, d in parts:
        if s == '=': text(ax, x, y + 4, '=', 'encre', 'l')
        else: box(ax, x - 5, y - 0.5, 10, 9, r, label=s, size='l', dash=d)
y2 = 60
trio(y2, [(24, r'$g$', 'fixe', True), (38, r'$g$', 'varie', False), (52, '=', None, 0), (66, r'$g$', 'fixe', True), (80, r'$h$', 'sujet', False)])
text(ax, 44, y2 + 13, r'$g^2 = g\,h$ avec $h \in H$', 'encre', 's')
text(ax, 9, y2 + 4, 'on enlève\n$g$ à gauche', 'fixe', 's')
arrow(ax, (59, y2 - 2), (59, 46.5), 'varie')
y3 = 36
trio(y3, [(45, r'$g$', 'varie', False), (59, '=', None, 0), (73, r'$h$', 'sujet', False)])
arrow(ax, (59, y3 - 2), (59, 24.5), 'limite')
box(ax, 8, 8, 72, 14, 'limite', label=r'$g \notin H$ mais $h \in H$ :' + '\nimpossible', size='s')
save(fig, '50-154')
