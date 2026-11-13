import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
c = (40, 38); u = 22
th = [math.radians(a) for a in range(0, 361, 3)]
line(ax, [(c[0]+u*math.cos(t), c[1]+u*math.sin(t)) for t in th], 'fixe', dash=True)
for i in (-1, 0, 1):
    for j in (-1, 0, 1):
        disc(ax, c[0]+i*u, c[1]+j*u, 0.9, 'sujet')
def arc(r, a0, a1, role):
    pts = [(c[0]+r*math.cos(math.radians(a)), c[1]+r*math.sin(math.radians(a))) for a in range(a0, a1+1)]
    line(ax, pts[:-2], role, lw=1.3); arrow(ax, pts[-3], pts[-1], role, lw=1.3)
arc(10, 0, 90, 'resultat'); arc(15, 0, 72, 'limite')
disc(ax, c[0]+u, c[1], 1.8, 'sujet')
text(ax, c[0]+u+2, c[1]-4, r'$(1,0)$', 'sujet', 's', ha='left')
disc(ax, c[0], c[1]+u, 2.2, 'resultat')
text(ax, c[0]-3, c[1]+u+4, r'$(0,1)$ : dans la grille', 'resultat', 's', ha='right')
p = (c[0]+u*math.cos(math.radians(72)), c[1]+u*math.sin(math.radians(72)))
disc(ax, p[0], p[1], 2.2, 'limite', fill=False, lw=1.2)
text(ax, p[0]+3, p[1]+5, 'hors de la grille', 'limite', 's', ha='left')
text(ax, 61, 43, '72°', 'limite', 's'); text(ax, 45, 45, '90°', 'resultat', 's')
text(ax, 44, 4, r'$\approx(0{,}31\ ;\ 0{,}95)$ : ordre 5 exclu', 'limite', 's')
save(fig, '74-108')
