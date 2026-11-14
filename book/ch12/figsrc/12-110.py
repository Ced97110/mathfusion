import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
box(ax, 6, 44, 76, 14, 'fixe')
text(ax, 44, 53.5, 'le nombre qui, multiplié', 'fixe', 'm'); text(ax, 44, 48.5, 'par a, donne 1', 'fixe', 'm')
arrow(ax, (44, 43), (44, 35), 'varie'); text(ax, 48, 39, 'on écrit', 'varie', 's', ha='left')
text(ax, 20, 29, '1', 'sujet', 20); line(ax, [(12, 23.5), (28, 23.5)], 'sujet', lw=1.4); text(ax, 20, 18, r'$a$', 'sujet', 20)
for y, t in [(29, '1 : le nombre un'), (23.5, 'trait : divisé par'), (18, r'$a$ : le nombre donné')]:
    text(ax, 50, y, t, 'fixe', 'm', ha='left'); arrow(ax, (48, y), (32, y), 'fixe', lw=0.7)
save(fig, '12-110')
