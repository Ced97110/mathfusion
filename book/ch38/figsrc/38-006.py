import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
gy = 14
line(ax, [(2, gy), (86, gy)], 'fixe')
poly(ax, [(62, gy), (76, 44), (86, gy)], 'fixe')
S = (76, 44)
stations = [(8, gy), (20, gy)]
for s in stations:
    line(ax, [s, S], 'varie', lw=1.0)
    disc(ax, s[0], s[1], 1.4, 'sujet')
line(ax, [stations[0], stations[1]], 'sujet', lw=2.2)
disc(ax, S[0], S[1], 1.2, 'sujet')
text(ax, 76, 49, 'Everest', 'sujet', 's')
text(ax, 14, gy + 6, 'stations', 'sujet', 's')
brace(ax, 8, 76, gy - 1.5, 'fixe', label='plus de 100 km')
text(ax, 44, 40, 'hauteur calculée', 'resultat', 's')
text(ax, 44, 34, 'depuis la plaine', 'resultat', 's')
save(fig, '38-006')
