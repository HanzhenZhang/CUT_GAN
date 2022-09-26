import shutil

root_target = '/mnt/ssd/zw/contrastive-unpaired-translation/datasets/gta5'
root_original = '/mnt/ssd/zw/gta5/labels'
total = 24966
train_rate = 0.8
test_rate = 0.2
index = int(total * train_rate)
# print(index)
# split train file
for i in range(1, index):
    i = str(i)
    file_name = "0" * (5 - len(i)) + i + ".png"
    original = root_original + "/" + file_name
    target = root_target + "/" + "trainB"
    shutil.copy(original, target)
# split test file
for i in range(index, total + 1):
    i = str(i)
    file_name = "0" * (5 - len(i)) + i + ".png"
    original = root_original + "/" + file_name
    target = root_target + "/" + "testB"
    shutil.copy(original, target)
