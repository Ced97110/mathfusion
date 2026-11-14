import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def ea(ax, p, q, role='varie', hp=(7, 3.5), hq=(7, 3.5), curve=0.0, both=False):
    dx, dy = q[0] - p[0], q[1] - p[1]; L = math.hypot(dx, dy)
    t = lambda h: min(h[0] / abs(dx) if dx else 9e9, h[1] / abs(dy) if dy else 9e9) + 1.0 / L
    arrow(ax, (p[0] + dx * t(hp), p[1] + dy * t(hp)), (q[0] - dx * t(hq), q[1] - dy * t(hq)), role, curve=curve, both=both)
fig, ax = canvas(82)
hs = (8, 3.5)
A = [(22, 66, r'$\alpha$'), (35, 42, r'$\alpha^2$'), (9, 42, r'$\alpha^2+\alpha$')]
B = [(66, 66, r'$\alpha+1$'), (78, 42, r'$\alpha^2+1$'), (54, 42, r'$\alpha^2+\alpha+1$')]
for T, role, hw in ((A, 'sujet', 7.5), (B, 'varie', 8.5)):
    for (x, y, s) in T: box(ax, x - hw, y - 4, 2 * hw, 8, role, label=s, size='s')
    for i in range(3):
        p, q = T[i], T[(i + 1) % 3]
        ea(ax, p[:2], q[:2], role, (hw, 4), (hw, 4))
text(ax, 22, 29, 'triangle bleu', 'sujet', 's')
text(ax, 66, 29, 'triangle orange', 'varie', 's')
for x, s in ((30, '0'), (58, '1')): disc(ax, x, 12, 5, 'resultat', label=s)
text(ax, 44, 3, 'points fixes', 'resultat', 's')
text(ax, 44, 78, r'chaque flèche : $x\mapsto x^2$', 'encre', 's')
save(fig, '67-092')
