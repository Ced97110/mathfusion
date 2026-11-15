// Copyright: Your Name. Apache 2.0
// Director of « Vent de travers », version 2: one Babylon engine, two scenes (CARTE 1 unit = 1 km,
// PROCHE 1 unit = 1 m), cuts with a short dip to black, post-processing per scene, the HTML text
// system, the sound and the film clock. Every picture is a pure function of the film time t.
// Sibling modules (carte.js, proche.js, avion.js) are loaded dynamically; a missing one is replaced
// by a plain stand-in so the director can run alone.

import { COULEUR, DUREE, PLANS, chargerDonnees, etat, prog, smooth } from './communs.js';
import { creerTexte } from './texte.js';
import { creerRendu, projectionDecalee } from './rendu.js';
import { PISTES, mixage } from './son.js';

export { mixage } from './son.js';

const V = (x, y, z) => new BABYLON.Vector3(x, y, z);
const avertir = (...a) => console.warn('[vent-de-travers]', ...a);

/** Scene changes: dip of 0.4 s in total, black exactly on the cut. */
const COUPES_SCENE = [PLANS.question.t[0], PLANS.pose.t[0]];
/** Cut inside PROCHE (balloon -> aeroplane), shorter dip, unless proche.js lists its own cuts. */
const COUPES_PROCHE = [PLANS.avion.t[0]];

/** Dip-to-black opacity at film time t (pure). */
export function voile(t, coupesProche = COUPES_PROCHE) {
  let v = 0;
  for (const c of COUPES_SCENE) v = Math.max(v, 1 - smooth(Math.abs(t - c) / 0.2));
  for (const c of coupesProche) v = Math.max(v, 0.85 * (1 - smooth(Math.abs(t - c) / 0.12)));
  return v;
}

/** Dynamic import that never throws: a missing sibling is logged and replaced. */
async function charger(chemin, fabrique, ...args) {
  try {
    const mod = await import(chemin);
    if (typeof mod[fabrique] !== 'function') { avertir(`${chemin} : ${fabrique} absent`); return { mod, obj: null }; }
    return { mod, obj: await mod[fabrique](...args) };
  } catch (err) {
    avertir(`${chemin} non chargé :`, err);
    return { mod: null, obj: null };
  }
}

/** Meshes from a module field that may be an array, a mesh, or a function returning them. */
function maillages(x) {
  const v = typeof x === 'function' ? x() : x;
  return (Array.isArray(v) ? v : [v]).flat().filter((m) => m && typeof m.getClassName === 'function');
}

// ------------------------------------------------------------------ stand-ins (tests without siblings)
function secoursCarte(engine) {
  const scene = new BABYLON.Scene(engine);
  scene.useRightHandedSystem = true;
  scene.clearColor = new BABYLON.Color4(0.05, 0.07, 0.06, 1);
  const camera = new BABYLON.FreeCamera('carteCam', V(0, 400, 0), scene);
  camera.mode = BABYLON.Camera.ORTHOGRAPHIC_CAMERA;
  camera.upVector = V(0, 0, -1);
  camera.setTarget(V(0, 0, 0));
  camera.minZ = 1; camera.maxZ = 1000;
  new BABYLON.HemisphericLight('carteCiel', V(0, 1, 0), scene);
  const ligne = (nom, couleur) => {
    const m = BABYLON.MeshBuilder.CreateLines(nom, { points: [V(0, 1, 0), V(1, 1, 0)], updatable: true }, scene);
    m.color = BABYLON.Color3.FromHexString(couleur);
    return m;
  };
  const fl = { air: ligne('air', COULEUR.bleu), vent: ligne('vent', COULEUR.violet), sol: ligne('sol', COULEUR.vert) };
  return {
    scene, camera,
    maj(t, e) {
      const aspect = engine.getAspectRatio(camera);
      const demi = 150;
      camera.orthoLeft = -demi; camera.orthoRight = demi;
      camera.orthoTop = demi / aspect; camera.orthoBottom = -demi / aspect;
      const poser = (m, [a, b], vis) => {
        BABYLON.MeshBuilder.CreateLines(null, { points: [V(a.x, 1, a.z), V(b.x, 1, b.z)], instance: m });
        m.visibility = vis;
      };
      poser(fl.air, e.flecheAir, e.hAir > 0 ? 1 : 0);
      poser(fl.vent, e.flecheVent, e.hVent > 0 ? 1 : 0);
      poser(fl.sol, e.flecheSol, e.visVert);
    },
    etiquettes(e) {
      const mi = ([a, b]) => ({ x: (a.x + b.x) / 2, y: 0, z: (a.z + b.z) / 2 });
      const out = [];
      if (e.hAir > 0) out.push({ texte: 'sans vent : 220 km', couleur: 'bleu', pos: mi(e.flecheAir) });
      if (e.hVent > 0) out.push({ texte: 'vent : 34 km', couleur: 'violet', pos: mi(e.flecheVent) });
      if (e.visVert > 0) out.push({ texte: 'trajet réel', couleur: 'vert', pos: mi(e.flecheSol), opacite: e.visVert });
      return out;
    },
  };
}

function secoursProche(engine) {
  const scene = new BABYLON.Scene(engine);
  scene.useRightHandedSystem = true;
  scene.clearColor = new BABYLON.Color4(0.42, 0.55, 0.7, 1);
  const camera = new BABYLON.FreeCamera('procheCam', V(0, 6, 30), scene);
  camera.minZ = 0.1; camera.maxZ = 5000;
  new BABYLON.HemisphericLight('procheCiel', V(0.2, 1, 0.3), scene);
  const sol = BABYLON.MeshBuilder.CreateGround('procheSol', { width: 2000, height: 2000 }, scene);
  const mat = new BABYLON.StandardMaterial('procheSolMat', scene);
  mat.diffuseColor = new BABYLON.Color3(0.25, 0.4, 0.2);
  sol.material = mat;
  const boule = BABYLON.MeshBuilder.CreateSphere('procheBallon', { diameter: 2 }, scene);
  return {
    scene, camera,
    maj(t) {
      boule.position.set(Math.sin(t) * 6, 3 + t * 0.5, 0);
      camera.position.set(Math.cos(t * 0.2) * 30, 8, Math.sin(t * 0.2) * 30);
      camera.setTarget(boule.position);
    },
  };
}

// ------------------------------------------------------------------ post-processing
const GRAIN_GLSL = `precision highp float;
varying vec2 vUV;
uniform sampler2D textureSampler;
uniform float graine;
uniform float force;
uniform vec2 taille;
float h(vec2 p) { p = fract(p * vec2(0.1031, 0.1030) + graine); p += dot(p, p.yx + 33.33); return fract((p.x + p.y) * p.x); }
void main(void) {
  vec4 c = texture2D(textureSampler, vUV);
  vec2 px = floor(vUV * taille);
  float n = h(px) + h(px + vec2(37.0, 91.0)) - 1.0;
  float l = dot(c.rgb, vec3(0.2126, 0.7152, 0.0722));
  gl_FragColor = vec4(c.rgb + n * force * (0.3 + l) * (1.1 - l), c.a);
}`;

/**
 * Pipeline of one scene: optional SSAO2, then DefaultRenderingPipeline (tone mapping, bloom), a glow
 * layer for the given meshes only, and a deterministic film grain seeded by the frame number.
 */
function habiller(engine, sc, nom, o) {
  const scene = sc.scene;
  const camera = sc.camera || scene.activeCamera;
  const r = { camera, graine: 0, glow: null, ssao: null, pipeline: null };
  if (!camera) return r;
  if (o.pipeline === false) return habillerLeger(engine, scene, camera, nom, o, r);
  if (o.ssao && engine.webGLVersion >= 2 && BABYLON.SSAO2RenderingPipeline) {
    try {
      const ssao = new BABYLON.SSAO2RenderingPipeline(`${nom}Ssao`, scene, { ssaoRatio: o.horsLigne ? 1 : 0.5, blurRatio: 1 }, [camera]);
      ssao.radius = 1.6; // metres
      ssao.totalStrength = 0.85;
      ssao.samples = o.horsLigne ? 32 : 12;
      ssao.maxZ = 400;
      ssao.expensiveBlur = true;
      r.ssao = ssao;
    } catch (err) { avertir('SSAO2 :', err); }
  }
  const p = new BABYLON.DefaultRenderingPipeline(`${nom}Rendu`, true, scene, [camera]);
  p.samples = o.horsLigne ? 1 : 4;
  p.fxaaEnabled = !o.horsLigne; // offline: the accumulation does the anti-aliasing
  p.bloomEnabled = true;
  p.bloomThreshold = o.bloomSeuil;
  p.bloomWeight = o.bloomPoids;
  p.bloomKernel = 64;
  p.bloomScale = 0.5;
  p.grainEnabled = false; // built-in grain is animated by wall time: replaced by a pure one below
  p.chromaticAberrationEnabled = false;
  p.imageProcessingEnabled = true;
  const ip = p.imageProcessing;
  ip.toneMappingEnabled = true;
  ip.toneMappingType = o.tonalite;
  ip.contrast = o.contraste;
  ip.exposure = 1;
  ip.vignetteEnabled = o.vignette > 0;
  ip.vignetteWeight = o.vignette;
  r.pipeline = p;

  // glow only on the meshes the modules declare (lights, arrows); created when the first one exists
  const vus = new Set();
  r.ajouterLumineux = (listes) => {
    for (const m of listes.flatMap(maillages)) {
      if (vus.has(m)) continue;
      if (!r.glow) {
        r.glow = new BABYLON.GlowLayer(`${nom}Glow`, scene, {
          camera, blurKernelSize: 48, mainTextureRatio: o.horsLigne ? 1 : 0.5, mainTextureSamples: o.horsLigne ? 1 : 4,
        });
        r.glow.intensity = o.glow;
      }
      vus.add(m);
      r.glow.addIncludedOnlyMesh(m);
    }
  };
  r.ajouterLumineux(o.lumineux);

  BABYLON.Effect.ShadersStore.grainFilmFragmentShader = GRAIN_GLSL;
  const g = new BABYLON.PostProcess(`${nom}Grain`, 'grainFilm', ['graine', 'force', 'taille'], null, 1.0, camera);
  g.onApply = (eff) => {
    eff.setFloat('graine', r.graine);
    eff.setFloat('force', o.grain);
    eff.setFloat2('taille', g.width, g.height);
  };
  return r;
}

/**
 * Light dressing for a scene that owns its own pipeline (proche.js) or must not be tone-mapped
 * (carte.js writes final sRGB): only the glow layer for declared meshes and the pure film grain.
 */
function habillerLeger(engine, scene, camera, nom, o, r) {
  const vus = new Set();
  r.ajouterLumineux = (listes) => {
    for (const m of listes.flatMap(maillages)) {
      if (vus.has(m)) continue;
      if (!r.glow) {
        r.glow = new BABYLON.GlowLayer(`${nom}Glow`, scene, {
          camera, blurKernelSize: 32, mainTextureRatio: o.horsLigne ? 1 : 0.5, mainTextureSamples: o.horsLigne ? 1 : 4,
        });
        r.glow.intensity = o.glow;
      }
      vus.add(m);
      r.glow.addIncludedOnlyMesh(m);
    }
  };
  r.ajouterLumineux(o.lumineux);
  if (o.grain > 0) {
    BABYLON.Effect.ShadersStore.grainFilmFragmentShader = GRAIN_GLSL;
    const g = new BABYLON.PostProcess(`${nom}Grain`, 'grainFilm', ['graine', 'force', 'taille'], null, 1.0, camera);
    g.onApply = (eff) => {
      eff.setFloat('graine', r.graine);
      eff.setFloat('force', o.grain);
      eff.setFloat2('taille', g.width, g.height);
    };
  }
  return r;
}

// ------------------------------------------------------------------ sound (two real recordings)
function creerSon() {
  const s = { actif: true, ctx: null, pistes: null };
  s.preparer = () => {
    if (s.ctx) return;
    const AC = window.AudioContext || window.webkitAudioContext;
    if (!AC) return;
    s.ctx = new AC();
    s.maitre = s.ctx.createGain();
    s.maitre.gain.value = s.actif ? 1 : 0;
    s.maitre.connect(s.ctx.destination);
    const piste = (fichier) => {
      const el = new Audio(fichier);
      el.preload = 'auto';
      const gain = s.ctx.createGain();
      gain.gain.value = 0;
      s.ctx.createMediaElementSource(el).connect(gain);
      gain.connect(s.maitre);
      return { el, gain, joue: false };
    };
    s.pistes = { vent: piste(PISTES.vent.fichier), moteur: piste(PISTES.moteur.fichier) };
  };
  /** Follows mixage(t): gains, and the position inside each recording. */
  s.maj = (t, enLecture) => {
    if (!s.ctx || !s.pistes) return;
    const m = mixage(t);
    const ct = s.ctx.currentTime;
    const caler = (p, gain, source) => {
      p.gain.gain.setTargetAtTime(gain, ct, 0.05);
      const doit = enLecture && s.actif && source !== null;
      if (doit) {
        if (Math.abs(p.el.currentTime - source) > 0.15) p.el.currentTime = source;
        if (!p.joue) { p.joue = true; p.el.play().catch(() => { p.joue = false; }); }
      } else if (p.joue) { p.joue = false; p.el.pause(); }
    };
    caler(s.pistes.vent, m.vent, m.sourceVent);
    caler(s.pistes.moteur, m.moteur, m.sourceMoteur);
  };
  s.basculer = () => {
    s.actif = !s.actif;
    s.preparer();
    if (s.ctx && s.ctx.state === 'suspended') s.ctx.resume();
    if (s.maitre) s.maitre.gain.setTargetAtTime(s.actif ? 1 : 0, s.ctx.currentTime, 0.05);
    return s.actif;
  };
  return s;
}

// ------------------------------------------------------------------ entry point
export async function main() {
  const params = new URLSearchParams(location.search);
  const $ = (id) => document.getElementById(id);
  const tDemande = params.has('t') ? Number(params.get('t')) : null;
  const horsLigne = params.get('rendu') === '1';
  // phone held upright: the vertical layout, unless a format is asked for explicitly
  const vertical = params.get('format') === 'vertical'
    || (!params.has('format') && !horsLigne && window.innerHeight > window.innerWidth * 1.15);
  const enPause = horsLigne || params.get('pause') === '1' || Number.isFinite(tDemande);
  if (horsLigne) document.body.classList.add('rendu');

  for (const zone of document.querySelectorAll('[data-sources]')) zone.appendChild($('modeleSources').content.cloneNode(true));

  const d = await chargerDonnees();
  const cadre = $('cadre');
  const canvas = $('scene');
  const engine = new BABYLON.Engine(canvas, true, {
    preserveDrawingBuffer: true, stencil: true, antialias: true, powerPreference: 'high-performance', useHighPrecisionFloats: true,
  }, false);
  const dpr = window.devicePixelRatio || 1;
  engine.setHardwareScalingLevel(horsLigne ? 1 : 1 / Math.min(dpr, 1.5));

  // size the frame before the scenes exist: render targets created at build time take this size
  /** Frame aspect (width / height): 16:9, or upright from 9:16 down to 9:19.5 (a phone's full height). */
  const rapport = (W, H) => (vertical ? Math.min(9 / 16, Math.max(9 / 19.5, W / H)) : 16 / 9);
  {
    const r = rapport(window.innerWidth, window.innerHeight);
    const w0 = Math.floor(Math.min(window.innerWidth, window.innerHeight * r));
    Object.assign(cadre.style, { width: `${w0}px`, height: `${Math.floor(w0 / r)}px` });
    engine.resize();
  }

  // ---------------------------------------------------------------- the two scenes
  const { obj: carteMod } = await charger('./carte.js', 'creerCarte', engine, d);
  const qualite = horsLigne ? 'film' : 'direct';
  const { obj: procheMod } = await charger('./proche.js', 'creerProche', engine, d, { qualite });
  const carte = carteMod && carteMod.scene ? carteMod : secoursCarte(engine);
  const proche = procheMod && procheMod.scene ? procheMod : secoursProche(engine);
  const { obj: avion } = procheMod ? await charger('./avion.js', 'creerAvion', proche.scene, d, { qualite }) : { obj: null };
  if (avion && avion.noeud) {
    try { if (typeof proche.ajouterAvion === 'function') proche.ajouterAvion(avion.noeud, {
      nezX: true, roueBas: 0, essieu: 0, attitudeInterne: true, sansOmbres: true, tToucher: avion.phases && avion.phases.tToucher,
    }); } catch (err) { avertir('ajouterAvion :', err); }
    try { if (typeof avion.setOmbres === 'function' && proche.ombres) avion.setOmbres(proche.ombres); } catch (err) { avertir('setOmbres :', err); }
  }
  const coupesProche = Array.isArray(proche.coupes) ? proche.coupes : COUPES_PROCHE;

  // vertical: the map turns if carte.js can; otherwise it is shown in a 16:9 band (letterbox)
  let bandeCarte = false;
  if (vertical) {
    if (typeof carte.setVertical === 'function') carte.setVertical(true);
    else bandeCarte = true;
    if (typeof proche.setVertical === 'function') proche.setVertical(true);
  }
  const camCarte = () => carte.scene.activeCamera || carte.camera;
  if (bandeCarte && camCarte()) {
    const hb = (9 / 16) * (9 / 16); // 16:9 band across a 9:16 frame
    camCarte().viewport = new BABYLON.Viewport(0, (1 - hb) / 2, 1, hb);
  }

  const habits = {
    proche: habiller(engine, proche, 'proche', {
      horsLigne, ssao: false, pipeline: proche.pipeline ? false : undefined, tonalite: BABYLON.ImageProcessingConfiguration.TONEMAPPING_ACES, contraste: 1.08,
      bloomSeuil: 0.82, bloomPoids: 0.22, vignette: 1.4, grain: 0.012, glow: 0.6,
      lumineux: [avion && avion.lumineux, proche.lumineux],
    }),
    carte: habiller(engine, carte, 'carte', {
      horsLigne, ssao: false, pipeline: carteMod ? false : undefined, tonalite: BABYLON.ImageProcessingConfiguration.TONEMAPPING_KHR_PBR_NEUTRAL, contraste: 1.0,
      bloomSeuil: 0.9, bloomPoids: 0.12, vignette: 0.8, grain: 0, glow: 0.55,
      lumineux: [carte.lumineux, carte.fleches],
    }),
  };

  if (proche.pipeline && horsLigne) proche.pipeline.fxaaEnabled = false; // the accumulation anti-aliases

  // ---------------------------------------------------------------- frame layout and text
  const texte = creerTexte(cadre, d, etat(DUREE - 0.01, d));
  const fixe = { largeur: 0, hauteur: 0 };
  function cadrer() {
    const W = fixe.largeur || window.innerWidth;
    const H = fixe.hauteur || window.innerHeight;
    const ratio = rapport(W, H);
    const w = Math.floor(Math.min(W, H * ratio));
    const h = Math.floor(w / ratio);
    Object.assign(cadre.style, {
      width: `${w}px`, height: `${h}px`,
      left: `${fixe.largeur ? 0 : Math.floor((W - w) / 2)}px`, top: `${fixe.hauteur ? 0 : Math.floor((H - h) / 2)}px`,
    });
    engine.resize();
    texte.dimensionner(w, h, vertical);
  }
  cadrer();
  window.addEventListener('resize', cadrer);

  // ---------------------------------------------------------------- one picture = f(t)
  const erreurs = new Set();
  const essayer = (cle, f) => {
    try { return f(); } catch (err) {
      if (!erreurs.has(cle)) { erreurs.add(cle); avertir(`${cle} :`, err); }
      return undefined;
    }
  };
  const etatFilm = (t) => ({ ...etat(t, d), vertical, horsLigne });
  const noir = new BABYLON.Color4(0, 0, 0, 1);

  /** Renders the engine canvas at time t; jitter = sub-pixel projection offset (offline mode). */
  function dessiner(t, jitter) {
    const e = etatFilm(t);
    const sc = e.scene === 'carte' ? carte : proche;
    const habit = habits[e.scene];
    essayer(`${e.scene}.maj`, () => sc.maj(t, e));
    if (sc === proche && avion && typeof avion.maj === 'function') essayer('avion.maj', () => avion.maj(t, e, e.plan === 'pose' ? 'approche' : 'croisiere'));
    habit.graine = (Math.floor(t * 30) % 977) / 977;
    const cam = sc.scene.activeCamera || sc.camera;
    if (sc === carte && bandeCarte) {
      engine.setViewport(new BABYLON.Viewport(0, 0, 1, 1));
      engine.clear(noir, true, true, true);
    }
    if (jitter && cam) {
      cam.computeWorldMatrix(true);
      const pr = cam.getProjectionMatrix(true);
      cam.freezeProjectionMatrix(projectionDecalee(pr, jitter.dx, jitter.dy, engine.getRenderWidth(), engine.getRenderHeight()));
    }
    essayer(`${e.scene}.render`, () => sc.scene.render());
    if (jitter && cam) cam.unfreezeProjectionMatrix();
    return e;
  }

  /** CARTE world point -> CSS px inside the frame (or null when behind the camera). */
  const tmpV = V(0, 0, 0);
  function projeter(p) {
    const cam = camCarte();
    if (!cam || !p) return null;
    tmpV.set(p.x, typeof p.y === 'number' ? p.y : 0, p.z);
    const w = engine.getRenderWidth();
    const h = engine.getRenderHeight();
    const s = BABYLON.Vector3.Project(tmpV, BABYLON.Matrix.IdentityReadOnly, carte.scene.getTransformMatrix(), cam.viewport.toGlobal(w, h));
    if (!(s.z >= 0 && s.z <= 1)) return null;
    const k = cadre.clientWidth / w;
    return { x: s.x * k, y: s.y * k };
  }

  /** HTML layer for time t (drawn once per frame, never accumulated). */
  const elVoile = $('voile');
  function majTexte(t) {
    const e = etatFilm(t);
    let etiquettes = [];
    let obstacles = [];
    if (e.scene === 'carte') {
      const cam = camCarte();
      if (cam) {
        essayer('carte.maj', () => carte.maj(t, e));
        cam.unfreezeProjectionMatrix();
        carte.scene.updateTransformMatrix(true);
      }
      if (typeof carte.etiquettes === 'function') etiquettes = essayer('carte.etiquettes', () => carte.etiquettes(e)) || [];
      if (typeof carte.obstacles === 'function') {
        obstacles = (essayer('carte.obstacles', () => carte.obstacles(e)) || []).map((o) => {
          const p = projeter({ x: o.x, y: 0, z: o.z });
          const q = p && projeter({ x: o.x + (o.r || 0), y: 0, z: o.z });
          return p ? { x: p.x, y: p.y, rayon: q ? Math.hypot(q.x - p.x, q.y - p.y) : 0 } : null;
        }).filter(Boolean);
      }
    }
    essayer('texte', () => texte.maj(t, e, { etiquettes, projeter, obstacles }));
    elVoile.style.opacity = voile(t, coupesProche).toFixed(3);
  }

  // ---------------------------------------------------------------- clock and controls
  const son = creerSon();
  const horloge = { t: 0, lecture: false, attente: -1 }; // attente: seconds held on the last frame
  const bLecture = $('bLecture');
  const majBoutons = () => { bLecture.textContent = horloge.lecture ? 'Pause' : 'Lecture'; };
  const ecranFin = $('fin');

  function montrer(t) {
    dessiner(t, null);
    majTexte(t);
  }
  function seek(t) {
    horloge.t = Math.min(DUREE, Math.max(0, Number(t) || 0));
    montrer(horloge.t);
    son.maj(horloge.t, horloge.lecture);
    if (!horsLigne) ecranFin.classList.add('cache'); // shown only when playback ends (see the loop)
    horloge.attente = -1;
    return horloge.t;
  }
  function lire() {
    if (horloge.t >= DUREE) horloge.t = 0;
    horloge.attente = -1;
    ecranFin.classList.add('cache');
    son.preparer();
    if (son.ctx && son.ctx.state === 'suspended') son.ctx.resume();
    horloge.lecture = true;
    majBoutons();
  }
  function pause() {
    horloge.lecture = false;
    son.maj(horloge.t, false);
    majBoutons();
  }

  if (!horsLigne) {
    engine.runRenderLoop(() => {
      if (horloge.lecture) {
        horloge.t += Math.min(engine.getDeltaTime() / 1000, 0.1);
        if (horloge.t >= DUREE) {
          horloge.t = DUREE;
          horloge.lecture = false;
          horloge.attente = 0;
          majBoutons();
        }
      } else if (horloge.attente >= 0 && horloge.t >= DUREE) {
        // the last frame (final rule on its plate) is held 3 s before the end screen covers it
        horloge.attente += Math.min(engine.getDeltaTime() / 1000, 0.1);
        if (horloge.attente >= 3) { horloge.attente = -1; ecranFin.classList.remove('cache'); }
      }
      montrer(horloge.t);
      son.maj(horloge.t, horloge.lecture);
    });
  }

  bLecture.addEventListener('click', () => (horloge.lecture ? pause() : lire()));
  const rejouer = () => { seek(0); lire(); };
  $('bRejouer').addEventListener('click', rejouer);
  $('bRejouerFin').addEventListener('click', rejouer);
  const bSon = $('bSon');
  bSon.addEventListener('click', () => bSon.setAttribute('aria-pressed', String(son.basculer())));
  window.addEventListener('keydown', (ev) => {
    if (ev.code !== 'Space' || ev.target !== document.body) return;
    ev.preventDefault();
    if (horloge.lecture) pause(); else lire();
  });
  // controls fade out while the film plays and nobody moves the pointer
  const barre = $('barre');
  let repos = 0;
  const reveiller = () => {
    barre.classList.remove('repos');
    clearTimeout(repos);
    repos = setTimeout(() => { if (horloge.lecture) barre.classList.add('repos'); }, 2500);
  };
  window.addEventListener('pointermove', reveiller);
  window.addEventListener('pointerdown', reveiller);

  // ---------------------------------------------------------------- offline render
  const rendu = creerRendu({
    moteur: engine,
    toile: $('accum'),
    dimensionner(l, h) {
      if (fixe.largeur === l && fixe.hauteur === h) return;
      fixe.largeur = l;
      fixe.hauteur = h;
      engine.setHardwareScalingLevel(1); // 1 render pixel per CSS pixel (the renderer uses deviceScaleFactor 1)
      cadrer();
    },
    dessiner: (t, jitter) => { dessiner(t, jitter); },
    texte: (t) => { horloge.t = t; majTexte(t); },
  });

  // ---------------------------------------------------------------- ready: compile every shot once
  async function prechauffer() {
    for (const p of Object.values(PLANS)) montrer((p.t[0] + p.t[1]) / 2);
    await Promise.all([carte.scene.whenReadyAsync(), proche.scene.whenReadyAsync()].map((x) => x.catch(() => {})));
    for (const p of Object.values(PLANS)) montrer((p.t[0] + p.t[1]) / 2);
    await new Promise((r) => requestAnimationFrame(() => requestAnimationFrame(r)));
    // glow meshes a module may only create during its first maj()
    habits.proche.ajouterLumineux?.([avion && avion.lumineux, proche.lumineux]);
    habits.carte.ajouterLumineux?.([carte.lumineux, carte.fleches]);
    seek(Number.isFinite(tDemande) ? tDemande : 0);
    return true;
  }
  const pret = prechauffer();

  window.film = {
    pret,
    duree: DUREE,
    get t() { return horloge.t; },
    seek,
    lire,
    pause,
    /** Offline: resolves when the page shows the accumulated frame for time t. */
    rendre: (t, options) => rendu.rendre(t, options),
    mixage,
    vertical,
    /** for tuning from the console */
    interne: { engine, carte, proche, avion, habits },
  };

  // ---------------------------------------------------------------- start screen
  const depart = $('depart');
  const etatChargement = $('etatChargement');
  const bLancer = $('bLancer');
  if (enPause) depart.classList.add('cache');
  await pret.catch((err) => { etatChargement.textContent = `Erreur : ${err.message || err}`; });
  etatChargement.textContent = '';
  bLancer.disabled = false;
  bLancer.addEventListener('click', () => { depart.classList.add('cache'); lire(); reveiller(); }, { once: true });
  majBoutons();
  return window.film;
}
