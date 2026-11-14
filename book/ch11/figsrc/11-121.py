import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
for cx, tour in ((22, True), (66, False)):
    cy, r = 46, 10
    if tour:
        disc(ax, cx, cy, r, 'fixe', fill=False, lw=2.0)
        ax.add_patch(Circle((cx, cy), r, ec=COL['sujet'], fc='none', lw=2.2, zorder=3))
    else:
        disc(ax, cx, cy, r, 'sujet')
    line(ax, [(cx, cy), (cx+r, cy)], 'varie', lw=1.3)
text(ax, 22, 64, '2π r', 'sujet', 'l'); text(ax, 66, 64, 'π r²', 'sujet', 'l')
line(ax, [(17, 30), (27, 30)], 'varie', lw=2.0); text(ax, 22, 33.5, 'r', 'varie', 's')
line(ax, [(55, 30), (65, 30)], 'varie', lw=2.0); text(ax, 60, 33.5, 'r', 'varie', 's')
text(ax, 68, 30, '×', 'encre', 'm', ha='left')
line(ax, [(73, 30), (83, 30)], 'varie', lw=2.0); text(ax, 78, 33.5, 'r', 'varie', 's')
text(ax, 22, 22, 'r écrit 1 fois', 'encre', 's'); text(ax, 66, 22, 'r écrit 2 fois', 'encre', 's')
text(ax, 22, 15, '1 longueur : un tour', 'sujet', 's'); text(ax, 66, 15, '2 longueurs : une aire', 'sujet', 's')
save(fig, '11-121')
