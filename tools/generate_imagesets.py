import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--image_dir", type=str, default="../data/KITTI/object/training/image_2")
parser.add_argument("--imagesets_dir", type=str, default="../data/KITTI/ImageSets")
args = parser.parse_args()

videos = os.listdir(args.image_dir)
for video_id in videos:
    image_ids = os.listdir(os.path.join(args.image_dir, video_id))
    image_ids = sorted([os.path.splitext(image_id)[0] for image_id in image_ids])
    output_dir = os.path.join(args.imagesets_dir, video_id)
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "train.txt"), "w+") as f:
        f.write("\n".join(image_ids))
    with open(os.path.join(output_dir, "val.txt"), "w+") as f:
        f.write("\n".join(image_ids))
