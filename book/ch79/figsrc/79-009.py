import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)

POS = {1:(44,0),2:(26,1),3:(48,1),5:(70,1),4:(10,2),6:(30,2),10:(58,2),15:(78,2),12:(20,3),20:(40,3),30:(68,3),60:(44,4)}
EDG = [(1,2),(1,3),(1,5),(2,4),(2,6),(3,6),(3,15),(5,10),(5,15),(2,10),(4,12),(4,20),(6,12),(6,30),(10,20),(10,30),(15,30),(12,60),(20,60),(30,60)]
def hasse(ax, y0, dy, role=None, eroles=None, r=3.4, size='s'):
    role = role or {}; eroles = eroles or {}
    P = lambda n: (POS[n][0], y0 + POS[n][1] * dy)
    for a, b in EDG:
        (x1, y1), (x2, y2) = P(a), P(b); d = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / d, (y2 - y1) / d
        line(ax, [(x1 + ux * r, y1 + uy * r), (x2 - ux * r, y2 - uy * r)], eroles.get((a, b), 'fixe'), lw=1.7 if (a, b) in eroles else 0.9)
    for n in POS: disc(ax, P(n)[0], P(n)[1], r, role.get(n, 'fixe'), label=str(n), size=size)
    return P

E = {(4, 12): 'resultat', (4, 20): 'resultat', (12, 60): 'resultat', (20, 60): 'resultat'}
P = hasse(ax, 8, 12, role={12: 'varie', 20: 'varie', 60: 'resultat', 4: 'resultat'}, eroles=E)
text(ax, 52, P(60)[1], 'PPCM', 'resultat', 's', ha='left'); text(ax, 4, P(4)[1] - 7, 'PGCD', 'resultat', 's', ha='left')
save(fig, '79-009')
