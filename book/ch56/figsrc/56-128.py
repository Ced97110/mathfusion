import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(60)
u = 7.5; ox, oy = 11.5, 16.0
X = lambda re: ox + re * u
Y = lambda im: oy + im * u
for re in range(-1, 10):
    for im in range(-1, 5):
        disc(ax, X(re), Y(im), 0.45, 'fixe')
lat = set()
for m in range(-6, 12):
    for n in range(-6, 12):
        re, im = 2 * m - n, m + 2 * n
        if -1 <= re <= 9 and -1 <= im <= 4:
            lat.add((re, im))
# réseau des multiples de b (2 + i) : lignes du réseau tourné
for (re, im) in lat:
    for (dr, di) in ((2, 1), (-1, 2)):
        if (re + dr, im + di) in lat:
            line(ax, [(X(re), Y(im)), (X(re + dr), Y(im + di))], 'varie', lw=0.5)
for (re, im) in lat:
    disc(ax, X(re), Y(im), 1.1, 'varie')
# cercle centré en bq = 7 + i, rayon |b| = racine de 5
rad = math.sqrt(5) * u
ax.add_patch(Circle((X(7), Y(1)), rad, ec=COL['fixe'], fc='none', lw=0.8, ls='--', zorder=1.8))
disc(ax, X(7), Y(1), 2.0, 'varie')
disc(ax, X(7), Y(2), 1.7, 'sujet')
arrow(ax, (X(7), Y(1) + 1.4), (X(7), Y(2) - 1.9), 'resultat', lw=1.2)
text(ax, X(7) + 3, Y(2) + 3.5, r'$a=7+2i$', 'sujet', 'm', ha='left')
text(ax, X(7) - 2.5, Y(1) - 4.5, r'$bq$', 'varie', 's', ha='right')
text(ax, X(7) + 2.5, Y(1.5), r'$r=i$', 'resultat', 's', ha='left')
text(ax, X(2) + 2, Y(1) + 3.5, r'$b$', 'varie', 's')
text(ax, X(0) - 2.5, Y(0) - 3.2, '0', 'fixe', 's')
text(ax, 24, 4.5, 'cercle centré sur $bq$', 'fixe', 's')
text(ax, 44, 55, r'taille $\delta$ : $\delta(r)=1$ plus petit que $\delta(b)=5$', 'resultat', 's')
save(fig, '56-128')
