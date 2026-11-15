// Copyright: Your Name. Apache 2.0
// « Vent de travers » v2 — scene PROCHE (shots 1, 2, 3 and 10). 1 unit = 1 metre, +x east, -z north,
// +y up, right-handed. Rendering is a pure function of the film time t: maj(t, e) sets the camera,
// the sun, the ground, the balloon, the aeroplane and the post-processes; nothing reads the clock.
//
// Places (each shot works in its own local frame, so float precision stays at the millimetre):
//   shots 1-3: origin = the balloon launch point at De Bilt (the aeroplane starts above it in shot 3);
//   shot 10:   origin = threshold of runway 09 on its centreline, runway along +x (45 m wide).
//
// The aeroplane node (built by another module, in metres) is expected with its nose along local -Z,
// up +Y, right wing +X, wheels down. ajouterAvion measures its lowest point once; maj then places it
// (shots 3 and 10) and hides it elsewhere. posAvion(t, e) gives the same world position without
// touching the scene (for sound and labels).
//
// Quality: creerProche(engine, d, { qualite: 'film' }) or ?rendu=film in the URL selects the offline
// settings (4096 shadows, 8x MSAA, 56 cloud steps, dense grass). Default is the live setting.

import { PLANS, clamp01, lerp, prog, rad, smooth, smoother } from './communs.js';
import { creerCiel, versSoleil } from './proche-ciel.js';
import { creerSol } from './proche-sol.js';
import { creerHerbe, creerArbres } from './proche-vegetation.js';
import { creerBallon } from './proche-ballon.js';
import { creerFeux } from './proche-piste.js';

const B = globalThis.BABYLON;
const V = (x, y, z) => new B.Vector3(x, y, z);
const UP = V(0, 1, 0);

const ALT_M = 1222; // flight level of the film = altitude of the measured wind (d.vent.altitude_m)
const X_POSE = 200; // touchdown point, metres past the threshold (touchdown zone), on the centreline
const T_POSE_DEF = 2.8; // seconds after 51.2 s at which the wheels touch (overridden by the aeroplane's own timing)
const ESSIEU = 0.3; // main wheels, metres aft of the aeroplane node origin (assumption, see ajouterAvion)

/** Unit horizontal vector toward a compass bearing (degrees clockwise from north). */
const cap = (deg) => V(Math.sin(rad(deg)), 0, -Math.cos(rad(deg)));

/** Humid layers of the sounding (relative humidity >= 93 %), padded to a drawable thickness. */
function couchesHumides(niveaux) {
  const runs = [];
  let cur = null;
  for (const [h, , , rh] of [...niveaux].sort((a, b) => a[0] - b[0])) {
    if (rh >= 93) { if (cur && h - cur[1] < 25) cur[1] = h; else { cur = [h, h]; runs.push(cur); } } else cur = null;
  }
  // measured humid layers, drawn at least 170 m thick so the clouds have volume; the layer under the
  // flight level grows downward (its top stays below the aeroplane), the others upward
  const c = runs.filter((r) => r[0] < 4000).map(([a, b]) => {
    const h0 = a - 15; const h1 = b + 15; const manque = Math.max(0, 170 - (h1 - h0));
    return h1 < ALT_M ? [h0 - manque, h1] : [h0, h1 + manque];
  });
  while (c.length < 2) c.push([9000, 9001]);
  return c.slice(0, 2);
}

/** Aeroplane orientation: heading (deg), pitch and roll (rad, roll > 0 = right wing down). */
function orientation(capDeg, tangage, roulis) {
  const fh = cap(capDeg);
  const rh = B.Vector3.Cross(fh, UP);
  const fwd = fh.scale(Math.cos(tangage)).add(UP.scale(Math.sin(tangage)));
  const upv = UP.scale(Math.cos(tangage)).subtract(fh.scale(Math.sin(tangage)));
  const right = rh.scale(Math.cos(roulis)).subtract(upv.scale(Math.sin(roulis)));
  const up2 = upv.scale(Math.cos(roulis)).add(rh.scale(Math.sin(roulis)));
  return { q: B.Quaternion.RotationQuaternionFromAxis(right, up2, fwd.scale(-1)), fwd, right, up: up2 };
}

/**
 * Aeroplane pose for shots 3 and 10 (pure). Returns null in the other shots.
 * Shot 3: real time, nose at the runway (d.km.faux.cap), moving along the ground vector d.km.faux.sol.
 * Shot 10: driven by e.approche (0 → 1 between 51.2 s and 54.6 s, see communs.js): flare, touchdown on
 * the centreline at X_POSE, de-crab from the 6.4° correction (d.km.bon.virage_deg), roll-out.
 */
function poseAvion(t, e, d, tPose = T_POSE_DEF, interne = false) {
  const k = d.km;
  if (e.plan === 'avion') {
    const tau = t - PLANS.avion.t[0];
    const v = { x: (k.faux.sol.est / 3.6) * tau, z: -(k.faux.sol.nord / 3.6) * tau };
    const tang = rad(0.6 * Math.sin(t * 1.3) + 0.3 * Math.sin(t * 2.9));
    const roul = rad(0.9 * Math.sin(t * 0.9 + 1) + 0.4 * Math.sin(t * 2.3));
    return { contact: V(v.x, ALT_M, v.z), hauteur: null, capDeg: k.faux.cap, tangage: interne ? 0 : tang, roulis: interne ? 0 : roul, centre: true };
  }
  if (e.plan === 'pose') {
    // seconds since the start of the approach progress (extended before 51.2 s with the same rate)
    // e.approche is linear in t over [51.2, 54.6] and frozen after it: use the shot clock instead,
    // so the roll-out keeps moving after 54.6 s.
    const tau = t - PLANS.pose.t[0] - 0.2;
    const T_POSE = tPose;
    let x; let h; let tang;
    if (tau < T_POSE) {
      const r = T_POSE - tau;
      x = X_POSE - 30 * r - 0.25 * r * r;
      h = 4.6 * Math.pow(r / 3.0, 1.8);
      tang = rad(lerp(2, 7, smooth((tau + 0.2) / (T_POSE + 0.2))));
    } else {
      const s = Math.min(tau - T_POSE, 7.5);
      x = X_POSE + 30 * s - 2 * s * s;
      h = 0;
      tang = rad(7 * (1 - smooth(s / 1.2)));
    }
    const crab = k.bon.virage_deg * (1 - smooth((tau + 0.6) / 0.8)); // nose aligned before the wheels touch
    const roul = -rad(1.8) * Math.sin(Math.PI * clamp01((tau - 0.9) / 2.0));
    return { contact: V(x, h, 0), hauteur: h, capDeg: 90 - crab, tangage: interne ? 0 : tang, roulis: interne ? 0 : roul, centre: false };
  }
  return null;
}

/**
 * @param {BABYLON.AbstractEngine} engine
 * @param {any} d data from chargerDonnees()
 * @param {{ qualite?: 'film'|'direct' }} [opts]
 * @returns {{ scene: BABYLON.Scene, camera: BABYLON.FreeCamera, maj: (t:number, e:any) => void,
 *   soleil: BABYLON.DirectionalLight, ombres: BABYLON.CascadedShadowGenerator,
 *   ajouterAvion: (noeud: BABYLON.TransformNode, o?: {roueBas?: number, essieu?: number}) => void,
 *   posAvion: (t:number, e:any) => BABYLON.Vector3|null, posBallon: (t:number, e:any) => BABYLON.Vector3|null,
 *   pipeline: BABYLON.DefaultRenderingPipeline }}
 */
export function creerProche(engine, d, opts = {}) {
  const film = opts.qualite === 'film' || (typeof location !== 'undefined' && /[?&]rendu=film\b/.test(location.search));
  const scene = new B.Scene(engine);
  scene.useRightHandedSystem = true;
  scene.clearColor = new B.Color4(0.55, 0.61, 0.69, 1);
  scene.skipPointerMovePicking = true;
  scene.fogMode = B.Scene.FOGMODE_NONE; // haze is the atmosphere post-process (height fog)

  const camera = new B.FreeCamera('cameraProche', V(0, 2, -5), scene);
  camera.fovMode = B.Camera.FOVMODE_VERTICAL_FIXED;
  camera.minZ = 0.05;
  camera.maxZ = 400000;
  scene.activeCamera = camera;

  const couches = couchesHumides(d.niveaux);
  const ciel = creerCiel(scene, camera, { film, couches });
  const ombres = new B.CascadedShadowGenerator(film ? 4096 : 2048, ciel.soleil, false, camera);
  ombres.numCascades = 4;
  ombres.lambda = 0.88;
  ombres.stabilizeCascades = true;
  ombres.cascadeBlendPercentage = 0.1;
  ombres.depthClamp = true;
  ombres.bias = 0.004;
  ombres.normalBias = 0.03;
  ombres.useContactHardeningShadow = true;
  ombres.contactHardeningLightSizeUVRatio = 0.035;
  ombres.filteringQuality = film ? B.ShadowGenerator.QUALITY_HIGH : B.ShadowGenerator.QUALITY_MEDIUM;
  ombres.darkness = 0;
  ombres.freezeShadowCastersBoundingInfo = true;

  // ground wind (lowest level of the sounding), blowing toward bearing dir + 180, m/s
  const n0 = d.niveaux[0];
  const ventSol = cap(n0[1] + 180).scale(n0[2]);
  // the air of the measured level, m/s (carries clouds and balloon)
  const ventAir = V(d.km.vent.est / 3.6, 0, -d.km.vent.nord / 3.6);

  const sol = creerSol(scene, { ombres, film, couches });
  const herbe = creerHerbe(scene, { film, uSite: sol.uniformes.site, ventSol: { x: ventSol.x / 4, z: ventSol.z / 4 } });
  const arbres = creerArbres(scene);
  const ballon = creerBallon(scene, { ombres });
  const feux = creerFeux(scene, { ombres });
  sol.miroir.renderList.push(ciel.dome, ballon.ballon);

  // ---- post-processes after the atmosphere: depth of field, bloom, tone mapping ---------------
  const pipeline = new B.DefaultRenderingPipeline('procheRendu', true, scene, [camera]);
  // depth of field off: its blur bled the bright haze over the aeroplane's edges (white halo)
  pipeline.depthOfFieldEnabled = false;
  pipeline.depthOfFieldBlurLevel = film ? B.DepthOfFieldEffectBlurLevel.High : B.DepthOfFieldEffectBlurLevel.Medium;
  pipeline.bloomEnabled = true;
  pipeline.bloomThreshold = 1.5; // the sunlit white fuselage stays under it: no halo around the aeroplane
  pipeline.bloomWeight = 0.15;
  pipeline.bloomKernel = 96;
  pipeline.bloomScale = 0.5;
  pipeline.fxaaEnabled = true;
  pipeline.sharpenEnabled = true;
  pipeline.sharpen.edgeAmount = 0.12;
  pipeline.imageProcessingEnabled = true;
  const ip = pipeline.imageProcessing;
  ip.toneMappingEnabled = true;
  ip.toneMappingType = B.ImageProcessingConfiguration.TONEMAPPING_ACES;
  ip.exposure = 1.15;
  ip.contrast = 1.12;
  ip.vignetteEnabled = true;
  ip.vignetteWeight = 1.6;
  ip.vignetteColor = new B.Color4(0, 0, 0, 0);

  let avion = null;
  let avionRoueBas = -1.27;
  let avionEssieu = ESSIEU;
  let tPose = T_POSE_DEF;
  let attitudeInterne = false;

  /**
   * Registers the aeroplane node (created in this scene). Its lowest point is measured at rest unless
   * given: o.roueBas = height of the wheel bottoms in the node frame (m, negative), o.essieu = main
   * wheels' distance aft of the node origin (m).
   */
  function ajouterAvion(noeud, o = {}) {
    if (o.nezX) {
      // the node has its nose on +x and right wing on +z: carry it in a node with nose on -z
      const porteur = new B.TransformNode('avionPorteur', scene);
      noeud.parent = porteur;
      noeud.position.setAll(0);
      noeud.rotationQuaternion = null;
      noeud.rotation.set(0, Math.PI / 2, 0);
      const m = B.Matrix.RotationY(noeud.rotation.y);
      if (B.Vector3.TransformNormal(V(1, 0, 0), m).z > 0) noeud.rotation.y = -Math.PI / 2;
      noeud = porteur;
    }
    if (typeof o.tToucher === 'number') tPose = o.tToucher - PLANS.pose.t[0] - 0.2;
    attitudeInterne = !!o.attitudeInterne;
    avion = noeud;
    const p = noeud.position.clone();
    const q = noeud.rotationQuaternion ? noeud.rotationQuaternion.clone() : null;
    const r = noeud.rotation.clone();
    noeud.position.setAll(0);
    noeud.rotationQuaternion = B.Quaternion.Identity();
    noeud.computeWorldMatrix(true);
    const { min } = noeud.getHierarchyBoundingVectors(true);
    avionRoueBas = o.roueBas ?? min.y;
    avionEssieu = o.essieu ?? ESSIEU;
    noeud.position.copyFrom(p);
    if (q) noeud.rotationQuaternion = q; else { noeud.rotationQuaternion = null; noeud.rotation.copyFrom(r); }
    for (const m of noeud.getChildMeshes(false)) { m.receiveShadows = true; if (!o.sansOmbres) ombres.addShadowCaster(m, false); }
    if (noeud.getClassName && noeud.getClassName() === 'Mesh') ombres.addShadowCaster(noeud, true);
  }

  /** World position of the aeroplane node for (t, e), or null when it is not in the shot. */
  function placementAvion(t, e) {
    const p = poseAvion(t, e, d, tPose, attitudeInterne);
    if (!p) return null;
    const o = orientation(p.capDeg, p.tangage, p.roulis);
    if (p.centre) return { pos: p.contact, q: o.q, o, p };
    // rotate about the main-wheel contact point: node = contact - R * (0, roueBas, essieu)
    const m = new B.Matrix();
    o.q.toRotationMatrix(m);
    const piv = B.Vector3.TransformCoordinates(V(0, avionRoueBas, avionEssieu), m);
    return { pos: p.contact.subtract(piv), q: o.q, o, p };
  }
  const posAvion = (t, e) => { const r = placementAvion(t, e); return r ? r.pos : null; };

  const ballonLoin = (e) => V(d.km.vent.est * 1000 * e.heureBallon, ALT_M, -d.km.vent.nord * 1000 * e.heureBallon);
  const posBallon = (t, e) => (e.plan === 'derive' ? ballonLoin(e) : null);

  // ---- shot 1 geometry: the camera faces the sun so the latex glows against it ----------------
  const s0 = versSoleil(0);
  // the camera looks across the sun (sun behind-left): the balloon is modelled by light, not a flat disc
  const hS = B.Vector3.TransformNormal(V(s0.v.x, 0, s0.v.z).normalize(), B.Matrix.RotationY(2.05));
  const rS = B.Vector3.Cross(hS, UP);
  const prise = V(0, 1.5, 0);

  /** Camera for each shot (pure). Returns position, target, vertical fov, focus distance (m), f-stop. */
  function plan(t, e, centreBallon, placeAvion) {
    if (e.plan === 'lacher') {
      const derive = V(0.012 * Math.sin(t * 0.9), 0.008 * Math.sin(t * 1.3 + 1), 0.01 * Math.sin(t * 0.7 + 2));
      // far enough back that both hands and the whole balloon sit in the upper two thirds of the
      // frame (the caption owns the bottom); then the camera tilts up a little to follow the rise
      const pos = prise.subtract(hS.scale(5.0)).subtract(rS.scale(0.35)).add(V(0, 0.35, 0)).add(derive);
      const suit = smooth((t - 1.5) / 2.1);
      const cible0 = prise.add(V(0, 0.7, 0)).add(hS.scale(0.25));
      const cible = B.Vector3.Lerp(cible0, centreBallon.subtract(V(0, 0.9, 0)), 0.7 * suit);
      const focus = B.Vector3.Distance(pos, B.Vector3.Lerp(prise.add(V(0, 0.45, 0)), centreBallon, suit));
      return { pos, cible, fov: rad(lerp(50, 54, suit)), focus, fStop: 4 };
    }
    if (e.plan === 'derive') {
      const k = smoother(prog(t, PLANS.derive.t[0], PLANS.derive.t[1]));
      const b = ballonLoin(e);
      const pos = B.Vector3.Lerp(V(-1500, 700, -1600), V(-9500, 6400, -9800), k);
      const milieu = V(b.x * 0.5, 0, b.z * 0.5);
      const cible = B.Vector3.Lerp(b, milieu, 0.75 * k);
      return { pos, cible, fov: rad(44), focus: B.Vector3.Distance(pos, b), fStop: 22 };
    }
    if (e.plan === 'avion') {
      const k = smoother(prog(t, PLANS.avion.t[0], PLANS.avion.t[1] - 0.4));
      const P = placeAvion.pos;
      const f = cap(d.km.faux.cap);
      const r = B.Vector3.Cross(f, UP);
      // three-quarter front view sweeping to a three-quarter rear view (runway direction ahead)
      const th = rad(lerp(38, 140, k));
      const R = lerp(17.5, 20.5, k);
      const pos = P.add(f.scale(Math.cos(th) * R)).add(r.scale(Math.sin(th) * R)).add(V(0, lerp(2.4, 4.6, k), 0));
      const cible = P.add(f.scale(lerp(0.6, 3.2, k))).add(V(0, lerp(1.2, 0.9, k), 0));
      return { pos, cible, fov: rad(31), focus: R, fStop: 11 };
    }
    // shot 10: low tracking shot from the south side of the runway, three-quarter rear, the camera
    // rolling with the aeroplane so it stays large in frame (about 60 % of the width)
    const P = placeAvion.pos;
    const k10 = smoother(prog(t, PLANS.pose.t[0], 56.5));
    const pos = V(P.x - lerp(7.5, 4.5, k10), lerp(1.6, 1.3, k10), lerp(22, 20, k10));
    const cible = V(P.x - lerp(1.0, 1.6, k10), P.y + 0.9, P.z);
    return { pos, cible, fov: rad(20), focus: B.Vector3.Distance(pos, cible), fStop: 5.6 };
  }

  const profondeur = scene.enableDepthRenderer(camera, false, true).getDepthMap();
  // the violet marker discards outside its ring: kept out of the depth used by the haze (else a dark box)
  profondeur.renderListPredicate = (m) => m.name !== 'repereBallon';
  let vertical = false;
  /** Phone layout (9:16): the horizontal field is fixed instead, so the subject keeps its width. */
  function setVertical(v) {
    vertical = !!v;
    camera.fovMode = vertical ? B.Camera.FOVMODE_HORIZONTAL_FIXED : B.Camera.FOVMODE_VERTICAL_FIXED;
  }
  function maj(t, e) {
    // the depth map is created before the film frame is sized: keep it at the render size
    const rw = engine.getRenderWidth(); const rh = engine.getRenderHeight();
    if (profondeur.getRenderWidth() !== rw || profondeur.getRenderHeight() !== rh) profondeur.resize({ width: rw, height: rh });
    const nom = e.plan;
    const site = nom === 'pose' ? 1 : 0;
    const placeAvion = placementAvion(t, e);
    // aeroplane
    if (avion) {
      avion.setEnabled(!!placeAvion);
      if (placeAvion) {
        avion.position.copyFrom(placeAvion.pos);
        avion.rotationQuaternion = placeAvion.q;
      }
    }
    // camera (the balloon pose is needed first in shot 1)
    const air = ventAir.scale(nom === 'derive' ? e.heureBallon * 3600 : t);
    let centre = null;
    const camProv = plan(t, e, prise.add(V(0, 1.3, 0)), placeAvion);
    camera.position.copyFrom(camProv.pos);
    camera.fov = camProv.fov;
    if (nom === 'lacher' || nom === 'derive') {
      centre = ballon.maj(t, e, { plan: nom, prise, h: hS, r: rS, vent: ventSol, ballonLoin: nom === 'derive' ? ballonLoin(e) : null, camera, soleil: s0.v });
    } else ballon.maj(t, e, { plan: nom, prise, h: hS, r: rS, vent: ventSol, ballonLoin: null, camera });
    const c = centre ? plan(t, e, centre, placeAvion) : camProv;
    camera.position.copyFrom(c.pos);
    camera.setTarget(c.cible);
    camera.fov = vertical ? 2 * Math.atan(Math.tan(c.fov / 2) * 1.35) : c.fov;
    camera.minZ = nom === 'lacher' ? 0.03 : nom === 'derive' ? 2 : nom === 'avion' ? 0.4 : 0.1;
    camera.getViewMatrix(true);
    camera.getProjectionMatrix(true);
    ballon.eclairer(c.cible.subtract(c.pos).normalize(), nom === 'lacher' ? s0.v : null);

    // sun hour: 12:00 UTC, the hour of the drift in shot 2, arrival time in shot 10
    const heures = nom === 'derive' ? e.heureBallon : nom === 'pose' ? d.km.distance / d.km.bon.vitesse_sol_kmh : 0;
    const s = ciel.maj({ oeil: c.pos, vise: c.cible.subtract(c.pos).normalize(), graine: (t * 30 * 0.6180339887) % 1, heures, air, nuages: nom === 'derive' ? 0.6 : 1, brume: 1, rayons: nom === 'lacher' ? 1.0 : nom === 'avion' ? 0.3 : 0 });
    // shadows: a fixed box around the action of each shot (deterministic, and tight for sharpness)
    ombres.shadowMaxZ = nom === 'lacher' ? 30 : nom === 'derive' ? 260 : nom === 'avion' ? 60 : 70;
    const cc = nom === 'avion' ? placeAvion.pos : nom === 'derive' ? camera.position : c.pos;
    const ext = nom === 'lacher' ? 25 : nom === 'avion' ? 15 : 300;
    ombres.shadowCastersBoundingInfo = new B.BoundingInfo(
      V(cc.x - ext, (nom === 'avion' ? cc.y - 8 : -2), cc.z - ext), V(cc.x + ext, (nom === 'avion' ? cc.y + 8 : 40), cc.z + ext));

    // ground and its graphic lines
    const vio = nom === 'derive' && e.heureBallon > 0 ? [ballonLoin(e).x, ballonLoin(e).z, 3.2, smooth((t - 4.4) / 0.4)] : null;
    const gris = nom === 'avion' ? [0, 0, 1.2, 0.4 * smooth(prog(t, 9.6, 10.8))] : null;
    sol.maj({ site, decalage: site === 1 ? [7300, -4100] : [0, 0], oeil: camera.position, soleil: s.v, air, nuages: nom === 'derive' ? 0.6 : 1, trait: vio, route: gris });
    herbe.maj(t, camera.position, nom === 'lacher' || nom === 'pose' ? 1 : 0);
    arbres.maj(site);
    feux.maj(site === 1);

    // depth of field (millimetres)
    const dof = pipeline.depthOfField;
    if (dof) {
    dof.focalLength = 12 / Math.tan(c.fov / 2);
    dof.fStop = c.fStop;
    dof.focusDistance = Math.max(c.focus, 0.1) * 1000;
    dof.lensSize = 50;
    }
  }

  return { scene, camera, maj, setVertical, soleil: ciel.soleil, ombres, ajouterAvion, posAvion, posBallon, pipeline, ciel, sol };
}
