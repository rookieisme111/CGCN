import json
import random

train_path = "./dataset/semeval/train.json"
with open(train_path,'r') as f:
    trian_dict = json.load(f)
#    print(trian_dict)

print(len(trian_dict))

indeces = list(range(len(trian_dict)))
random.shuffle(indeces)
trian_dict=[ trian_dict[i] for i in indeces]

new_train_path="./dataset/semeval/new_train.json"
new_trian_list= trian_dict[:7200]
print(len(new_trian_list))
with open(new_train_path,'w') as f:
    json.dump(new_trian_list,f)

new_dev_path="./dataset/semeval/new_dev.json"
new_dev_list= trian_dict[7200:]
print(len(new_dev_list))
with open(new_dev_path,'w') as f:
    json.dump(new_dev_list,f)