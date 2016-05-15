from menpo.io.input.landmark import ljson_importer
from .mesh import assimp_importer, wrl_importer, mjson_importer, obj_importer
from .landmark_mesh import (bnd_importer, lan_importer, lm3_importer,
                            pts_mesh_importer)

mesh_types = {'.dae': assimp_importer,
              '.3ds': assimp_importer,
              '.ase': assimp_importer,
              '.obj': obj_importer,
              '.ifc': assimp_importer,
              '.xgl': assimp_importer,
              '.zgl': assimp_importer,
              '.ply': assimp_importer,
              '.dxf': assimp_importer,
              '.lwo': assimp_importer,
              '.lws': assimp_importer,
              '.lxo': assimp_importer,
              '.stl': assimp_importer,
              '.x': assimp_importer,
              '.ac': assimp_importer,
              '.md5': assimp_importer,
              '.smd': assimp_importer,
              '.vta': assimp_importer,
              '.m3': assimp_importer,
              '.3d': assimp_importer,
              '.b3d': assimp_importer,
              '.q3d': assimp_importer,
              '.q3s': assimp_importer,
              '.nff': assimp_importer,
              '.off': assimp_importer,
              '.raw': assimp_importer,
              '.ter': assimp_importer,
              '.mdl': assimp_importer,
              '.hmp': assimp_importer,
              '.ndo': assimp_importer,
              '.ms3d': assimp_importer,
              '.cob': assimp_importer,
              '.scn': assimp_importer,
              '.bvh': assimp_importer,
              '.csm': assimp_importer,
              '.xml': assimp_importer,
              '.irrmesh': assimp_importer,
              '.irr': assimp_importer,
              '.md2': assimp_importer,
              '.md3': assimp_importer,
              '.pk3': assimp_importer,
              '.mdc': assimp_importer,
              '.wrl': wrl_importer,
              '.mjson': mjson_importer}

mesh_landmark_types = {'.pts3': pts_mesh_importer,
                       '.lm3': lm3_importer,
                       '.lan': lan_importer,
                       '.bnd': bnd_importer,
                       '.ljson': ljson_importer}

