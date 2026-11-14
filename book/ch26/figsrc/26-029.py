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
fig, ax = canvas(62)
A, B, C = tri(ax, 20, 26, 8, hl={"b": "sujet"}, arc="varie")
t = math.atan2(3, 4); r = 5
line(ax, [(B[0] + r * math.cos(math.radians(180 + 90 - (90 - math.degrees(t)) * 0 - (math.degrees(t) + 90) * i / 20 * 0)), B[1]) for i in range(1)] or [], "autre") if False else None
text(ax, A[0] - 3, A[1] - 2, "A", "varie", "l", weight="bold")
text(ax, B[0] + 3, B[1] + 3, "B", "autre", "l", weight="bold")
text(ax, 36, 31, "$b$ = 4", "sujet", "m")
text(ax, 31, 43, "$c$ = 5", "fixe", "s")
box(ax, 2, 4, 40, 10, "varie", label="cos A = 4 ÷ 5 = 0,8", size="s")
box(ax, 46, 4, 40, 10, "autre", label="sin B = 4 ÷ 5 = 0,8", size="s")
arrow(ax, (22, 14), (33, 25), "varie"); arrow(ax, (66, 14), (40, 25), "autre")
save(fig, "26-029")
