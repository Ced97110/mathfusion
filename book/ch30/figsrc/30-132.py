import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
k = 0.7
cx, cy, r = 24, 20 + 22 * k, 20 * k
line(ax, [(3, 20), (45, 20)], 'fixe', lw=1.0)
ax.add_patch(Circle((cx, cy), r, ec=COL['fixe'], fc='none', lw=1.0, zorder=2))
disc(ax, cx, cy, 0.9, 'sujet')
arrow(ax, (cx, cy), (cx + r - 0.5, cy), 'sujet')
text(ax, cx + r / 2, cy + 2.4, '20 m', 'sujet', 's')
arrow(ax, (4, 20), (4, cy), 'varie', both=True)
text(ax, 5.5, 20 + 22 * k / 2, '22 m', 'varie', 's', ha='left')
disc(ax, cx + r, cy, 1.4, 'resultat')
text(ax, cx + r + 1, cy + 4.5, r'$t=2$', 'resultat', 's')
rows = [(r'centre $22$ m : $D=22$', 'varie'), (r'rayon $20$ m : $A=20$', 'sujet'),
        (r'tour en $8$ min : $2\pi/B=8$', 'autre'), (r'en montée à $t=2$ : $C=2$', 'resultat')]
for i, (s, ro) in enumerate(rows):
    box(ax, 48, 53 - i * 11, 38, 8, ro, label=s, size='s')
box(ax, 3, 3, 82, 9, 'encre', label=r'$h=20\,\sin(\frac{\pi}{4}(t-2))+22$', size='m')
save(fig, '30-132')
