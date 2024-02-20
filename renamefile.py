import os


def rename_file(path):
    entries = os.listdir(path)
    for entry in entries:   # train or val
        entry_path = os.path.join(path, entry)
        if os.path.isdir(entry_path):
            sub_dirs = os.listdir(entry_path)
            for sub_dir in sub_dirs:  # fight or nonfight
                sub_path = os.path.join(entry_path, sub_dir)
                if os.path.isdir(sub_path):
                    sub_sub_dirs = os.listdir(sub_path)
                    i = 0
                    for sub_sub_dir in sub_sub_dirs:   # .avi
                        sub_path_0 = os.path.join(entry_path,sub_dir)
                        file_path = os.path.join(sub_path_0,sub_sub_dir)
                        train = "train"
                        val = "val"
                        fight = "Fight"
                        nonfight = "NonFight"
                        if train in sub_path_0:
                            if nonfight in sub_path_0:   # 这里有一个小bug是包含nonfight自然也包含fight，因此要先判断nonfight
                                new_file_name = "train_nonfight_" + str(i) + ".avi"
                                new_file_path = os.path.join(sub_path,new_file_name)
                                if os.path.exists(new_file_path):
                                    pass
                                else:
                                    os.rename(file_path,new_file_path)
                                i = i + 1
                            elif fight in sub_path_0:
                                new_file_name = "train_fight_" + str(i) + ".avi"
                                new_file_path = os.path.join(sub_path, new_file_name)
                                if os.path.exists(new_file_path):
                                    pass
                                else:
                                    os.rename(file_path, new_file_path)
                                i = i + 1
                            else:
                                pass
                        elif val in sub_path_0:
                            if nonfight in sub_path_0:
                                new_file_name = "val_nonfight_" + str(i) + ".avi"
                                new_file_path = os.path.join(sub_path, new_file_name)
                                if os.path.exists(new_file_path):
                                    pass
                                else:
                                    os.rename(file_path, new_file_path)
                                i = i + 1
                            elif fight in sub_path_0:
                                new_file_name = "val_fight_" + str(i) + ".avi"
                                new_file_path = os.path.join(sub_path, new_file_name)
                                if os.path.exists(new_file_path):
                                    pass
                                else:
                                    os.rename(file_path, new_file_path)
                                i = i + 1
                            else:
                                pass
                else:
                    pass
        else:
            pass

path = r"E:\datasetProcess\RWF-2000data"
rename_file(path)
