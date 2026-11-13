import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
f = numberline(ax, 8, 76, 18, 0, 1, step=0.05, every=10, arrow_right=False, role='fixe')
for cx, lab in [(18, '35 %'), (44, '0,35'), (70, r'$\frac{7}{20}$')]:
    box(ax, cx - 11, 38, 22, 11, 'sujet', label=lab, size='l')
    arrow(ax, (cx, 37), (f(0.35) + (cx - 44) * 0.08, 21.5), 'sujet')
disc(ax, f(0.35), 18, 1.6, 'resultat')
text(ax, 44, 52.5, 'trois écritures', 'sujet', 's')
text(ax, 44, 6, 'une seule place sur la droite', 'resultat', 's')
save(fig, '09-073')
