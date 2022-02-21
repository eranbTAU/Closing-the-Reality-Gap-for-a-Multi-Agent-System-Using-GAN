from torch.utils.data import DataLoader
from carnet.data.Cartrajectories import TrajectoryDataset, seq_collate

def data_loader(args, path):
    dset = TrajectoryDataset(path)
    loader = DataLoader(
        dset,
        batch_size=args.batch_size,
        shuffle=True,
        num_workers=args.loader_num_workers,
        collate_fn=seq_collate)
    return dset, loader