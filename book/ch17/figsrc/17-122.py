import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
y = 22
f = numberline(ax, 8, 70, y, 0, 7, arrow_right=True)
text(ax, 44, 55, r'$\sqrt{x-3}$ existe si $x-3 \geq 0$', 'sujet', 'm')
line(ax, [(f(3), y + 7), (80, y + 7)], 'resultat', lw=2.8)
ax.add_patch(Circle((f(3), y + 7), 1.4, ec=COL['resultat'], fc=COL['resultat'], zorder=4))
line(ax, [(f(3), y + 7), (f(3), y)], 'fixe', dash=True)
text(ax, 66, y + 12, r'domaine : $x \geq 3$', 'resultat', 's')
disc(ax, f(2), y, 1.5, 'limite'); text(ax, f(2), y + 6, r'$\sqrt{-1}$', 'limite', 's')
text(ax, f(2), y + 11, 'n’existe pas', 'limite', 's')
ax.add_patch(Circle((f(4), y), 1.5, ec=COL['resultat'], fc=COL['resultat'], zorder=4))
text(ax, f(4) + 3, y + 3, r'$\sqrt{1}=1$', 'resultat', 's', ha='left')
save(fig, '17-122')
