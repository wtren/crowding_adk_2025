load ./1ake_A.pdb, ake
load ./4ake_A.pdb, ref

select CORE0, ref and resi 1-29+68-117+161-214
select CORE, ake and resi 1-29+68-117+161-214
select NMPbd, ake and resi 30-67
select LIDbd, ake and resi 118-167
select AP5, ake and resi 215

pair_fit CORE and name CA, CORE0 and name CA
disable AP5

bg_color white
hide everything 

set_color dblue= [0.05 , 0.19 , 0.57]
set_color blue=  [0.02 , 0.50 , 0.72]
set_color mblue= [0.5  , 0.7  , 0.9 ]
set_color lblue= [0.86 , 1.00 , 1.00]

set_color green= [0.00 , 0.53 , 0.22]
set_color lgreen=[0.50 , 0.78 , 0.50]
set_color yellow=[0.95 , 0.78 , 0.00]
set_color orange=[1.00 , 0.40 , 0.0 ]

# these are trivial
set_color red=   [1.00 , 0.00 , 0.00]
set_color mred=  [1.00 , 0.40 , 0.40]
set_color lred=  [1.00 , 0.80 , 0.80]
set_color vlred= [1.00 , 0.90 , 0.90]
set_color white= [1.00 , 1.00 , 1.00]
set_color vlgray=[0.95 , 0.95 , 0.95]
set_color lgray= [0.90 , 0.90 , 0.90]
set_color gray=  [0.70 , 0.70 , 0.70]
set_color dgray= [0.50 , 0.50 , 0.50]
set_color vdgray=[0.30 , 0.30 , 0.30]
set_color black= [0.00 , 0.00 , 0.00]

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

show sphere, AP5
util.cbac AP5
set sphere_mode, 4
set sphere_quality, 4
set sphere_scale, 0.7

create pr, ake and resi 1-214
set solvent_radius, 2.5
show surface, pr
set surface_quality, 1
set transparency, 0.5, pr

# show sticks, AP5
# set stick_radius, 0.6
# set stick_quality, 40
# util.cnc AP5

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
png 1ake_1.png, dpi=600
quit
