import os
import numpy as np
import open3d as o3d

def pointcloud_recognize(file_path):
    file_type = os.path.splitext(file_path)[-1]
    if file_type =='.npy':
        pcl = np.load(file_path)
    if file_type == '.bin':
        pcl = np.fromfile(file_path, dtype=np.float32, count=-1).reshape(-1, 4)
    return pcl, True