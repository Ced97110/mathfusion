import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, r'$N$ = 16 + 2 + 4 + 2 = 24', 'sujet', 'm')
arrow(ax, (44, 53), (44, 49), 'varie')
for g in range(6):
    gx = 8 + (g % 3) * 26; gy = 30 - (g // 3) * 12
    box(ax, gx - 1.8, gy - 1.5, 20.4, 10, 'sujet', fill=False, dash=True, r=1)
    for k in range(4):
        box(ax, gx + k * 4.2, gy, 3.8, 7, 'sujet', r=0.4, lw=0.5)
text(ax, 22, 44.5, r'un groupe : $|G|$ = 4', 'sujet', 's')
text(ax, 44, 11, r'24 $\div$ 4 = 6 groupes', 'varie', 'm')
text(ax, 44, 4, r'$k$ = 6 orbites', 'resultat', 'l')
save(fig, '49-221')
