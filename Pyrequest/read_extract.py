import yaml


class read_extract:
    def __init__(self,yaml_file):
        self.yaml_file=yaml_file
# 读取
    def read(self):
        with open(self.yaml_file,encoding='utf-8') as f:
            m=yaml.load(f,yaml.FullLoader)
            print(m)
# 写入
    def write(self):
        with open(self.yaml_file,encoding='utf-8',mode='w') as f:
            data=[{'age': 18}]
            z=yaml.dump(data,f)
if __name__ == '__main__':
    r=read_extract('extract.yaml')
    # r.read()
    r.write()
