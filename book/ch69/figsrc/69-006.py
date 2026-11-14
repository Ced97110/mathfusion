import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
cx, cy, R = 24, 34, 15
disc(ax, cx, cy, R, 'fixe', fill=False, lw=0.6)
for k in range(5):
    a = math.radians(90 - 72 * k)
    disc(ax, cx + R * math.cos(a), cy + R * math.sin(a), 3.2, 'sujet', label=str(k))
text(ax, cx, cy, '3 > 4 ?', 'varie', 'm')
text(ax, cx, 60, 'cadran à 5 positions', 'sujet', 's')
text(ax, cx, 11, 'après 4, retour à 0', 'fixe', 's')
names = ['ℚ', 'ℝ', 'ℂ', 'ℤ/5ℤ', 'ℚ(√2)']
for i, n in enumerate(names):
    box(ax, 52, 50 - 10 * i, 32, 7, 'fixe', label=n + ' : ordre ?')
save(fig, '69-006')
