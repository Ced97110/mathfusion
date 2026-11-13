import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
y = 16
f = numberline(ax, 10, 64, y, -7, 7, every=7)
disc(ax, f(7), y, 1.7, 'sujet'); disc(ax, f(-7), y, 1.7, 'autre'); disc(ax, f(0), y, 1.3, 'fixe')
for cx, s, r in ((52, '7', 'sujet'), (76, '+7', 'sujet'), (10, r'$-7$', 'autre')):
    box(ax, cx - 6, 29, 12, 8, r, label=s, size='m')
    arrow(ax, (cx, 28.5), (f(7) if r == 'sujet' else f(-7), y + 2.5), r)
text(ax, 64, 43, 'rien ou + : à droite', 'sujet', 's')
text(ax, 2, 43, r'$-$ : à gauche', 'autre', 's', ha='left')
save(fig, '13-024')
