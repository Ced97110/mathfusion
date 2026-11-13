import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 6, 60, 'rationnel : 15/11', 'autre', 'm', ha='left')
box(ax, 6, 46, 9, 10, 'autre', label='1,')
for c in range(2):
    box(ax, 17 + 13 * c, 46, 11, 10, 'autre', label='36')
box(ax, 43, 46, 10, 10, 'autre', label='…')
arrow(ax, (22.5, 45.5), (35.5, 45.5), 'autre', curve=0.7)
text(ax, 29, 37, 'bloc 36 qui revient', 'autre', 's')
text(ax, 6, 30, 'irrationnel : √2', 'sujet', 'm', ha='left')
box(ax, 6, 16, 9, 10, 'sujet', label='1,')
for c, g in enumerate(['41', '42', '13', '5']):
    box(ax, 17 + 13 * c, 16, 11, 10, 'sujet', label=g)
box(ax, 69, 16, 10, 10, 'sujet', label='…')
text(ax, 42, 8, 'aucun bloc ne revient', 'limite', 's')
save(fig, '12-079')
