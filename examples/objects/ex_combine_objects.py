"""
Combine multiple objects
========================

This example illustrate
.. image:: ../../picture/picobjects/ex_brain_obj.png
"""
import numpy as np

from visbrain.objects import (BrainObj, ColorbarObj, SceneObj, SourceObj,
                              ImageObj, RoiObj, CrossSecObj, ConnectObj)
from visbrain.io import download_file

"""Get the path to Visbrain data and download deep sources
"""
mat = np.load(download_file('xyz_sample.npz'))
xyz, subjects = mat['xyz'], mat['subjects']
data = np.random.uniform(low=-1., high=1., size=(xyz.shape[0],))

print("""
=============================================================================
                             Default scene
=============================================================================
""")
CAM_STATE = dict(azimuth=0,        # azimuth angle
                 elevation=90,     # elevation angle
                 )
CBAR_STATE = dict(cbtxtsz=12, txtsz=10., width=.1, cbtxtsh=3.,
                  rect=(-.3, -2., 1., 4.))
sc = SceneObj(camera_state=CAM_STATE, size=(1400, 1000))

# print("""
# =============================================================================
#                                fMRI activation
# =============================================================================
# """)
# file = download_file('lh.sig.nii.gz')
# b_obj_fmri = BrainObj('inflated', translucent=False, sulcus=True)
# b_obj_fmri.add_activation(file=file, clim=(5., 20.), hide_under=5,
#                           cmap='viridis', hemisphere='left')
# sc.add_to_subplot(b_obj_fmri, row=0, col=0, row_span=3,
#                   title='fMRI activation', rotate='top')

# print("""
# =============================================================================
#                                Cross-sections
# =============================================================================
# """)
# cs_brod = CrossSecObj('brodmann', interpolation='nearest',
#                       section=(70, 80, 90), cmap='viridis')
# cs_brod.localize_source((-10., -15., 20.))
# sc.add_to_subplot(cs_brod, row=2, col=2, col_span=2, row_span=2,
#                   title='Cross-sections')

# print("""
# ===============================================================================
#                            Region Of Interest (ROI)
# ===============================================================================
# """)
# roi_aal = RoiObj('aal')
# roi_aal.select_roi(select=[29, 30], unique_color=True, smooth=11)
# CAM_STATE_ROI = dict(scale_factor=200 * 100, distance=800 * 100, azimuth=0,
#                      elevation=90)
# sc.add_to_subplot(roi_aal, row=0, col=1,
#                   title='Region Of Interest (ROI)', camera_state=CAM_STATE_ROI)

print("""
=============================================================================
                                    Sources
=============================================================================
""")
s_obj = SourceObj('FirstSources', xyz, data=data)
s_obj.color_sources(data=data, cmap='Spectral_r')
sc.add_to_subplot(s_obj, row=0, col=2, title='Sources')
sc.add_to_subplot(BrainObj('B3'), use_this_cam=True, row=0, col=2)


# print("""
# # =============================================================================
# #                               Connectivity
# # =============================================================================
# """)
# arch = np.load(download_file('phase_sync_delta.npz'))
# nodes, edges = arch['nodes'], arch['edges']
# c_count = ConnectObj('default', nodes, edges, select=edges > .7,
#                      color_by='count', antialias=True, line_width=2.,
#                      dynamic=(.1, 1.))
# s_obj_c = SourceObj('sources', nodes, color='#ab4642', radius_min=5.)
# sc.add_to_subplot(c_count, row=1, col=1, title='3D connectivity')
# sc.add_to_subplot(s_obj_c, row=1, col=1)
# sc.add_to_subplot(BrainObj('B3'), use_this_cam=True, row=1, col=1)

sc.preview()
