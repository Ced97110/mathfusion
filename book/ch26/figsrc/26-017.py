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
A, B, C = tri(ax, 8, 14, 10, hl={"b": "sujet"}, arc="varie")
text(ax, A[0] - 3, A[1] - 2, "A", "varie", "l", weight="bold")
text(ax, B[0] + 3, B[1] + 2, "B", "fixe", "m")
text(ax, C[0] + 3, C[1] - 2, "C", "fixe", "m")
text(ax, 28, 8, "$b$ = 4 : touche A", "sujet", "m")
text(ax, 62, 29, "$a$ = 3", "fixe", "s")
text(ax, 22, 42, "$c$ = 5", "fixe", "s")
text(ax, 62, 46, "hypoténuse : pas $b$", "fixe", "s", ha="right") if False else None
save(fig, "26-017")
