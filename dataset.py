import re
import os
from PIL import Image
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
import torchvision.transforms as transforms


class RWF2000dataset(Dataset):

    def __init__(self, data_dir, transform=None):
        self.label_name = {
            '^fight.*': 1,  # 以 "fight" 开头的标签对应值 1
            '^nonfight.*': 0  # 以 "nonfight" 开头的标签对应值 0
        }
        self.data_info = self.get_img_info(data_dir)
        self.transform = transform

    def __getitem__(self, index):
        path_img, label = self.data_info[index]
        img = Image.open(path_img).convert('RGB')

        if self.transform is not None:
            img = self.transform(img)

        return img, label

    def __len__(self):
        return len(self.data_info)

    def get_img_info(self, data_dir):
        data_info = list()
        for root, dirs, _ in os.walk(data_dir):
            # 遍历下设各个文件夹
            for sub_dir in dirs:
                img_names = os.listdir(os.path.join(root, sub_dir))
                img_names = list(filter(lambda x: x.endswith('.jpg'), img_names))
                # 遍历文件夹中
                for i in range(len(img_names)):
                    img_name = img_names[i]
                    path_img = os.path.join(root, sub_dir, img_name)

                    label = None
                    for pattern, label_value in self.label_name.items():
                        if re.match(pattern, sub_dir):
                            label = label_value
                            break

                    if label is not None:
                        data_info.append((path_img, int(label)))

        return data_info


if __name__ == '__main__':
    # 这个数是瞎编的
    norm_mean = [0.485, 0.456, 0.406]
    norm_std = [0.229, 0.224, 0.225]
    train_transform = transforms.Compose([
        transforms.Resize((32, 32)),
        transforms.RandomCrop(32, padding=4),
        transforms.ToTensor(),
        transforms.Normalize(norm_mean, norm_std),
    ])
    train_data = RWF2000dataset(r"E:\datasetProcess\RWF-2000-picture\train", train_transform)
    train_loader = DataLoader(dataset=train_data, batch_size=4, shuffle=True)
    print("dataset ok!!!")