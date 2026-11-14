import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
text(ax, 44, 91, r"$G'$ : produits de $a\,b\,a^{-1}\,b^{-1}$", 'sujet', 'm')
text(ax, 22, 82, r'$a$, $b$ commutent', 'encre', 's'); text(ax, 66, 82, 'triangle', 'encre', 's')
line(ax, [(44, 5), (44, 85)], 'fixe', dash=True)
# left column : commutative case
box(ax, 4, 66, 36, 9, 'sujet', label=r'$a\,b\,a^{-1}\,b^{-1}$')
arrow(ax, (22, 66), (22, 53), 'varie'); text(ax, 24.5, 59.5, r'échange $b$, $a^{-1}$', 'varie', 's', ha='left')
box(ax, 4, 44, 36, 9, 'sujet', label=r'$a\,a^{-1}\,b\,b^{-1}$')
arrow(ax, (22, 44), (22, 31), 'varie'); text(ax, 24.5, 37.5, r'$aa^{-1}=bb^{-1}=e$', 'varie', 's', ha='left')
box(ax, 12, 22, 20, 9, 'resultat', label='$e$', size='m')
text(ax, 22, 12, r"$G' = \{e\}$", 'resultat', 'l', weight='bold')
# right column : triangle
box(ax, 48, 66, 36, 9, 'sujet', label=r'$a\,b\,a^{-1}\,b^{-1}$')
arrow(ax, (66, 66), (66, 53), 'varie')
box(ax, 50, 44, 32, 9, 'limite', label='une rotation', size='s')
text(ax, 66, 12, r"$G' \neq \{e\}$", 'limite', 'l', weight='bold')
save(fig, '50-064')
