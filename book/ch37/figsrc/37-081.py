import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
steps = [('sujet', 'départ : Δ = ½ b c sin A', 8), ('fixe', 'étape 1 : cos A = 0,75 (avec a, b, c)', 8),
         ('varie', 'étape 2 : sin² A = (1 + cos A)(1 − cos A)\n= (1 + 0,75)(1 − 0,75) = 0,4375', 14), ('fixe', 'étape 3 : 150 × 70 et 50 × 30', 8),
         ('fixe', 'étape 4 : s = 75, 35, 25, 15', 8), ('fixe', 'étape 5 : Δ² = 984 375', 8),
         ('resultat', 'arrivée : Δ = 992,2 m², sans angle', 8)]
ys = []; ytop = 94
for role, lab, hh in steps:
    ytop -= hh; ys.append((ytop, hh)); ytop -= 4.5
for (role, lab, hh), (y, _) in zip(steps, ys):
    box(ax, 30, y, 57, hh, role, label=lab, size='s' if role == 'varie' else 'm', weight='bold' if role == 'varie' else 'normal', lw=1.6 if role == 'varie' else 0.8)
for (y0, h0), (y1, h1) in zip(ys[:-1], ys[1:]):
    arrow(ax, (58.5, y0), (58.5, y1 + h1), 'encre', lw=0.8)
# triangle b = 50, c = 60, angle A = 41,41° between them
Aa = math.acos(0.75)
A0 = (5, 46); Bp = (A0[0] + 0.38*60, A0[1]); Cp = (A0[0] + 0.38*50*0.75, A0[1] + 0.38*50*math.sin(Aa))
poly(ax, [A0, Bp, Cp], 'sujet')
th = [i*Aa/20 for i in range(21)]
ax.plot([A0[0] + 5*math.cos(t) for t in th], [A0[1] + 5*math.sin(t) for t in th], color=COL['encre'], lw=0.8, zorder=3)
text(ax, A0[0] - 1.5, A0[1] - 3, 'A', 'encre', 'm', weight='bold')
text(ax, A0[0] + 11, A0[1] - 3.5, 'c = 60', 'sujet', 'm')
text(ax, Cp[0] + 7, Cp[1] + 1, 'b = 50', 'sujet', 'm')
text(ax, A0[0] + 13, A0[1] + 3.5, '41,41°', 'encre', 's')
save(fig, '37-081')
