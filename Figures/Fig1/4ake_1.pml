load ./4ake_A.pdb, ake

select CORE, resi 1-29+68-117+161-216
select NMPbd, resi 30-67
select LIDbd, resi 118-167

disable LIDbd

bg_color white
hide everything 

show cartoon, ake
set cartoon_rect_length, 1.2
set cartoon_oval_length, 1.2
set cartoon_rect_width, 0.3
set cartoon_oval_width, 0.3
set cartoon_loop_radius, 0.3
set cartoon_highlight_color, [0.95, 0.95, 0.95]

color oxygen, LIDbd
color nitrogen, NMPbd
color hydrogen, CORE

create pr, ake
set solvent_radius, 2.5
show surface, pr
set surface_quality, 1
set transparency, 0.5, pr

set ray_opaque_background, off
set orthoscopic, 0
set ray_shadow, off
set depth_cue, 1
set orthoscopic, off
set valence, off

set antialias, 3
set light_count, 3
set ambient, 0.3
set ray_trace_mode, 1
set spec_count, 5
set shininess, 50
set specular, 1
set reflect, 0.3

### cut below here and paste into script ###
set_view (\
    -0.369208008,   -0.369691044,   -0.852652311,\
     0.214279115,    0.858890831,   -0.465181351,\
     0.904306352,   -0.354454756,   -0.237893373,\
    -0.000002358,    0.000014499, -195.294464111,\
    -4.381158829,   -2.580474615,  -10.971721649,\
   163.390289307,  227.209167480,  -20.000000000 )
### cut above here and paste into script ###

viewport 1024, 1024
# draw 1024, 1024, 8

ray 1600, 1600
png 4ake_1.png, dpi=600
quit
