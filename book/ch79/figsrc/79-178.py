import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
B = [('1',44,8),('2',28,26),('4',24,44),('12',28,62),('60',44,78)]
O = [('1',44,8),('5',60,26),('15',64,44),('30',60,62),('60',44,78)]
for ch, r in ((B,'sujet'),(O,'varie')):
    for i in range(4):
        if (ch is B and i == 3) or (ch is O and i == 0): continue
        line(ax, [ch[i][1:], ch[i+1][1:]], r, lw=1.6)
line(ax, [B[3][1:], B[4][1:]], 'resultat', lw=2.6)
line(ax, [O[0][1:], O[1][1:]], 'resultat', lw=2.6)
for ch, r in ((B,'sujet'),(O,'varie')):
    for k, x, y in ch[1:4] if True else []:
        disc(ax, x, y, 4.2, r, label=k)
disc(ax, 44, 8, 4.2, 'fixe', label='1'); disc(ax, 44, 78, 4.2, 'fixe', label='60')
arrow(ax, (38, 70), (50, 16), 'resultat', curve=-0.0, both=True)
text(ax, 17, 72, 'de 12 à 60', 'resultat', 's')
text(ax, 72, 14, 'de 1 à 5', 'resultat', 's')
for _p in ax.patches:
    if isinstance(_p, Circle): _p.set_zorder(3.5)
save(fig, '79-178')
