import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def wave(ax, f, x0, w, y0, k, role, lw=1.1, dash=False, n=400, t1=2 * math.pi):
    line(ax, [(x0 + w * i / n, y0 + k * f(t1 * i / n)) for i in range(n + 1)], role, lw, dash)

fig, ax = canvas(84)
a = math.atan2(4, 3)
wave(ax, lambda t: 5 * math.sin(t + a), 6, 76, 61, 3, 'autre', 1.3)
text(ax, 44, 80, 'même période : hauteur 5', 'autre', 's')
line(ax, [(6, 61), (82, 61)], 'fixe', 0.5)
wave(ax, lambda t: 2 * abs(math.cos(t)), 6, 76, 22, 6, 'varie', 0.8, True)
wave(ax, lambda t: -2 * abs(math.cos(t)), 6, 76, 22, 6, 'varie', 0.8, True)
wave(ax, lambda t: math.sin(12 * t) + math.sin(14 * t), 6, 76, 22, 6, 'sujet', 1.0)
text(ax, 44, 41, 'périodes presque égales', 'sujet', 's')
text(ax, 44, 4, 'le volume monte et descend', 'varie', 's')
save(fig, '35-005')
