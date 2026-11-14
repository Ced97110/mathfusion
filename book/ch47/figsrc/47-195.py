import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cx, cy, R = 23, 31, 18
for i in range(7):
    a = math.pi/2 - i*2*math.pi/7
    r = 'fixe' if i == 0 else ('varie' if i == 3 else 'sujet')
    disc(ax, cx + R*math.cos(a), cy + R*math.sin(a), 5, r, label=str(i), size='m')
text(ax, cx, cy, r'$p=7$', 'encre', 'm')
box(ax, 47, 46, 39, 12, 'sujet', label=r'6 inversibles $=7-1$', size='s')
arrow(ax, (66.5, 46), (66.5, 40), 'sujet')
text(ax, 66.5, 36.5, 'exposant 6', 'varie', 's')
text(ax, 66.5, 28, r'case 3 : $3^6=729$', 'varie', 's')
text(ax, 66.5, 22, r'$729=7\times104+1$', 'varie', 's')
arrow(ax, (66.5, 19), (66.5, 14), 'varie')
box(ax, 54, 3, 25, 9.5, 'resultat', label='reste 1', size='m')
save(fig, '47-195')
