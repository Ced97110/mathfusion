import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
G = [[(5, 21), (14, 21), (9.5, 28)], [(23, 21), (28, 22), (25.5, 28)], [(9, 7.5), (23, 7.5)]]
R = [(0, 17, 17, 16), (19, 17, 13, 16), (0, 1, 32, 13)]
RL = ['sujet', 'varie', 'autre']
for ox in (2, 54):
    for g, rl in zip(G, RL):
        for p in g: disc(ax, ox + p[0], p[1], 1.2, rl)
for g, rl in zip(G, RL):
    for i in range(len(g)):
        for j in range(i + 1, len(g)):
            line(ax, [(2 + g[i][0], g[i][1]), (2 + g[j][0], g[j][1])], rl, lw=0.9)
for (x, y, w, h), rl in zip(R, RL): box(ax, 54 + x, y, w, h, rl, fill=False, lw=1.0)
text(ax, 18, 40, 'relation', 'fixe', 'm'); text(ax, 70, 40, 'partition', 'resultat', 'm')
arrow(ax, (38, 31), (51, 31), 'sujet'); text(ax, 44.5, 35, 'classes', 'sujet', 's')
arrow(ax, (51, 15), (38, 15), 'varie'); text(ax, 44.5, 11, 'même bloc', 'varie', 's')
text(ax, 44, 46, 'chaque côté donne l’autre', 'encre', 'm')
save(fig, '43-069')
