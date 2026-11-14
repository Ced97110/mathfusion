import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
box(ax, 4, 66, 80, 12, 'varie', label='Pour combien de carrés ?', size='l')
text(ax, 44, 58, r'$N(xy)=N(x)N(y)$, $N$ = somme de carrés', 'encre', 's')
def sq(x, y, role, lab=None, dash=False):
    box(ax, x, y, 7, 7, role, label=lab, dash=dash, size='m')
text(ax, 4, 49, '1 carré', 'sujet', 's', ha='left'); sq(4, 38, 'sujet')
text(ax, 38, 42, r'$2^2\cdot3^2=6^2$', 'resultat', 's', ha='left')
text(ax, 4, 30, '2 carrés', 'sujet', 's', ha='left'); sq(4, 19, 'sujet'); sq(12, 19, 'sujet')
text(ax, 38, 22, r'$5\cdot25=5^2+10^2$', 'resultat', 's', ha='left')
text(ax, 4, 11.5, r'$3,\ 4,\ \ldots$ carrés', 'varie', 's', ha='left')
for k in range(3): sq(4 + k * 9, 0.5, 'varie', '?', True)
save(fig, '77-143')
