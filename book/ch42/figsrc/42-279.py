import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(62)
def nested(cx, big, small, rb, rs, labbig, labsmall):
    cy = 34
    ax.add_patch(Circle((cx, cy), rb, fc=FILL[big], ec=COL[big], lw=0.9, zorder=2))
    ax.add_patch(Circle((cx, cy - 3.5), rs, fc=FILL[small], ec=COL[small], lw=0.9, zorder=3))
    text(ax, cx, cy - 3.5, labsmall, small, 'm'); text(ax, cx, cy + 7.5, labbig, big, 'm')
nested(15, 'autre', 'sujet', 11, 5, r'$B$', r'$A$')
nested(44, 'sujet', 'autre', 11, 5, r'$A$', r'$B$')
ax.add_patch(Circle((73, 34), 11, fc=FILL['sujet'], ec=COL['sujet'], lw=0.9, zorder=2))
ax.add_patch(Circle((73, 34), 12.3, fc='none', ec=COL['autre'], lw=0.9, ls='--', zorder=3))
text(ax, 73, 34, r'$A=B$', 'resultat', 'l')
text(ax, 29.5, 34, '+', 'encre', 'xl'); text(ax, 58.5, 34, r'$\Rightarrow$', 'resultat', 'xl')
for cx, t in ((15, 'preuve 1'), (44, 'preuve 2'), (73, 'conclusion')):
    text(ax, cx, 56, t, 'varie', 's')
for cx, t, r in ((15, r'$A\subseteq B$', 'sujet'), (44, r'$B\subseteq A$', 'autre'), (73, 'les deux sens', 'resultat')):
    text(ax, cx, 14, t, r, 'm')
save(fig, '42-279')
