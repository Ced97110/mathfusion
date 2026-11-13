import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
xs = [18, 44, 70]
for x, ini, nom in zip(xs, 'RSA', ['Rivest', 'Shamir', 'Adleman']):
    disc(ax, x, 56, 6.5, 'sujet', label=ini, size='xl')
    text(ax, x, 45, nom, 'encre', 's')
    arrow(ax, (x, 42), (44 + (x - 44) * 0.5, 36), 'fixe')
box(ax, 30, 24, 28, 11, 'sujet', label='RSA', size='xl', weight='bold')
f = numberline(ax, 24, 64, 6, 1976, 1978, 1, arrow_right=False, every=2)
disc(ax, f(1976), 6, 1.4, 'autre'); disc(ax, f(1978), 6, 1.4, 'sujet')
text(ax, f(1976) - 2, 12.5, 'idée : Diffie et Hellman', 'autre', 's')
text(ax, f(1978) + 2, 12.5, "RSA réalise l'idée", 'sujet', 's')
save(fig, '53-007')
