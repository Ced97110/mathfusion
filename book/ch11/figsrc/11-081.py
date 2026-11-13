import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def ring(ax, x, y, r, role, lw=2.2):
    th = [i * math.pi / 90 for i in range(181)]
    line(ax, [(x + r * math.cos(t), y + r * math.sin(t)) for t in th], role, lw=lw)
fig, ax = canvas(62)
disc(ax, 22, 33, 15, 'sujet'); ring(ax, 22, 33, 15, 'sujet')
poly(ax, [(52, 18), (82, 18), (82, 48), (52, 48)], 'autre', lw=0.8)
line(ax, [(52, 18), (82, 18), (82, 48), (52, 48), (52, 18)], 'autre', lw=2.2)
text(ax, 22, 56, r'circonférence $C$', 'sujet', 'm', weight='bold')
text(ax, 67, 56, 'périmètre', 'autre', 'm', weight='bold')
text(ax, 22, 10, 'tour : ligne courbe', 'sujet', 's')
text(ax, 67, 10, 'tour : 4 segments', 'autre', 's')
text(ax, 22, 33, r'$d$ = 5 m', 'fixe', 's')
text(ax, 67, 33, 'côté 5 m', 'fixe', 's')
save(fig, '11-081')
