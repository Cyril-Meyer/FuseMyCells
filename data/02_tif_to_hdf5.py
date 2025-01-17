import os
import h5py
import image

with h5py.File('FuseMyCells.hdf5', 'w') as hdf:
    for organ in ['nucleus', 'membrane']:
        group = hdf.create_group(organ)
        for i in range(500):
            filenameX = f'images/image_{i}_{organ}_angle.tif'
            filenameY = f'images/image_{i}_{organ}_fused.tif'
            if os.path.isfile(filenameX) and os.path.isfile(filenameY):
                X, X_meta = image.imread(filenameX, metadata=True)
                Y, Y_meta = image.imread(filenameY, metadata=True)

                if not X_meta == Y_meta:
                    raise ValueError

                sample = group.create_group(f'image_{i}')
                for k in X_meta.keys():
                    sample.attrs[k] = X_meta[k]

                dsX = sample.create_dataset(f'angle', data=X)
                dsY = sample.create_dataset(f'fused', data=Y)

                hdf.flush()
            exit()
