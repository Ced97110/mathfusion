import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
cx, cy, R = 28, 30, 22
for k in range(10):
    a = math.radians(90 - k * 36)
    inv = k in (1, 3, 7, 9)
    disc(ax, cx + R * math.cos(a), cy + R * math.sin(a), 5.5, 'sujet' if inv else 'fixe', fill=inv, label=str(k), size='m')
text(ax, 70, 40, r'$\varphi(10)=4$', 'sujet', 'l')
text(ax, 70, 33, '1, 3, 7, 9', 'sujet', 's')
text(ax, 70, 22, r'$\varphi(7)=6$', 'autre', 'l')
text(ax, 70, 15, 'toutes sauf 0', 'autre', 's')
save(fig, '47-188')
