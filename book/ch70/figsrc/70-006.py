import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 66, r'$f(x,y)=0$ : un point réel ?', 'sujet', 'm', weight='bold')
s = 6.0
for cx, cy, role, caption in [(22, 34, 'resultat', 'oui : au moins un point'), (66, 34, 'limite', 'non : aucun point')]:
    box(ax, cx - 20, 10, 40, 48, role, fill=False, lw=0.7, dash=True)
    arrow(ax, (cx - 17, cy), (cx + 17, cy), 'fixe', lw=0.6)
    arrow(ax, (cx, cy - 20), (cx, cy + 20), 'fixe', lw=0.6)
    text(ax, cx + 18.5, cy - 2.2, r'$x$', 'fixe', 's')
    text(ax, cx + 2.5, cy + 21.5, r'$y$', 'fixe', 's')
    text(ax, cx, 5, caption, role, 's')
# left: a curve with a real point on it
disc(ax, 22 - 2, 34 + 1, 2 * s, 'sujet', fill=False, lw=1.3)
disc(ax, 22 + 2 * s * 0.6 - 2, 34 + 2 * s * 0.8 + 1, 1.2, 'resultat')
save(fig, '70-006')
