import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
X, Wd = 8, 72
box(ax, 8, 53, 6, 5, 'sujet'); text(ax, 16, 55.5, r'$Sp$', 'sujet', 'm', ha='left')
box(ax, 40, 53, 6, 5, 'autre'); text(ax, 48, 55.5, r'$SL$', 'autre', 'm', ha='left')
text(ax, 44, 44, 'dimension 2 : 6 et 6', 'encre', 'm')
box(ax, X, 31, Wd, 9, 'autre'); box(ax, X, 31, Wd, 9, 'sujet')
text(ax, 44, 35.5, 'même taille', 'sujet', 's')
text(ax, 44, 22, 'dimension 4 : 720 et 20 160', 'encre', 'm')
box(ax, X, 9, Wd, 9, 'autre'); box(ax, X, 9, Wd * 720 / 20160, 9, 'sujet')
text(ax, 48, 13.5, r'$SL$ : 28 fois plus', 'autre', 's')
text(ax, 9.5, 4, '720', 'sujet', 's', ha='left')
save(fig, '75-085')
