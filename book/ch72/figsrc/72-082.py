import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(70)
o = (44, 33); t = 17; g = 6.5
line(ax, [(o[0]-2*t, o[1]-t), (o[0]+2*t, o[1]+t)], 'sujet', lw=1.6)
line(ax, [(o[0]+0.7*t, o[1]-1.4*t), (o[0]-0.7*t, o[1]+1.4*t)], 'autre', lw=1.6)
d1 = (2/5**.5, 1/5**.5); d2 = (-1/5**.5, 2/5**.5); k = 3
p1 = (o[0]+k*d1[0], o[1]+k*d1[1]); p3 = (o[0]+k*d2[0], o[1]+k*d2[1]); p2 = (p1[0]+k*d2[0], p1[1]+k*d2[1])
line(ax, [p1, p2, p3], 'resultat', lw=0.8)
arrow(ax, o, (o[0]+2*g, o[1]+g), 'sujet', lw=2.0)
arrow(ax, o, (o[0]-g, o[1]+2*g), 'autre', lw=2.0)
# a few more vectors of each line: the whole line is U, the whole line is U-perp
for m in (-2, -1, 2):
    disc(ax, o[0]+2*g*m*0.75, o[1]+g*m*0.75, 1.0, 'sujet')
for m in (-1.5, 1.5):
    disc(ax, o[0]-g*m*0.75, o[1]+2*g*m*0.75, 1.0, 'autre')
text(ax, 86, 60, r'$U$ : multiples de (2 ; 1)', 'sujet', 's', ha='right')
text(ax, 2, 66, r'$U^{\perp}$ : multiples de ($-$1 ; 2)', 'autre', 's', ha='left')
text(ax, 44, 5, r'$U^{\perp}$ : orthogonal à tous les vecteurs de $U$', 'resultat', 's')
save(fig, '72-082')
