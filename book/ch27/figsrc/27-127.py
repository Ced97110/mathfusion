import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
u = 5.0
cubes(ax, [(i, j, k) for i in range(4) for j in range(3) for k in range(2)], (22, 10), u, 'sujet')
text(ax, 22, 56, 'boîte droite', 'sujet', 's')
text(ax, 22, 50, '4 × 3 × 2 = 24 m³', 'resultat', 's')
o = (66, 12); v = 5.0
def Q(x, y, z):
    a = iso(x, y, 0, o, v); return (a[0] + z*v*0.9, a[1] + z*v*0.6 + z*v*0.4)
pts = lambda f: [Q(*p) for p in f]
poly(ax, pts([(0,0,0),(3,0,0),(3,2,0),(0,2,0)]), 'autre')
poly(ax, pts([(0,0,0),(3,0,0),(3,0,2),(0,0,2)]), 'autre')
poly(ax, pts([(0,0,0),(0,2,0),(0,2,2),(0,0,2)]), 'autre')
poly(ax, pts([(0,0,2),(3,0,2),(3,2,2),(0,2,2)]), 'autre')
text(ax, 66, 56, 'boîte penchée', 'autre', 's')
text(ax, 66, 50, 'déterminant (ch. 76)', 'autre', 's')
save(fig, '27-127')
