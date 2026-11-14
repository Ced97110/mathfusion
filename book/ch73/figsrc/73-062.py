import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
box(ax, 2, 2, 84, 68, 'fixe', r=2)
text(ax, 14, 65, r'$GL_2$', 'fixe', 'l')
ax.add_patch(Circle((32, 34), 20, ec=COL['sujet'], fc='none', lw=1.2, zorder=3))
ax.add_patch(Circle((56, 34), 20, ec=COL['autre'], fc='none', lw=1.2, zorder=3))
text(ax, 22, 59, r'$O(V,Q)$', 'sujet', 's'); text(ax, 66, 59, r'$SL_2$', 'autre', 's')
for x, l, r in ((22, 'miroir', 'sujet'), (44, 'quart\nde tour', 'resultat'), (66, 'cisaillement', 'autre')):
    disc(ax, x, 36, 1.2, r); text(ax, x, 30, l, r, 's')
save(fig, '73-062')
