# Copyright: Your Name. Apache 2.0
"""Outside checks on a Blender render of scene.json.

1. Every vertex Blender projects lies within 1 px of the numpy projection.
2. In the rendered image, the pixel under each parallelepiped vertex is drawn (alpha > 0),
   so the geometry on screen is the geometry of the fiche, not an off-frame or empty render.
3. The projected edge w is tilted at least 15° from vertical; no two vertices closer than 3 % of the height.
"""
from __future__ import annotations

import itertools
import json
import math
import sys

import numpy as np
from PIL import Image

TOL_PX, MIN_TILT_DEG = 1.0, 15.0


def numpy_px(scene: dict, pts: np.ndarray) -> np.ndarray:
    cam = scene["camera"]
    rot = np.array(cam["rot_columns"]).T
    rx, ry = cam["res"]
    xy = (pts - np.array(cam["location"])) @ rot[:, :2]
    k = rx / cam["ortho_scale"]
    return np.column_stack([rx / 2 + xy[:, 0] * k, ry / 2 - xy[:, 1] * k])


def main(scene_path: str, png_path: str) -> int:
    scene = json.load(open(scene_path))
    got = json.load(open(png_path.replace(".png", ".px.json")))
    alpha = np.asarray(Image.open(png_path).convert("RGBA"))[:, :, 3]
    ok = True
    for o in scene["objects"]:
        exp = numpy_px(scene, np.array(o["vertices"]))
        err = np.linalg.norm(exp - np.array(got[o["name"]]), axis=1).max()
        print(f"{o['name']}: écart max {err:.3f} px")
        ok &= err <= TOL_PX
    para = np.array(got["parallelepipede"])
    drawn = [alpha[int(round(y)) - 2 : int(round(y)) + 3, int(round(x)) - 2 : int(round(x)) + 3].max() > 0 for x, y in para]
    print("sommets du parallélépipède dessinés :", sum(drawn), "/ 8")
    ok &= all(drawn)
    w = para[4] - para[0]  # vertex 4 = o + w
    tilt = math.degrees(math.atan2(abs(w[0]), abs(w[1])))
    dmin = min(np.linalg.norm(p - q) for p, q in itertools.combinations(para, 2)) / alpha.shape[0]
    print(f"w à {tilt:.1f}° de la verticale ; distance min entre sommets {dmin:.1%} de la hauteur")
    ok &= tilt >= MIN_TILT_DEG and dmin >= 0.03
    print("RÉUSSI" if ok else "ÉCHEC")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
