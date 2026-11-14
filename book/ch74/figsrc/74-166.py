import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
t, x0, y0 = 15, 20, 18
text(ax, 44, 69, 'carrelage p4m', 'sujet', 'l')
for i in range(4):
    line(ax, [(x0, y0 + i*t), (x0 + 3*t, y0 + i*t)], 'fixe')
    line(ax, [(x0 + i*t, y0), (x0 + i*t, y0 + 3*t)], 'fixe')
for i in range(4):
    for j in range(4):
        x, y = x0 + i*t, y0 + j*t
        poly(ax, [(x-1.9, y), (x, y+2.6), (x+1.9, y), (x, y-2.6)], 'sujet')
for i in range(3):
    for j in range(3):
        disc(ax, x0 + (i+.5)*t, y0 + (j+.5)*t, 2.2, 'resultat')
poly(ax, [(6-1.9, 8), (6, 10.6), (6+1.9, 8), (6, 5.4)], 'sujet')
text(ax, 10, 8, 'losange bleu : coin', 'sujet', 's', ha='left')
disc(ax, 52, 8, 2.2, 'resultat')
text(ax, 56, 8, 'disque vert : centre', 'resultat', 's', ha='left')
save(fig, '74-166')
