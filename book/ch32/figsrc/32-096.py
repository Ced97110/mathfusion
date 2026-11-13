import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def P(cx, cy, r, d):
    return (cx + r * math.cos(math.radians(d)), cy + r * math.sin(math.radians(d)))
def arc(ax, cx, cy, r, a0, a1, role, lw=0.9, dash=False, n=90):
    line(ax, [P(cx, cy, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw, dash)
def circ_axes(ax, cx, cy, r, ext=3):
    line(ax, [(cx - r - ext, cy), (cx + r + ext, cy)], "fixe", 0.5)
    line(ax, [(cx, cy - r - ext), (cx, cy + r + ext)], "fixe", 0.5)
    arc(ax, cx, cy, r, 0, 360, "fixe", 0.8)
def pt(ax, cx, cy, r, d, role, rr=1.3):
    x, y = P(cx, cy, r, d); disc(ax, x, y, rr, role)

fig, ax = canvas(86)
def eq(yc, inner, role):
    text(ax, 22, yc, 'sin', 'encre', 'l'); box(ax, 30, yc - 5, 16, 10, role, label=inner, size='l'); text(ax, 62, yc, '= 0,5', 'encre', 'l')
eq(78, '2θ', 'varie'); eq(56, 'y', 'sujet')
arrow(ax, (38, 72), (38, 62), 'varie'); text(ax, 42, 67, 'y = 2θ', 'varie', 'm', ha='left')
box(ax, 8, 28, 36, 8, 'varie', label='θ : 0° à 360°', size='s')
box(ax, 8, 12, 72, 8, 'sujet', label='y : 0° à 720°', size='s')
arrow(ax, (44, 28), (44, 21), 'varie'); text(ax, 48, 24.5, '× 2', 'varie', 'm', ha='left')
text(ax, 44, 5, 'ensuite θ = y ÷ 2', 'resultat', 'm')
save(fig, '32-096')
