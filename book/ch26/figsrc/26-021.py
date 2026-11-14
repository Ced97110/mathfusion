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
A, B, C = tri(ax, 6, 14, 8, hl={"a": "sujet", "b": "autre"}, arc="varie")
text(ax, A[0] - 2.5, A[1] - 2, "A", "varie", "l", weight="bold")
text(ax, 22, 8, "$b$ = 4", "autre", "m")
text(ax, C[0] + 4, C[1] + 12, "$a$ = 3", "sujet", "m")
text(ax, 15, 36, "$c$ : pas utilisé", "fixe", "s", ha="center")
box(ax, 56, 38, 30, 9, "sujet", label="tan A", size="l", weight="bold")
text(ax, 71, 30, "côté opposé $a$ = 3", "sujet", "s")
text(ax, 71, 23, "côté adjacent $b$ = 4", "autre", "s")
box(ax, 56, 7, 30, 9, "resultat", label="3 ÷ 4 = 0,75", size="m")
arrow(ax, (71, 20), (71, 17), "resultat")
save(fig, "26-021")
