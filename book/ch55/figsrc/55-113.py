import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
u = 8.0
ox, oy = 6, 18
text(ax, 44, 70, r'$\Delta=e_1^2-4e_2$', 'encre', 'l')
# carré de côté 5 = 3 + 2 : quatre rectangles 2 x 3 et un carré 1 x 1 au centre
rects = [(0, 0, 3, 2), (3, 0, 2, 3), (2, 3, 3, 2), (0, 2, 2, 3)]
for (a, b, c, d) in rects:
    ax.add_patch(Rectangle((ox + a * u, oy + b * u), c * u, d * u, ec=COL['autre'], fc=FILL['autre'], lw=0.8, zorder=2))
    text(ax, ox + (a + c / 2) * u, oy + (b + d / 2) * u, '6', 'autre', 'm')
ax.add_patch(Rectangle((ox + 2 * u, oy + 2 * u), u, u, ec=COL['resultat'], fc=FILL['resultat'], lw=1.0, zorder=2))
text(ax, ox + 2.5 * u, oy + 2.5 * u, '1', 'resultat', 'm', weight='bold')
ax.add_patch(Rectangle((ox, oy), 5 * u, 5 * u, ec=COL['sujet'], fc='none', lw=1.4, zorder=3))
brace(ax, ox, ox + 5 * u, oy, 'sujet', label=r'$x_1+x_2=5$', down=True)
text(ax, 54, 56, r'$e_1^2=5^2=25$', 'sujet', 'm', ha='left')
text(ax, 54, 44, r'$4e_2=4\times 6=24$', 'autre', 'm', ha='left')
text(ax, 54, 32, r'$\Delta=25-24=1$', 'resultat', 'm', ha='left', weight='bold')
save(fig, '55-113')
