import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
yl = 30
f = lambda v: 44 + v * 7
line(ax, [(f(-4) - 5, yl), (f(-4) - 2.8, yl)], 'fixe')
for v in range(-4, 4): line(ax, [(f(v) + 2.8, yl), (f(v + 1) - 2.8, yl)], 'fixe')
arrow(ax, (f(4) + 2.8, yl), (f(4) + 8, yl), 'fixe', lw=0.9)
for v in range(-4, 5):
    role = 'sujet' if v == 1 else ('resultat' if v >= 0 else 'autre')
    disc(ax, f(v), yl, 2.8, role, label=str(v).replace('-', '−'), size='s')
brace(ax, f(0) - 3, f(4) + 3, yl + 4.5, 'resultat', 'sous-monoïde : 0, 1, 2, …', down=False)
brace(ax, f(-4) - 3, f(-1) + 3, yl - 4.5, 'autre', 'avec inverses : −1, −2, …', down=True)
arrow(ax, (f(2.4), yl - 11), (f(1) + 0.5, yl - 4.6), 'sujet'); text(ax, f(2.9), yl - 14, 'X = {1}', 'sujet', 's')
text(ax, 44, 52, 'même départ, deux ensembles', 'fixe', 's')
save(fig, '46-064')
