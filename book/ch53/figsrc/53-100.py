import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
cx, cy, R, N = 25, 28, 21, 55
good = 0
for k in range(N):
    a = math.pi / 2 - 2 * math.pi * k / N
    inv = math.gcd(k, N) == 1
    good += inv
    disc(ax, cx + R * math.cos(a), cy + R * math.sin(a), 1.3, 'resultat' if inv else 'fixe')
assert good == 40
text(ax, cx, cy + 3, r'$\varphi(55)$', 'resultat', 'l')
text(ax, cx, cy - 3, '= 40', 'resultat', 'l')
disc(ax, 58, 40, 1.5, 'resultat')
text(ax, 62, 40, '40 inversibles', 'resultat', 's', ha='left')
disc(ax, 58, 30, 1.5, 'fixe')
text(ax, 62, 30, '15 retirées', 'fixe', 's', ha='left')
text(ax, 58, 20, '11 + 5 − 1 = 15', 'encre', 's', ha='left')
text(ax, 58, 12, '55 − 15 = 40', 'encre', 's', ha='left')
save(fig, '53-100')
