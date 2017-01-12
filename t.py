import codecs
import json

def replace(fname, idx):
    with codecs.open(fname, 'r', encoding='GBK') as fp:
        data = json.load(fp)
        objs = data['data']

        for o in objs:
            if o['name'] == 'XMN-LAB':
                o['id'] = 1
            elif o['id'] == 1 and o['name'] != 'XMN_LAB':
                o['id'] = idx

        # json.dump(data, fp)

    with codecs.open(fname, 'w', encoding='GBK') as fp:
        json.dump(data, fp, indent=4)

def isOpenWhatsNew(fname,False):
    with codecs.open(fname, 'r', encoding='GBK') as fp:
        data = json.load(fp)
        objs = data['data']

        for o in objs:
            if o['name'] == 'XMN-LAB':
                o['id'] = 1
            elif o['id'] == 1 and o['name'] != 'XMN_LAB':
                o['id'] = idx

        # json.dump(data, fp)

    with codecs.open(fname, 'w', encoding='GBK') as fp:
        json.dump(data, fp, indent=4)
    

replace('pre_env.txt', 8)

