// Copyright: Your Name. Apache 2.0
// « Vent de travers » v2 — PROCHE scene: the radiosonde balloon (white latex, translucent), its neck,
// the cord, the instrument box with its wire antenna, two gloved hands that let go, and the violet
// marker that keeps the balloon visible when it is kilometres away (shot 2).
// Units: metres. Pure function of t: maj(t, e, pose) sets everything.

import { COULEUR, clamp01, smooth } from './communs.js';

const B = globalThis.BABYLON;
const R_BALLON = 0.78; // radius at launch (a 1.5 m sounding balloon)
const COU = 0.16; // neck length below the envelope
const CORDE = 1.6; // neck to instrument box
const N_CORDE = 28;

const V = (x, y, z) => new B.Vector3(x, y, z);

function enveloppe(scene) {
  // teardrop: round top, longer cone toward the neck; local origin at the neck tie, +y up
  const pts = [];
  const n = 72;
  for (let i = 0; i <= n; i++) {
    const th = (i / n) * Math.PI; // 0 = top, PI = bottom
    const bas = th > Math.PI / 2 ? (th - Math.PI / 2) / (Math.PI / 2) : 0;
    const r = R_BALLON * Math.sin(th) * (1 - 0.1 * bas * bas);
    const y = R_BALLON * 1.22 - R_BALLON * Math.cos(th) * (1 + 0.32 * bas);
    pts.push(V(Math.max(r, 0.022), y + COU, 0));
  }
  pts.push(V(0.02, COU * 0.5, 0), V(0.016, 0, 0));
  const m = B.MeshBuilder.CreateLathe('ballon', { shape: pts, tessellation: 128, sideOrientation: B.Mesh.DOUBLESIDE }, scene);
  return m;
}

function caisse(scene) {
  const g = new B.TransformNode('sonde', scene);
  const corps = B.MeshBuilder.CreateBox('sondeCorps', { width: 0.075, height: 0.27, depth: 0.055 }, scene);
  corps.position.y = -0.135;
  const mat = new B.PBRMaterial('matSonde', scene);
  mat.albedoColor = new B.Color3(0.78, 0.78, 0.76);
  mat.metallic = 0; mat.roughness = 0.55;
  corps.material = mat;
  corps.parent = g;
  const capot = B.MeshBuilder.CreateBox('sondeCapot', { width: 0.079, height: 0.035, depth: 0.059 }, scene);
  capot.position.y = -0.02;
  const matC = new B.PBRMaterial('matCapot', scene);
  matC.albedoColor = new B.Color3(0.05, 0.05, 0.055);
  matC.metallic = 0; matC.roughness = 0.5;
  capot.material = matC; capot.parent = g;
  // wire antenna hanging below, and the sensor boom
  const fil = B.MeshBuilder.CreateTube('antenne', { path: [V(0, -0.27, 0), V(0.004, -0.42, 0.002), V(0.01, -0.62, 0.006)], radius: 0.0012, tessellation: 5 }, scene);
  const matF = new B.PBRMaterial('matAntenne', scene);
  matF.albedoColor = new B.Color3(0.55, 0.52, 0.45); matF.metallic = 0.8; matF.roughness = 0.35;
  fil.material = matF; fil.parent = g;
  const bras = B.MeshBuilder.CreateTube('capteur', { path: [V(0, -0.03, 0.028), V(0, 0.09, 0.07)], radius: 0.003, tessellation: 6 }, scene);
  bras.material = matC; bras.parent = g;
  return { g, maillages: [corps, capot, fil, bras] };
}

/** A gloved fist around a vertical axis (local Y). Palm on the -X side; curl 1 = closed, 0 = open. */
function main(scene, nom, matGant, matManche) {
  const root = new B.TransformNode(nom, scene);
  const paume = B.MeshBuilder.CreateCapsule(`${nom}Paume`, { radius: 0.03, height: 0.105, tessellation: 20, subdivisions: 4 }, scene);
  paume.scaling.set(0.72, 1, 1.3);
  paume.position.set(-0.048, -0.005, 0.0);
  paume.material = matGant; paume.parent = root;
  const doigts = [];
  const longs = [[0.045, 0.028, 0.024], [0.05, 0.031, 0.025], [0.047, 0.029, 0.024], [0.037, 0.023, 0.021]];
  for (let k = 0; k < 4; k++) {
    const seg = longs[k].map((L, i) => {
      const c = B.MeshBuilder.CreateCapsule(`${nom}D${k}${i}`, { radius: 0.0098 - i * 0.0008, height: L + 0.018, tessellation: 12, subdivisions: 2, orientation: V(1, 0, 0) }, scene);
      c.material = matGant; c.parent = root;
      return { c, L };
    });
    doigts.push({ seg, y: 0.03 - k * 0.0215, base: V(-0.042, 0.03 - k * 0.0215, 0.033) });
  }
  const pouce = [0.034, 0.03].map((L, i) => {
    const c = B.MeshBuilder.CreateCapsule(`${nom}P${i}`, { radius: 0.011, height: L + 0.02, tessellation: 12, subdivisions: 2, orientation: V(1, 0, 0) }, scene);
    c.material = matGant; c.parent = root;
    return { c, L };
  });
  // cuff and forearm sleeve (built in world space by maj)
  const manche = B.MeshBuilder.CreateCylinder(`${nom}Manche`, { height: 1, diameterTop: 0.105, diameterBottom: 0.075, tessellation: 24 }, scene);
  manche.material = matManche;
  const poignet = B.MeshBuilder.CreateCylinder(`${nom}Poignet`, { height: 1, diameterTop: 0.07, diameterBottom: 0.062, tessellation: 20 }, scene);
  poignet.material = matGant;

  const tmp = new B.Matrix();
  /** Chain of phalanges from `base` along `dir`, each joint bent by `pli` radians about local Y. */
  const chaine = (segs, base, dir0, pli) => {
    let p = base.clone();
    let a = Math.atan2(-dir0.z, dir0.x);
    for (const { c, L } of segs) {
      const d = V(Math.cos(a), 0, -Math.sin(a));
      c.position.copyFrom(p.add(d.scale(L * 0.5)));
      c.rotation.set(0, a, 0);
      p = p.add(d.scale(L));
      a += pli;
    }
  };
  /**
   * @param {BABYLON.Vector3} pos fist centre (world)
   * @param {BABYLON.Vector3} axeX local X in world (from palm toward the held object)
   * @param {number} serre 1 closed … 0 open
   * @param {BABYLON.Vector3} coude elbow (world) for the sleeve
   */
  function poser(pos, axeX, serre, coude) {
    const y = V(0, 1, 0);
    const x = axeX.subtract(y.scale(B.Vector3.Dot(axeX, y))).normalize();
    const z = B.Vector3.Cross(x, y);
    root.position.copyFrom(pos);
    root.rotationQuaternion = B.Quaternion.RotationQuaternionFromAxis(x, y, z);
    for (const d of doigts) chaine(d.seg, d.base, V(1, 0, 0), serre * 1.25 + 0.12);
    chaine(pouce, V(-0.04, 0.06, -0.03), V(0.6, 0, 0.8).normalize(), -(serre * 0.9 + 0.1));
    // wrist on the palm's far side, then the sleeve to the elbow
    root.computeWorldMatrix(true);
    const poing = B.Vector3.TransformCoordinates(V(-0.075, -0.03, 0), root.getWorldMatrix());
    const tube = (m, a, b) => {
      const d = b.subtract(a);
      const L = d.length();
      m.position.copyFrom(a.add(b).scale(0.5));
      m.scaling.set(1, L, 1);
      const up = d.normalize();
      const ref = Math.abs(up.y) > 0.9 ? V(1, 0, 0) : V(0, 1, 0);
      const ax = B.Vector3.Cross(ref, up).normalize();
      const az = B.Vector3.Cross(ax, up);
      m.rotationQuaternion = B.Quaternion.RotationQuaternionFromAxis(ax, up, az);
    };
    const dirCoude = coude.subtract(poing).normalize();
    const finPoignet = poing.add(dirCoude.scale(0.09));
    tube(poignet, finPoignet, poing);
    tube(manche, coude, finPoignet.subtract(dirCoude.scale(0.02)));
    tmp.copyFrom(root.getWorldMatrix());
  }
  const maillages = [paume, manche, poignet, ...doigts.flatMap((d) => d.seg.map((s) => s.c)), ...pouce.map((s) => s.c)];
  return { root, poser, maillages };
}

/**
 * @param {BABYLON.Scene} scene
 * @param {{ ombres: BABYLON.CascadedShadowGenerator }} o
 */
export function creerBallon(scene, o) {
  const ballon = enveloppe(scene);
  const mat = new B.PBRMaterial('matLatex', scene);
  mat.albedoColor = new B.Color3(0.86, 0.84, 0.79);
  mat.metallic = 0;
  mat.roughness = 0.34;
  mat.subSurface.isTranslucencyEnabled = true;
  mat.subSurface.translucencyIntensity = 0.85;
  mat.subSurface.tintColor = new B.Color3(1.0, 0.9, 0.76);
  mat.subSurface.minimumThickness = 0;
  mat.subSurface.maximumThickness = 0.6;
  mat.sheen.isEnabled = true;
  mat.sheen.intensity = 0.25;
  mat.sheen.color = new B.Color3(1, 0.97, 0.92);
  ballon.material = mat;

  const lien = B.MeshBuilder.CreateTorus('lien', { diameter: 0.04, thickness: 0.012, tessellation: 24 }, scene);
  const matLien = new B.PBRMaterial('matLien', scene);
  matLien.albedoColor = new B.Color3(0.75, 0.73, 0.68); matLien.metallic = 0; matLien.roughness = 0.8;
  lien.material = matLien;

  const chemin0 = Array.from({ length: N_CORDE }, (_, i) => V(0, -i * 0.05, 0));
  let corde = B.MeshBuilder.CreateTube('corde', { path: chemin0, radius: 0.0016, tessellation: 6, updatable: true }, scene);
  corde.material = matLien;

  const sonde = caisse(scene);
  const matGant = new B.PBRMaterial('matGant', scene);
  matGant.albedoColor = new B.Color3(0.045, 0.047, 0.05);
  matGant.metallic = 0; matGant.roughness = 0.62;
  matGant.sheen.isEnabled = true; matGant.sheen.intensity = 0.35; matGant.sheen.color = new B.Color3(0.6, 0.6, 0.62);
  const matManche = new B.PBRMaterial('matManche', scene);
  matManche.albedoColor = new B.Color3(0.055, 0.06, 0.045);
  matManche.metallic = 0; matManche.roughness = 0.9;
  const mainA = main(scene, 'mainA', matGant, matManche);
  const mainB = main(scene, 'mainB', matGant, matManche);

  // violet marker: ring + dot, constant size on screen, almost no haze (alpha = fog weight)
  B.Effect.ShadersStore.vdtRepereVertexShader = `precision highp float;
attribute vec3 position; attribute vec2 uv; uniform mat4 worldViewProjection; varying vec2 vUv;
void main(void){ vUv = uv * 2.0 - 1.0; gl_Position = worldViewProjection * vec4(position, 1.0); }`;
  // shot 2: the balloon is kilometres away, so it is shown as a large drawn balloon (violet = the
  // air), lit from the upper left, with its neck and a short string: a balloon at a glance.
  B.Effect.ShadersStore.vdtRepereFragmentShader = `precision highp float;
varying vec2 vUv; uniform vec3 uCol; uniform float uVis;
float sdSeg(vec2 p, vec2 a, vec2 b) { vec2 pa = p - a, ba = b - a; float h = clamp(dot(pa, ba) / dot(ba, ba), 0.0, 1.0); return length(pa - ba * h); }
void main(void){
  vec2 p = vUv;
  // envelope: an ellipse narrowing toward the neck (teardrop)
  vec2 q = p - vec2(0.0, 0.22);
  float bas = clamp(-q.y / 0.62, 0.0, 1.0);
  vec2 rr = vec2(0.5 * (1.0 - 0.28 * bas * bas), 0.62);
  float corps = (length(q / rr) - 1.0) * min(rr.x, rr.y);
  float cou = sdSeg(p, vec2(0.0, -0.36), vec2(0.0, -0.46)) - 0.045;
  float x = p.y < -0.46 ? 0.035 * sin((p.y + 0.46) * 14.0) : 0.0;
  float fil = abs(p.x - x) - 0.012;
  fil = max(fil, max(p.y - (-0.46), -0.96 - p.y));
  float d = min(min(corps, cou), fil);
  float aa = fwidth(d);
  float a = (1.0 - smoothstep(-aa, aa, d)) * uVis;
  if (a < 0.5) discard;
  // shading of the envelope as a sphere lit from the upper left, dark rim for contrast
  vec2 n2 = clamp(q / rr, -1.0, 1.0);
  vec3 n = vec3(n2, sqrt(max(0.0, 1.0 - dot(n2, n2))));
  float lum = 0.45 + 0.75 * max(0.0, dot(n, normalize(vec3(-0.45, 0.55, 0.7))));
  float reflet = pow(max(0.0, dot(n, normalize(vec3(-0.35, 0.45, 0.82)))), 40.0);
  vec3 c = corps < 0.0 ? uCol * lum + vec3(2.2) * reflet : uCol * 0.7;
  float bord = smoothstep(-0.05, -0.012, corps) * step(corps, 0.0);
  c = mix(c, uCol * 0.35, bord);
  gl_FragColor = vec4(c, 0.1); // alpha = fog weight: the balloon stays clear of the haze
}`;
  const matRep = new B.ShaderMaterial('repere', scene, { vertex: 'vdtRepere', fragment: 'vdtRepere' }, {
    attributes: ['position', 'uv'], uniforms: ['worldViewProjection', 'uCol', 'uVis'],
  });
  matRep.backFaceCulling = false;
  const vio = B.Color3.FromHexString(COULEUR.violet).toLinearSpace().scale(2.2);
  matRep.setColor3('uCol', vio);
  matRep.setFloat('uVis', 1);
  const repere = B.MeshBuilder.CreatePlane('repereBallon', { size: 1 }, scene);
  repere.material = matRep;
  repere.billboardMode = B.Mesh.BILLBOARDMODE_ALL;
  repere.isPickable = false;

  for (const m of [ballon, lien, corde, ...sonde.maillages, ...mainA.maillages, ...mainB.maillages]) {
    m.isPickable = false;
    m.receiveShadows = true;
    o.ombres.addShadowCaster(m);
  }
  ballon.receiveShadows = false; // a smooth envelope: self-shadow steps on its terminator otherwise

  const cordeChemin = chemin0.map((p) => p.clone());
  function majCorde(a, b) {
    const d = B.Vector3.Distance(a, b);
    const sag = d < CORDE ? 0.5 * Math.sqrt(CORDE * CORDE - d * d) : 0;
    for (let i = 0; i < N_CORDE; i++) {
      const s = i / (N_CORDE - 1);
      const p = B.Vector3.Lerp(a, b, s);
      p.y -= sag * 4 * s * (1 - s);
      cordeChemin[i].copyFrom(p);
    }
    corde = B.MeshBuilder.CreateTube('corde', { path: cordeChemin, radius: 0.0016, tessellation: 6, instance: corde });
  }

  /**
   * Pose for shots 1 and 2.
   * @param {number} t film time
   * @param {any} e etat(t, d)
   * @param {{ plan: string, prise: BABYLON.Vector3, h: BABYLON.Vector3, r: BABYLON.Vector3, vent: BABYLON.Vector3,
   *   ballonLoin: BABYLON.Vector3|null, camera: BABYLON.Camera }} p
   *   prise = grip point of the neck, h = horizontal view direction, r = camera right, vent = ground wind (m/s)
   * @returns {BABYLON.Vector3} balloon centre
   */
  function maj(t, e, p) {
    const proche = p.plan === 'lacher';
    for (const m of [lien, corde, ...sonde.maillages, ...mainA.maillages, ...mainB.maillages]) m.setEnabled(proche);
    ballon.setEnabled(p.plan === 'lacher' || p.plan === 'derive');
    repere.setEnabled(p.plan === 'derive');
    let centre = null;
    if (proche) {
      // physics of the release (starts with e.lacher): 2.5 m/s² until 5 m/s, drifting with the ground wind
      const tau = Math.max(0, t - 1.2);
      const v = 5;
      const ta = v / 2.5;
      const monte = tau < ta ? 1.25 * tau * tau : 1.25 * ta * ta + v * (tau - ta);
      const derive = p.vent.scale(0.55 * tau * clamp01(tau / 0.8));
      const ouvre = smooth((t - 1.2) / 0.35);
      const cou = p.prise.add(V(0, 0.07 + monte, 0)).add(derive);
      // the envelope leans with the wind and breathes a little
      const pench = 0.18 + 0.03 * Math.sin(t * 1.9) + 0.1 * clamp01(tau);
      const axe = V(0, 1, 0).add(p.vent.normalize().scale(pench)).normalize();
      const z = B.Vector3.Cross(V(1, 0, 0), axe).normalize();
      const x = B.Vector3.Cross(axe, z);
      ballon.position.copyFrom(cou);
      ballon.rotationQuaternion = B.Quaternion.RotationQuaternionFromAxis(x, axe, z);
      const w = 0.018 * Math.sin(t * 6.3) + 0.012 * Math.sin(t * 9.7 + 1.0);
      ballon.scaling.set(1 + w, 1 - w * 1.4, 1 - w * 0.6);
      lien.position.copyFrom(cou.add(V(0, 0.01, 0)));
      // instrument box: hangs CORDE below the neck, swinging after the jerk of the release
      const sw = 0.28 * Math.exp(-tau * 1.1) * Math.sin(tau * 3.4) * clamp01(tau * 3);
      const dirB = V(0, -1, 0).add(p.h.scale(-sw)).add(p.vent.normalize().scale(-0.12 * clamp01(tau))).normalize();
      const boite = cou.add(dirB.scale(CORDE));
      sonde.g.position.copyFrom(boite.add(V(0, 0.01, 0)));
      sonde.g.rotation.set(sw * 0.6, 0.6 + 0.4 * Math.sin(t * 0.8), sw * 0.3);
      majCorde(cou, boite);
      // hands: A around the neck, B around the cord lower down; both open and drop away
      // the hands open wide and drop away: the gesture reads even when they are small in frame
      const chute = V(0, -0.16 * ouvre, 0);
      const vers = p.r.scale(-1);
      mainA.poser(p.prise.add(chute).add(p.r.scale(0.12 * ouvre)), vers, 1 - ouvre,
        p.prise.add(p.r.scale(0.36)).add(p.h.scale(-0.16)).add(V(0, -0.26, 0)));
      const priseB = p.prise.add(V(0, -0.34, 0)).add(p.r.scale(0.03));
      mainB.poser(priseB.add(chute.scale(1.3)).add(p.r.scale(-0.1 * ouvre)), vers.add(p.h.scale(0.3)), 1 - ouvre,
        priseB.add(p.r.scale(0.34)).add(p.h.scale(-0.1)).add(V(0, -0.22, 0)));
      centre = cou.add(axe.scale(COU + R_BALLON * 1.22));
    } else if (p.plan === 'derive') {
      // shot 2: the balloon at its level, carried by the air
      ballon.rotationQuaternion = B.Quaternion.Identity();
      ballon.scaling.setAll(1);
      ballon.position.copyFrom(p.ballonLoin.subtract(V(0, COU + R_BALLON * 1.22, 0)));
      centre = p.ballonLoin.clone();
      const cam = p.camera;
      // cam.position / cam.fov are set by proche.js before this call (never the derived globalPosition,
      // which still holds the previous frame's camera)
      const dist = B.Vector3.Distance(cam.position, centre);
      const px = 150; // drawn balloon (with string) in pixels at 720 lines: envelope about 125 px at 1080
      const taille = (2 * dist * Math.tan(cam.fov / 2) * px) / 720;
      repere.position.copyFrom(centre);
      repere.scaling.setAll(Math.max(taille, 3.2));
      ballon.setEnabled(false); // sub-pixel at this distance: the drawn balloon stands for it
      matRep.setFloat('uVis', smooth((t - 4.1) / 0.5));
    }
    return centre || null;
  }

  /**
   * Backlit latex glow: light scattered through the envelope, strongest when the sun is behind it.
   * Called after the camera is placed for this frame.
   * @param {BABYLON.Vector3} vise unit view direction of the camera
   * @param {BABYLON.Vector3|null} soleil unit vector toward the sun (null: no glow)
   */
  function eclairer(vise, soleil) {
    const contre = soleil ? Math.max(0, B.Vector3.Dot(vise, soleil)) : 0;
    mat.emissiveColor = new B.Color3(1.0, 0.88, 0.7).scale(0.9 * contre * contre);
  }

  return { ballon, maj, eclairer, repere };
}
