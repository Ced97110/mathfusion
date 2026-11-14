import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# bits order: haut-gauche, haut-droite, bas-droite, bas-gauche ; 1 = orange, 0 = bleu
def pions(ax, cx, cy, s, bits, frame='fixe'):
    box(ax, cx - s / 2, cy - s / 2, s, s, frame, r=0.6, lw=0.8)
    d = s * 0.27
    for (dx, dy), b in zip([(-1, 1), (1, 1), (1, -1), (-1, -1)], bits):
        disc(ax, cx + dx * d, cy + dy * d, s * 0.16, 'varie' if b else 'sujet')
def rot(b, k=1):
    for _ in range(k % 4): b = (b[3], b[0], b[1], b[2])
    return b
def orbit(b):
    out = []
    for k in range(4):
        c = rot(b, k)
        if c not in out: out.append(c)
    return out
fig, ax = canvas(80)
a = (0, 1, 0, 0); z = (0, 0, 0, 0)
pions(ax, 16, 62, 16, a, 'resultat'); pions(ax, 72, 62, 16, rot(a), 'resultat')
arrow(ax, (26, 62), (62, 62), 'resultat', lw=1.2); text(ax, 44, 67, r'$r$', 'resultat', 'l')
text(ax, 44, 52, 'même orbite', 'resultat', 'm', weight='bold')
line(ax, [(4, 44), (84, 44)], 'fixe', dash=True)
pions(ax, 16, 24, 16, z, 'limite'); pions(ax, 72, 24, 16, a, 'limite')
arrow(ax, (26, 24), (62, 24), 'limite', lw=1.2)
text(ax, 44, 29, r'$\times$', 'limite', 'xl'); text(ax, 44, 14, 'aucune rotation', 'limite', 's')
text(ax, 44, 5, 'orbites différentes', 'limite', 'm', weight='bold')
save(fig, '49-225')
