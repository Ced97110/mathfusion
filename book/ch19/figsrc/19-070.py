import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
y1, y2 = 10, 58
line(ax, [(30, y1), (46, y1)], 'fixe', dash=True); line(ax, [(30, y2), (46, y2)], 'fixe', dash=True)
disc(ax, 30, y1, 2.2, 'sujet'); disc(ax, 30, y2, 2.2, 'autre')
text(ax, 26, y1, r'$y_1=5$', 'sujet', 'm', ha='right'); text(ax, 26, y2, r'$y_2=13$', 'autre', 'm', ha='right')
arrow(ax, (46, y1), (46, y2), 'varie', both=False)
text(ax, 50, 46, 'montée', 'varie', 'm', ha='left')
text(ax, 50, 34, r'$y_2-y_1$', 'varie', 'm', ha='left')
text(ax, 50, 24, r'$13-5=8$', 'resultat', 'l', ha='left', weight='bold')
save(fig, '19-070')
