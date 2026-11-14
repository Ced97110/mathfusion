import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
def nd(x, y, n, role, w=12, h=7): box(ax, x - w/2, y - h/2, w, h, role, label=n)
text(ax, 20, 56, 'dessin', 'sujet', 'l', weight='bold'); text(ax, 64, 56, 'calcul', 'autre', 'l', weight='bold')
line(ax, [(42,6),(42,58)], 'fixe', dash=True)
nd(8,16,'12','sujet'); nd(32,16,'20','autre'); nd(20,40,'60','resultat')
line(ax, [(10,20),(17,36)]); line(ax, [(30,20),(23,36)])
text(ax, 48, 42, 'multiples de 12', 'sujet', 's', ha='left'); text(ax, 48, 22, 'multiples de 20', 'autre', 's', ha='left')
X = lambda v: 48 + v / 60 * 30
for v in (12, 24, 36, 48): disc(ax, X(v), 35, 2.8, 'sujet', label=str(v), size='s')
for v in (20, 40): disc(ax, X(v) - 0.0, 15, 2.8, 'autre', label=str(v), size='s')
disc(ax, 82, 25, 3.4, 'resultat', label='60', size='s')
line(ax, [(X(48)+2.8,35),(80,27.5)], 'fixe'); line(ax, [(X(40)+2.8,15),(80,22.5)], 'fixe')
save(fig, '79-090')
