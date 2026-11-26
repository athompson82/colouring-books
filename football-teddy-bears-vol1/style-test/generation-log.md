# Style Test – Generation Log (2026-11-26)

Model: **Runway – Nano Banana 2.1** (`nano-banana-2.1`), 2K, ratio 3:4 → 1792 × 2400 px PNG
Cost: **6 credits per image** (confirmed by balance: 55,791 → 55,737) · **Total: 54 credits**

| File | Scene | Style | Runway task ID | Credits |
|---|---|---|---|---|
| 05-game-face_styleA.png | Game Face | A – Plush athletic | afdde760-5cb6-455c-a3b2-d0999dfc9041 | 6 |
| 05-game-face_styleB.png | Game Face | B – Comic muscular | bffb7466-b05b-4007-9ddc-6869db921fcd | 6 |
| 05-game-face_styleC.png | Game Face | C – Hybrid mascot | 3b228795-6625-4d70-b85a-c934bb8dd34b | 6 |
| 18-stiff-arm_styleA.png | Stiff Arm | A – Plush athletic | 4450d1b0-0d66-47e6-a9e0-a7cf40b5f1a7 | 6 |
| 18-stiff-arm_styleB.png | Stiff Arm | B – Comic muscular | 013e5b9e-32b9-4696-8cbf-060651cec6a9 | 6 |
| 18-stiff-arm_styleC.png | Stiff Arm | C – Hybrid mascot | d56a27a5-4b0e-4abf-9e3b-dd8555ea55b8 | 6 |
| 06-tunnel_styleA.png | Through the Tunnel | A – Plush athletic | 5ff6b387-6408-46ef-ba55-2a9f0eca84f7 | 6 |
| 06-tunnel_styleB.png | Through the Tunnel | B – Comic muscular | c62ecfb1-6901-457a-977f-fea22cfd55e5 | 6 |
| 06-tunnel_styleC.png | Through the Tunnel | C – Hybrid mascot | a3537f41-097f-4a6b-85f8-38fedeebf7b7 | 6 |

## How the prompts are built
Each prompt is **[Scene] + [Character style] + [Line art rules]**, joined in that order exactly as below.

### Scene blocks
**Game Face:** Colouring book page, portrait. Chest-up poster portrait of a teddy bear football linebacker: thick neck, broad powerful shoulders in shoulder pads, plain jersey with stripe trim and a hollow outlined number 54, eye black stripes drawn as outlined shapes, plain helmet with face mask and chin strap tucked under one arm, intense stare straight at the viewer, simple outlined burst rays behind.

**Stiff Arm:** Colouring book page, portrait. Full-body football action: a compact, powerful teddy bear running back with a low centre of gravity and thick legs, football held high and tight in one arm, delivering a stiff arm into the face mask of a leaner, longer-limbed teddy bear safety who is lunging to tackle him; turf chunks flying from cleats, outlined motion lines, a yard line on the field, low dramatic camera angle. Both wear plain helmets with face masks, shoulder pads under plain striped jerseys with hollow outlined numbers 22 and 31, football pants with knee pads, gloves and cleats.
*(Style B version: "outlined motion and impact lines" and "low dramatic camera angle with foreshortening".)*

**Through the Tunnel:** Colouring book page, portrait. A team of teddy bear football players charging out of a stadium tunnel toward the viewer: a quarterback in front with a raised fist, behind him a huge heavy offensive lineman, a tall lean wide receiver and a stocky linebacker — clearly different body types for different positions. Plain helmets with face masks, shoulder pads under plain striped jerseys with hollow outlined numbers, football pants, cleats. Swirling smoke drawn as outlined cloud shapes around their feet, stadium light beams drawn as outlined rays, detailed tunnel walls with concrete blocks and railings, crowd in the stands beyond drawn as outlined figures.
*(Style B version adds: ", dramatic foreshortened comic-book perspective".)*

### Character style blocks
**A – Plush athletic:** CHARACTER STYLE: recognizable plush teddy bear(s) with athletic proportions: plush body shapes, clearly visible stitched seams along the muzzle(s), ears, chest/limbs, round eyes with determined brows, round ears, short snout(s) with stitched nose(s); athletic/broad-shouldered, not chubby, not babyish, not realistic grizzly bear(s).

**B – Comic muscular:** CHARACTER STYLE: muscular comic-book teddy bear athlete(s): heroic exaggerated proportions, powerful chest/arms/legs, fierce intense expression(s), dynamic comic-book energy; still unmistakably teddy bear(s) with round ears, short rounded muzzle(s) and stylized plush fur edges, not realistic grizzly bear(s).

**C – Hybrid mascot:** CHARACTER STYLE: a hybrid of recognizable teddy bear features (round ears, short rounded muzzle(s), small stitched nose(s), a few subtle seam lines) and a competitive sports-mascot aesthetic: confident athletic build(s), sharp determined brows, bold graphic shapes like a modern team mascot illustration, cool and competitive rather than cute; not realistic grizzly bear(s).

### Line art rules block (all images)
LINE ART RULES: pure black outlines on pure white only; no grayscale, no shading, no gradients, no hatching, no solid black filled areas — every shape is an open outlined region that can be coloured in [Game Face adds: ", including eye black, face mask bars and pupils kept small"; Tunnel adds: "— the tunnel interior must be drawn as outlined shapes, not filled black"]. Bold clean outer contours with thinner interior detail lines, detailed but uncluttered, appropriate for teens and adults. White background, keep a clear margin around the art. Accurate American football gear [Stiff Arm: "and technique"]. No text, no logos, no brand marks, no team names [Tunnel adds: ", no signage"].

(Exact full prompts are also stored on each Runway task and can be retrieved by task ID.)
