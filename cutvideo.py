# 这里读取的视频实际上每个都是5s 150帧
import os
import cv2


def split_frames_to_train_val(folder_path, output_folder):
    # 创建 train 和 val 文件夹
    train_folder = os.path.join(output_folder, "train")
    train_fight_folder = os.path.join(train_folder, "fight")
    train_nonfight_folder = os.path.join(train_folder, "nonfight")
    val_folder = os.path.join(output_folder, "val")
    val_fight_folder = os.path.join(val_folder, "fight")
    val_nonfight_folder = os.path.join(val_folder, "nonfight")
    os.makedirs(train_folder, exist_ok=True)
    os.makedirs(train_fight_folder,exist_ok=True)
    os.makedirs(train_nonfight_folder,exist_ok=True)
    os.makedirs(val_folder, exist_ok=True)
    os.makedirs(val_fight_folder,exist_ok=True)
    os.makedirs(val_nonfight_folder,exist_ok=True)

    # 获取指定文件夹中的所有视频文件
    entries = os.listdir(folder_path)
    for entry in entries:   # train or val
        entry_path = os.path.join(folder_path, entry)
        if os.path.isdir(entry_path):
            sub_folders = os.listdir(entry_path)
            for sub_folder in sub_folders: # fight or nonfight
                sub_path = os.path.join(entry_path, sub_folder)
                if os.path.isdir(sub_path):
                    videos = os.listdir(sub_path)
                    for video in videos:
                        video_path = os.path.join(sub_path, video)
                        video_name = os.path.splitext(video)[0]
                        video1 = cv2.VideoCapture(video_path)  # 实体视频
                        frame_count = 0
                        success = True
                        while success:
                            success, image = video1.read()
                            if success:
                                if "train" in video_path:
                                    if "nonfight" in video_path:
                                        output_video_folder = os.path.join(train_nonfight_folder,video_name)
                                        os.makedirs(output_video_folder, exist_ok=True)
                                        output_path = os.path.join(output_video_folder,
                                                                   f"{video_name}_{frame_count}.jpg")
                                    elif "fight" in video_path:
                                        output_video_folder = os.path.join(train_fight_folder, video_name)
                                        os.makedirs(output_video_folder, exist_ok=True)
                                        output_path = os.path.join(output_video_folder,
                                                                   f"{video_name}_{frame_count}.jpg")
                                elif "val" in video_path:
                                    if "nonfight" in video_path:
                                        output_video_folder = os.path.join(val_nonfight_folder, video_name)
                                        os.makedirs(output_video_folder, exist_ok=True)
                                        output_path = os.path.join(output_video_folder,
                                                                   f"{video_name}_{frame_count}.jpg")
                                    elif "fight" in video_path:
                                        output_video_folder = os.path.join(val_fight_folder, video_name)
                                        os.makedirs(output_video_folder, exist_ok=True)
                                        output_path = os.path.join(output_video_folder,
                                                                   f"{video_name}_{frame_count}.jpg")

                                cv2.imwrite(output_path,image)
                                frame_count = frame_count + 1
                        video1.release()
                        print(f"视频 '{video_name}' 的帧数为: {frame_count}")



video_folder_path = r"E:\datasetProcess\RWF-2000-video"  # 视频文件夹路径
output_folder = r"E:\datasetProcess\RWF-2000-picture"  # 存储提取帧的文件夹路径

split_frames_to_train_val(video_folder_path, output_folder)