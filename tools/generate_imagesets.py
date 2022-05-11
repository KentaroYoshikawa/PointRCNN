import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--image_dir", type=str, default="../data/KITTI/object/training/image_2")
parser.add_argument("--label_dir", type=str, default="../data/KITTI/object/training/label_2")
parser.add_argument("--velodyne_dir", type=str, default="../data/KITTI/object/training/velodyne")
parser.add_argument("--imagesets_dir", type=str, default="../data/KITTI/ImageSets")
parser.add_argument("--fps", type=int, required=True)
args = parser.parse_args()

videos = os.listdir(args.image_dir)
for video_id in videos:
    image_ids = os.listdir(os.path.join(args.image_dir, video_id))
    image_ids = sorted([os.path.splitext(image_id)[0] for image_id in image_ids])
    label_ids = os.listdir(os.path.join(args.label_dir, video_id))
    label_ids = sorted([os.path.splitext(label_id)[0] for label_id in label_ids])
    velodyne_ids = os.listdir(os.path.join(args.velodyne_dir, video_id))
    velodyne_ids = sorted([os.path.splitext(velodyne_id)[0] for velodyne_id in velodyne_ids])

    ids = sorted(list(set(image_ids) & set(label_ids) & set(velodyne_ids)))
    ids = ids[::10 // args.fps]

    output_dir = os.path.join(args.imagesets_dir, video_id)
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "train.txt"), "w+") as f:
        f.write("\n".join(ids))
    with open(os.path.join(output_dir, "val.txt"), "w+") as f:
        f.write("\n".join(ids))
