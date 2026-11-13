import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
cs = [(35, 66), (53, 66), (44, 53)]
R = 14
for cx, cy in cs:
    ax.add_patch(Circle((cx, cy), R, ec='none', fc=FILL['sujet'], zorder=1))
for cx, cy in cs:
    ax.add_patch(Circle((cx, cy), R, ec=COL['sujet'], fc='none', lw=0.9, zorder=3))
text(ax, 27, 72, r'$A_1$', 'sujet', 'm')
text(ax, 61, 72, r'$A_2$', 'sujet', 'm')
text(ax, 44, 44, r'$A_3$', 'sujet', 'm')
text(ax, 44, 34, r'$n = 3$ clubs', 'encre', 'm')
text(ax, 44, 24, r'$A_1 \cup A_2 \cup \cdots \cup A_n$', 'varie', 'm')
arrow(ax, (44, 21), (44, 17), 'varie')
text(ax, 44, 9, r'$\bigcup_{i=1}^{n} A_i$', 'sujet', 'l')
save(fig, '42-137')
