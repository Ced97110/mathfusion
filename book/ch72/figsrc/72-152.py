import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
cy = 30
def ln(c, deg, role, h=12):
    t = math.radians(deg); line(ax, [(c - h * math.cos(t), cy - h * math.sin(t)), (c + h * math.cos(t), cy + h * math.sin(t))], role, lw=1.4)
c = 15
ln(c, 0, 'sujet'); ln(c, 45, 'autre')
text(ax, c + 8, cy - 3.5, r'$S_u$', 'sujet', 's'); text(ax, c + 8, cy + 11, r'$S_v$', 'autre', 's')
line(ax, [(c + 7 * math.cos(math.radians(a)), cy + 7 * math.sin(math.radians(a))) for a in range(0, 46, 5)], 'varie', lw=0.9)
text(ax, c - 6, cy + 8, '45°', 'varie', 's')
text(ax, c, 12, 'deux plis', 'encre', 's')
for c, ang, role, lab in [(44, 90, 'varie', r'$S_uS_v$ : ¼ tour'), (73, 180, 'resultat', r'$(S_uS_v)^2$ : ½ tour')]:
    disc(ax, c, cy, 10, 'fixe')
    disc(ax, c + 10, cy, 1.5, 'encre')
    t = math.radians(ang); disc(ax, c + 10 * math.cos(t), cy + 10 * math.sin(t), 1.5, role)
    if ang == 90: arrow(ax, (c + 6, cy + 1), (c + 1, cy + 6), role, curve=0.4)
    else: arrow(ax, (c + 6, cy + 3), (c - 6, cy + 3), role, curve=0.6)
    text(ax, c, 12, lab, role, 's')
save(fig, '72-152')
