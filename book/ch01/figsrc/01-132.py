import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 12, 50, '2', 'sujet', 'l')
text(ax, 15, 53.5, '3', 'varie', 'm')
text(ax, 14, 43, '2 puissance 3', 'encre', 's')
xs = [40, 56, 72]
for x in xs:
    disc(ax, x, 50, 4.5, 'sujet', label='2', size='m')
for x in [(xs[i] + xs[i+1]) / 2 for i in range(2)]:
    text(ax, x, 50, r'$\times$', 'encre', 'm')
arrow(ax, (14.5, 50), (35, 50), 'sujet')
brace(ax, 35.5, 76.5, 57, 'varie', label='3 nombres 2', down=False)
arrow(ax, (16.5, 55.5), (34, 58.5), 'varie', curve=0.3)
for x in [12, 19, 28, 35, 47, 54, 63, 70]:
    ax.add_patch(Rectangle((x, 22), 6, 6, ec=COL['resultat'], fc=FILL['resultat'], lw=0.8, zorder=2))
text(ax, 44, 33, r'2 $\times$ 2 $\times$ 2 = 8', 'resultat', 'm')
brace(ax, 12, 76, 20, 'resultat', label='8 épaisseurs', down=True)
box(ax, 24, 2, 40, 7, 'limite', label=r'pas 2 + 3 = 5', size='s')
save(fig, '01-132')
