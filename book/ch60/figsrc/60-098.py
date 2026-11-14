import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 22, 64, 'la méthode liste', 'sujet', 's')
cx, cy, R = 22, 38, 10
for k in range(6):
    a = math.radians(90 - 60 * k)
    disc(ax, cx + R * math.cos(a), cy + R * math.sin(a), 2.0, 'sujet')
text(ax, 22, 18, r'$\mathbb{Z}/6$ : seul groupe', 'sujet', 's')
text(ax, 22, 11, 'abélien de 6 éléments', 'sujet', 's')
box(ax, 46, 20, 40, 40, 'limite', fill=False, dash=True)
text(ax, 66, 64, 'elle ne voit pas', 'limite', 's')
perms = ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']
for n, p in enumerate(perms):
    i, j = divmod(n, 2)
    box(ax, 49 + j * 18.5, 44 - i * 11.5, 16, 9, 'limite', label=p, size='s')
text(ax, 66, 11, 'rangements de 3 objets', 'limite', 's')
save(fig, '60-098')
