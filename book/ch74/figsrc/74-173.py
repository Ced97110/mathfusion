import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 22, 61, r'$D_4$ : 8 éléments', 'sujet', 'l')
c = (22, 46); h = 8
poly(ax, [(c[0]-h, c[1]-h), (c[0]+h, c[1]-h), (c[0]+h, c[1]+h), (c[0]-h, c[1]+h)], 'sujet')
for dx, dy in [(12,0),(0,12),(12,12),(12,-12)]:
    line(ax, [(c[0]-dx, c[1]-dy), (c[0]+dx, c[1]+dy)], 'varie', dash=True)
text(ax, 22, 29, '4 axes : 4 réflexions', 'varie', 's')
for k in range(4):
    x = 3 + k * 10
    box(ax, x, 12, 8, 8, 'sujet', r=0.4)
    cxm = [x+1.8, x+6.2, x+6.2, x+1.8][k]; cym = [y for y in [14+0, 14.0+0, 18.2, 18.2]][k]
    cxm, cym = [(x+1.8, 13.8), (x+6.2, 13.8), (x+6.2, 18.2), (x+1.8, 18.2)][k]
    disc(ax, cxm, cym, 1.1, 'varie')
    text(ax, x+4, 8.5, ['0°', '90°', '180°', '270°'][k], 'varie', 's')
text(ax, 22, 3, '4 rotations', 'varie', 's')
t = 8.5
for i in range(4):
    line(ax, [(54, 24+i*t), (54+3*t, 24+i*t)], 'resultat')
    line(ax, [(54+i*t, 24), (54+i*t, 24+3*t)], 'resultat')
text(ax, 67, 18, 'réseau carré', 'resultat', 'm')
arrow(ax, (45, 46), (52, 46), 'fixe', both=True)
text(ax, 48.5, 51, 'ordre 4', 'fixe', 's')
save(fig, '74-173')
