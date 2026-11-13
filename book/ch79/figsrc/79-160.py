import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
box(ax, 4, 54, 40, 11, 'sujet', label=r'$10 = 4 + h_3$')
box(ax, 4, 32, 40, 11, 'varie', label=r'$h_3 = 10 - 4$')
box(ax, 4, 10, 40, 11, 'resultat', label=r'$h_3 = 6$', weight='bold')
arrow(ax, (24, 54), (24, 43), 'varie'); arrow(ax, (24, 32), (24, 21), 'varie')
text(ax, 50, 48.5, 'on retire 4\ndes deux côtés', 'varie', 's', ha='left')
text(ax, 50, 26.5, 'on calcule', 'varie', 's', ha='left')
box(ax, 54, 5, 32, 14, 'resultat', label='4 et 10 pairs :\n6 reste pair', size='s') if False else None
text(ax, 66, 10, '4 et 10 pairs :\n6 reste pair', 'resultat', 's')
save(fig, '79-160')
