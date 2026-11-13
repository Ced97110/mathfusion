import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 67, r'pair $>2$ = premier + premier', 'encre', 'm', weight='bold')
u, x0 = 2.6, 8
for y, (a, b) in ((50, (5, 23)), (40, (11, 17))):
    box(ax, x0, y, a * u, 7, 'sujet', label=str(a), size='m', r=0.4)
    box(ax, x0 + a * u, y, b * u, 7, 'sujet', label=str(b), size='m', r=0.4)
brace(ax, x0, x0 + 28 * u, 58, 'sujet', '28', down=False, size='m')
# vérifié / non démontré
yd, n = 26, 12
p = 4.4
for i in range(n):
    disc(ax, 8 + i * p, yd, 1.5, 'resultat')
for i in range(n, n + 3):
    disc(ax, 8 + i * p, yd, 1.5, 'autre', fill=False)
arrow(ax, (8 + (n + 3) * p - 1, yd), (84, yd), 'autre')
brace(ax, 6, 8 + (n - 1) * p + 2, yd - 3.5, 'resultat', 'vérifié par ordinateur')
brace(ax, 6, 84, yd - 12, 'autre', 'mais pas démontré pour tous')
save(fig, '05-183')
