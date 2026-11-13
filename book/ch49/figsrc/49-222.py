import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
s = 6
for r in range(4): box(ax, 14, 14 + r * s, s, s, 'sujet', r=0.3, lw=0.5)
for i in range(2):
    for j in range(2): box(ax, 52 + i * s, 14 + j * s, s, s, 'autre', r=0.3, lw=0.5)
text(ax, 17, 52, 'petite orbite', 'sujet', 'm')
text(ax, 58, 52, 'orbite plus grande', 'autre', 'm')
text(ax, 17, 43, r'$|O|$ = 1', 'sujet', 'm')
text(ax, 58, 34, r'$|O|$ = 2', 'autre', 'm')
text(ax, 7, 26, '4', 'sujet', 'm')
text(ax, 46, 20, '2', 'autre', 'm')
text(ax, 17, 8, r'1 $\times$ 4 = 4', 'sujet', 'm')
text(ax, 58, 8, r'2 $\times$ 2 = 4', 'autre', 'm')
text(ax, 44, 3, r'même total : $|G|$', 'resultat', 's')
save(fig, '49-222')
