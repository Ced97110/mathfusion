import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(96)
box(ax, 3, 80, 30, 11, 'sujet', label=r'$G_f\subseteq A_n$', size='s')
text(ax, 44, 85.5, r'$\Leftrightarrow$', 'sujet', 'l')
box(ax, 55, 80, 30, 11, 'sujet', label=r'$d$ carré dans $F$', size='s')
text(ax, 44, 74, 'vrai si 1 + 1 ≠ 0', 'fixe', 's')
# left: framework
box(ax, 3, 36, 39, 34, 'resultat')
text(ax, 22.5, 65, '1 + 1 ≠ 0', 'resultat', 's', weight='bold')
text(ax, 22.5, 56, r'$D\neq -D$', 'resultat', 'm')
text(ax, 22.5, 47, 'un échange change D', 'resultat', 's')
text(ax, 22.5, 40, 'l’équivalence tient', 'resultat', 's')
# right: counterexample in F2
box(ax, 46, 36, 39, 34, 'limite')
text(ax, 65.5, 65, '1 + 1 = 0', 'limite', 's', weight='bold')
disc(ax, 56, 55, 4.6, 'limite'); text(ax, 56, 55, r'$\omega$', 'limite', 's')
disc(ax, 75, 55, 4.6, 'limite'); text(ax, 75, 55, r'$\omega+1$', 'limite', 's')
arrow(ax, (61, 55), (70, 55), 'limite', lw=1.0, both=True)
text(ax, 65.5, 44, 'D = −D = 1, d = 1', 'limite', 's')
text(ax, 65.5, 39.5, 'échange impair, mais d carré', 'limite', 's')
text(ax, 44, 27, 'sans l’hypothèse : faux', 'limite', 'm', weight='bold')
text(ax, 44, 20, r'$x^2+x+1$ sur $\{0,1\}$', 'fixe', 's')
save(fig, '65-043')
