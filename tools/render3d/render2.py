# Copyright: Your Name. Apache 2.0
"""Blender Cycles render of scene.json.

Usage: Blender -b -P render2.py -- scene.json out.png [samples]
Writes out.png (transparent background, soft shadows on an invisible floor) and
out.px.json (pixel position of each vertex and anchor, as Blender projects them).
"""
import json
import sys

import bpy
from bpy_extras.object_utils import world_to_camera_view
from mathutils import Matrix, Vector


def material(name: str, rgb: list, alpha: float, rough: float = 0.45) -> bpy.types.Material:
    mat = bpy.data.materials.new(name)
    bsdf = mat.node_tree.nodes["Principled BSDF"]
    bsdf.inputs["Base Color"].default_value = (*rgb, 1.0)
    bsdf.inputs["Roughness"].default_value = rough
    bsdf.inputs["Alpha"].default_value = alpha
    return mat


def ink(name: str, rgb: list) -> bpy.types.Material:
    """Edge material: emits its own colour so edges stay crisp and keep the role colour."""
    mat = material(name, [0.0, 0.0, 0.0], 1.0, 1.0)  # black base: only the emission shows
    bsdf = mat.node_tree.nodes["Principled BSDF"]
    bsdf.inputs["Specular IOR Level"].default_value = 0.0
    bsdf.inputs["Emission Color"].default_value = (*srgb_to_linear(rgb), 1.0)
    bsdf.inputs["Emission Strength"].default_value = 1.0  # with "Standard" view: pixel = role colour
    return mat


def srgb_to_linear(rgb: list) -> list:
    return [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in rgb]


def mix(a: list, b: list, t: float) -> list:
    return [x * (1 - t) + y * t for x, y in zip(a, b)]


def add_object(sc: bpy.types.Scene, o: dict) -> None:
    mesh = bpy.data.meshes.new(o["name"])
    mesh.from_pydata([tuple(v) for v in o["vertices"]], [], o["faces"])
    body = bpy.data.objects.new(o["name"], mesh)
    sc.collection.objects.link(body)
    flat = len(o["faces"]) == 1
    # translucent faces: hidden edges stay visible through them (six faces can be counted)
    body.data.materials.append(material(o["name"] + "_f", mix(o["face"], o["edge"], 0.55 if flat else 0.4), 1.0 if flat else 0.42))
    if flat:
        sol = body.modifiers.new("t", "SOLIDIFY")
        sol.thickness = 0.04
    edges = bpy.data.objects.new(o["name"] + "_e", mesh.copy())
    sc.collection.objects.link(edges)
    wire = edges.modifiers.new("w", "WIREFRAME")
    wire.thickness = 0.075
    wire.use_replace = True
    edges.data.materials.clear()  # mesh.copy() carried the face material in slot 0
    edges.data.materials.append(ink(o["name"] + "_e", o["edge"]))


def build(scene: dict, samples: int) -> None:
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    sc.render.engine = "CYCLES"
    prefs = bpy.context.preferences.addons["cycles"].preferences
    prefs.compute_device_type = "METAL"
    prefs.get_devices()
    for d in prefs.devices:
        d.use = True
    sc.cycles.device = "GPU"
    sc.cycles.samples = samples
    sc.cycles.use_denoising = True
    sc.cycles.max_bounces = 4
    sc.cycles.denoiser = "OPENIMAGEDENOISE"
    sc.render.film_transparent = True
    sc.view_settings.view_transform = "Standard"  # AgX (default) washes the role colours to grey
    sc.render.resolution_x, sc.render.resolution_y = scene["camera"]["res"]

    world = bpy.data.worlds.new("w")
    world.color = (1.0, 1.0, 1.0)
    bg = world.node_tree.nodes["Background"]
    bg.inputs["Color"].default_value = (1, 1, 1, 1)
    bg.inputs["Strength"].default_value = 0.55  # white studio fill: no hard black sides
    sc.world = world

    for o in scene["objects"]:
        add_object(sc, o)

    bpy.ops.mesh.primitive_plane_add(size=200, location=(0, 0, -0.003))  # just below the bases
    bpy.context.active_object.is_shadow_catcher = True

    sun = bpy.data.objects.new("sun", bpy.data.lights.new("sun", "SUN"))
    sun.data.energy = 2.6
    sun.data.angle = 0.35
    sun.rotation_euler = (0.55, 0.15, 2.2)  # from the upper left of the viewer
    sc.collection.objects.link(sun)

    cam = bpy.data.objects.new("cam", bpy.data.cameras.new("cam"))
    cam.data.type = "ORTHO"
    cam.data.ortho_scale = scene["camera"]["ortho_scale"]
    x, y, z = (Vector(c) for c in scene["camera"]["rot_columns"])
    loc = Vector(scene["camera"]["location"])
    cam.matrix_world = Matrix(
        ((x[0], y[0], z[0], loc[0]), (x[1], y[1], z[1], loc[1]), (x[2], y[2], z[2], loc[2]), (0, 0, 0, 1))
    )
    sc.collection.objects.link(cam)
    sc.camera = cam


def main() -> None:
    argv = sys.argv[sys.argv.index("--") + 1 :]
    scene = json.load(open(argv[0]))
    out = argv[1]
    build(scene, int(argv[2]) if len(argv) > 2 else 96)
    sc = bpy.context.scene
    rx, ry = scene["camera"]["res"]

    def px(v: list) -> list:
        c = world_to_camera_view(sc, sc.camera, Vector(v))  # (0..1, 0..1) from bottom-left
        return [c.x * rx, (1 - c.y) * ry]

    proj = {o["name"]: [px(v) for v in o["vertices"]] for o in scene["objects"]}
    proj["anchors"] = {k: px(v) for k, v in scene["anchors"].items()}
    json.dump(proj, open(out.replace(".png", ".px.json"), "w"))
    sc.render.filepath = out
    bpy.ops.render.render(write_still=True)


main()
