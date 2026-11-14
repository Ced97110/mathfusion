import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# Pétale : boucle qui part de O et y revient. cos 3θ : 3 pétales ; cos 2θ : 4 pétales
fig, ax = canvas(70)
u = 17
def petal(o, n, centre_deg, role):
    h = 90.0 / n
    pts = [(o[0] + u * math.cos(math.radians(n * d)) * math.cos(math.radians(centre_deg + d)),
            o[1] + u * math.cos(math.radians(n * d)) * math.sin(math.radians(centre_deg + d))) for d in [-h + 2 * h * i / 60 for i in range(61)]]
    poly(ax, pts, role)
o3 = (22, 34); o2 = (66, 34)
for k in range(1, 3):
    petal(o3, 3, 120 * k, 'fixe')
petal(o3, 3, 0, 'sujet')
for k in range(1, 4):
    petal(o2, 2, 90 * k, 'fixe')
petal(o2, 2, 0, 'sujet')
disc(ax, o3[0], o3[1], 1.2, 'encre'); disc(ax, o2[0], o2[1], 1.2, 'encre')
text(ax, o3[0], 62, r'$r = \cos 3\theta$', 'encre', 'm')
text(ax, o2[0], 62, r'$r = \cos 2\theta$', 'encre', 'm')
text(ax, o3[0], 12, '3 pétales', 'fixe', 'm')
text(ax, o2[0], 12, '4 pétales', 'fixe', 'm')
text(ax, o3[0] + 12, o3[1] + 7, 'un pétale', 'sujet', 's')
text(ax, o3[0] - 12, o3[1] - 10, 'pôle $O$', 'encre', 's')
text(ax, 44, 5, 'boucle qui part de $O$ et y revient', 'sujet', 's')
save(fig, '40-054')
