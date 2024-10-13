import sys

sys.path.append("auxiliary/")
from render import render_meteorite_model

# reusable function
render_meteorite_model(
    dl_path="kernels/dsk/",
    model_filename="didymos_g_01165mm_spc_0000n00000_v003.obj",
    model_url="https://naif.jpl.nasa.gov/pub/naif/pds/pds4/dart/dart_spice/spice_kernels/dsk/",
    output_gif_name=f"didymos.gif"
)