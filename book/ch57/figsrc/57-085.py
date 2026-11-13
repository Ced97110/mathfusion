import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
# la règle 2 est nommée en haut
box(ax, 8, 68, 72, 10, 'varie', label=r'règle 2 : $(a+b)x=ax+bx$', size='s', lw=1.2)
# avec la règle 2 : 0x = 0
disc(ax, 8, 54.5, 4.5, 'varie', label='0')
box(ax, 16, 50, 24, 9, 'sujet', label='(2 ; 1)')
arrow(ax, (42, 54.5), (58, 54.5), 'varie')
box(ax, 60, 50, 24, 9, 'resultat', label='(0 ; 0)')
text(ax, 44, 41, r'$0x=(0+0)x=0x+0x$', 'sujet', 'm')
line(ax, [(2, 34), (86, 34)], 'fixe', lw=0.5)
# sans la règle 2 : 0x ne vaut plus 0
text(ax, 2, 29, 'règle 2 retirée : x ↦ x', 'fixe', 's', ha='left')
disc(ax, 8, 19.5, 4.5, 'varie', label='0')
box(ax, 16, 15, 24, 9, 'sujet', label='(2 ; 1)')
arrow(ax, (42, 19.5), (58, 19.5), 'varie')
box(ax, 60, 15, 24, 9, 'limite', label='(2 ; 1)')
text(ax, 72, 9, 'pas (0 ; 0)', 'limite', 's')
save(fig, '57-085')
