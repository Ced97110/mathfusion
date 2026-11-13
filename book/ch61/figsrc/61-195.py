import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
fig, ax = canvas(80)
def angle(ox, oy, total, n, wl, tl, rw, rt):
    L = 32
    for k in range(n + 1):
        a = math.radians(total / n * k); edge = k in (0, n)
        line(ax, [(ox, oy), (ox + L * math.cos(a), oy + L * math.sin(a))], 'sujet' if edge else 'varie', lw=1.2 if edge else 0.9, dash=not edge)
    ax.add_patch(Arc((ox, oy), 16, 16, theta1=0, theta2=total, ec=COL['sujet'], lw=0.9, zorder=3))
    ax.add_patch(Arc((ox, oy), 28, 28, theta1=0, theta2=total / n, ec=COL['varie'], lw=0.9, zorder=3))
    m = math.radians(total / 2); t = math.radians(total / n / 2)
    text(ax, ox + rw * math.cos(m), oy + rw * math.sin(m), wl, 'sujet', 's')
    text(ax, ox + rt * math.cos(t), oy + rt * math.sin(t), tl, 'varie', 's')
angle(6, 34, 90, 3, '90°', '30°', 17, 22)
angle(48, 34, 60, 3, '60°', '20°', 20, 24)
text(ax, 22, 74, '90° partagé en 3', 'sujet', 's')
text(ax, 64, 74, '60° partagé en 3', 'sujet', 's')
box(ax, 3, 16, 38, 9, 'resultat', label='30° : se construit')
box(ax, 47, 16, 38, 9, 'limite', label='20° : pas constructible')
text(ax, 44, 10, 'un seul angle qui échoue', 'encre', 's')
text(ax, 44, 5.5, 'écarte une méthode générale', 'encre', 's')
save(fig, '61-195')
