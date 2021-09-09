import json
import random

file_path = "./dataset/gcn_dataset.json"
with open(file_path,'r',encoding='utf-8') as f:
    trian_dict = json.load(f)
#    print(trian_dict)

print(len(trian_dict))

samples_num = len(trian_dict)

indeces = list(range(len(trian_dict)))
random.shuffle(indeces)
trian_dict=[ trian_dict[i] for i in indeces]

train_num = int(samples_num * 0.7)
dev_num = int(samples_num * 0.1)

new_train_path="./dataset/traffic/train.json"
new_trian_list= trian_dict[:train_num]
print(len(new_trian_list))
with open(new_train_path,'w',encoding='utf-8') as f:
    json.dump(new_trian_list,f,ensure_ascii=False)

new_dev_path="./dataset/traffic/dev.json"
new_dev_list= trian_dict[train_num:train_num+dev_num]
print(len(new_dev_list))
with open(new_dev_path,'w',encoding='utf-8') as f:
    json.dump(new_dev_list,f,ensure_ascii=False)

new_test_path="./dataset/traffic/test.json"
new_test_list= trian_dict[train_num+dev_num:]
print(len(new_test_list))
with open(new_test_path,'w',encoding='utf-8') as f:
    json.dump(new_test_list,f,ensure_ascii=False)