import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arc(ax, cx, cy, R, a0, a1, role='sujet', lw=1.0, n=80):
    line(ax, [(cx + R * math.cos(a0 + (a1 - a0) * i / n), cy + R * math.sin(a0 + (a1 - a0) * i / n)) for i in range(n + 1)], role, lw)

def rad(ax, cx, cy, R, a, role='fixe', lw=0.9, r0=0.0):
    line(ax, [(cx + r0 * math.cos(a), cy + r0 * math.sin(a)), (cx + R * math.cos(a), cy + R * math.sin(a))], role, lw)

def pol(cx, cy, R, a):
    return (cx + R * math.cos(a), cy + R * math.sin(a))

fig, ax = canvas(64)
cxs = [16, 44, 72]
cy, R = 52, 9
arc(ax, cxs[0], cy, R, 0, 2 * math.pi, 'sujet', 1.8)
arc(ax, cxs[1], cy, R, 0, 2 * math.pi, 'fixe', 0.8)
arc(ax, cxs[1], cy, R, 0, math.pi, 'varie', 2.2)
arc(ax, cxs[2], cy, R, 0, 2 * math.pi, 'fixe', 0.8)
arc(ax, cxs[2], cy, R, 0, math.pi, 'varie', 2.2)
rad(ax, cxs[2], cy, R, 0, 'sujet', 1.4); rad(ax, cxs[2], cy, R, math.pi, 'sujet', 1.4)
boxes = [('sujet', r'$C=2\pi r$'), ('varie', r'$\pi r$'), ('resultat', r'$\theta=\pi r/r=\pi$')]
for i, (role, lab) in enumerate(boxes):
    box(ax, cxs[i] - 11, 22, 22, 12, role, label=lab, size='s')
for i, cap in enumerate(['départ', 'étape qui porte', 'arrivée']):
    text(ax, cxs[i], 15, cap, 'encre', 's')
arrow(ax, (cxs[0] + 11, 28), (cxs[1] - 11, 28), 'encre')
arrow(ax, (cxs[1] + 11, 28), (cxs[2] - 11, 28), 'encre')
text(ax, 30, 38, 'moitié', 'varie', 's')
text(ax, 58, 38, '÷ r', 'varie', 's')
save(fig, '29-047')
