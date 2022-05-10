import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--src", type=str, default="../data/KITTI/object/training/label")
parser.add_argument("--dst", type=str, default="../data/KITTI/object/training/label_2")
args = parser.parse_args()

videos = os.listdir(args.src)

for video_id in videos:
    output_dir = os.path.join(args.dst, video_id)
    os.makedirs(output_dir, exist_ok=True)

    with open(os.path.join(args.src, video_id, f"{video_id}.txt"), 'r') as f:
        lines = f.readlines()

    frames = {}
    for line in lines:
        split_line = line.strip().split(" ")
        frame_id = int(split_line[0])
        if frame_id not in frames:
            frames[frame_id] = []
        frames[frame_id].append(" ".join(split_line[2:]))

    for frame_id, lines in frames.items():
        with open(os.path.join(output_dir, "%06d.txt" % frame_id), "w+") as f:
            f.write("\n".join(lines))
