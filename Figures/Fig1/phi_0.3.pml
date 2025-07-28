load ./4ake_5unit0.pdb, ake
load ./crowd_140.pdb, crowder

remove resn OTH and Z>0
# remove resn OTH within 20 of ldh

select CORE, ake and resi 1-29+68-117+161-214
select NMPbd, ake and resi 30-67
select LIDbd, ake and resi 118-167

disable LIDbd

bg_color white
hide everything 

alter crowder, vdw=8
show spheres, crowder
set sphere_mode, 4
set sphere_quality, 4
#set sphere_transparency, 0.3
color palegreen, crowder

alter ake, vdw=2
show spheres, ake
# set cartoon_rect_length, 1.5
# set cartoon_oval_length, 1.5
# set cartoon_rect_width, 0.3
# set cartoon_oval_width, 0.3
# set cartoon_loop_radius, 0.3
# set cartoon_highlight_color, [0.95, 0.95, 0.95]

color oxygen, LIDbd
color nitrogen, NMPbd
color hydrogen, CORE

set ray_opaque_background, off
set orthoscopic, 0
set ray_shadow, off
set depth_cue, 1
set orthoscopic, off
set valence, off

set antialias, 3
set light_count, 3
set ambient, 0.4
set ray_trace_mode, 1
set spec_count, 5
set shininess, 50
set specular, 1
set reflect, 0.3


### cut below here and paste into script ###
set_view (\
     0.992750525,   -0.065156728,    0.101003341,\
     0.037828121,    0.966989636,    0.251991183,\
    -0.114088409,   -0.246343687,    0.962443411,\
     0.000001013,   -0.000003551, -365.263397217,\
     1.075775981,    6.434647560,   -1.713133216,\
   304.127258301,  426.399475098,  -20.000000000 )
### cut above here and paste into script ###

viewport 1024, 1024
# draw 1024, 1024, 8

ray 1600, 1600
png x3.png, dpi=600
quit
