import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def tri(ax, ox, oy, s, p=4, q=3, hl=None, arc=None):
    """Triangle rectangle en C ; A bas-gauche, C bas-droite, B haut-droite ; cotes p (AC) et q (BC)."""
    A = (ox, oy); C = (ox + p * s, oy); B = (ox + p * s, oy + q * s)
    poly(ax, [A, C, B], "fixe")
    for pts, k in (((A, C), "b"), ((C, B), "a"), ((A, B), "c")):
        line(ax, list(pts), (hl or {}).get(k, "fixe"), lw=2.2 if k in (hl or {}) else 0.9)
    line(ax, [(C[0] - 2.2, C[1]), (C[0] - 2.2, C[1] + 2.2), (C[0], C[1] + 2.2)], "fixe", lw=0.8)
    if arc:
        t1 = math.atan2(q, p)
        line(ax, [(ox + 7 * math.cos(t1 * i / 20), oy + 7 * math.sin(t1 * i / 20)) for i in range(21)], arc, lw=1.1)
    return A, B, C

fig, ax = canvas(56)
A, B, C = tri(ax, 8, 14, 10, hl={"c": "sujet"})
line(ax, [(C[0] - 3.2, C[1]), (C[0] - 3.2, C[1] + 3.2), (C[0], C[1] + 3.2)], "sujet", lw=1.2)
text(ax, C[0] + 3, C[1] - 2, "C", "sujet", "l", weight="bold")
text(ax, 28, 8, "$b$ = 4", "fixe", "s")
text(ax, 62, 29, "$a$ = 3", "fixe", "s")
text(ax, 24, 45, "$c$ = 5 : hypoténuse", "sujet", "s")
text(ax, 68, 8, "angle droit en C", "sujet", "s")
arrow(ax, (68, 12), (C[0] - 0.5, C[1] + 1.5), "sujet", curve=-0.2)
save(fig, "26-018")
