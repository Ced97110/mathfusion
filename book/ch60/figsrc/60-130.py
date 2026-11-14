import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
R, d, cy = 13, 11, 40
def venn(cx, left, mid, right, midrole, title, verdict, vrole):
    disc(ax, cx - d / 2, cy, R, 'sujet')
    disc(ax, cx + d / 2, cy, R, 'varie', fill=False, lw=1.3)
    text(ax, cx - d / 2 - 6.5, cy, left, 'sujet', 's')
    text(ax, cx, cy, mid, midrole, 's', weight='bold')
    text(ax, cx + d / 2 + 6.5, cy, right, 'varie', 's')
    text(ax, cx - d / 2 - 2, cy + R + 3, r'$\langle g\rangle$, $g=(1,0)$', 'sujet', 's')
    text(ax, cx, cy + R + 11, title, 'varie', 'm')
    text(ax, cx, cy - 20, verdict, vrole, 's', weight='bold')
venn(24, '(1, 0)\n(3, 0)', '(0, 0)\n(2, 0)', '(1, 1)\n(3, 1)', 'limite', 'ajout (1, 1) : ordre 4', 'chevauche en (2, 0)', 'limite')
venn(66, '(1, 0)\n(2, 0)\n(3, 0)', '(0, 0)', '(0, 1)', 'resultat', 'ajout (0, 1) : ordre 2', 'seul (0, 0) en commun', 'resultat')
text(ax, 44, 8, 'orange : sous-groupe ajouté H', 'varie', 's')
save(fig, '60-130')
