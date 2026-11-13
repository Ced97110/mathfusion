import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
base = (30, 12); L = 50
a = math.radians(50)
arrow(ax, base, (base[0], base[1] + L), 'sujet', lw=2.0)
arrow(ax, base, (base[0] + L * math.sin(a), base[1] + L * math.cos(a)), 'autre', lw=2.0)
pts = [base] + [(base[0] + 22 * math.sin(a * k / 16), base[1] + 22 * math.cos(a * k / 16)) for k in range(17)]
poly(ax, pts, 'varie', lw=0.5)
text(ax, base[0] + 11, base[1] + 24.5, r'$\varphi$ = 50°', 'varie', 'l', ha='left')
text(ax, base[0] - 2.5, base[1] + 38, r'$AE$ : plus grande pente', 'sujet', 's', rot=90, ha='right')
text(ax, base[0] + 28, base[1] + 38, 'chemin du marcheur', 'autre', 's', rot=0, ha='left')
disc(ax, *base, 1.5, 'encre')
text(ax, base[0] + 1.5, base[1] - 4, r'$A$', 'encre', 'm', ha='left')
text(ax, 44, 70, 'colline vue de dessus', 'fixe', 's')
save(fig, '27-061')
