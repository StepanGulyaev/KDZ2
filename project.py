class Project:
    def __init__(self,f1,f2,number):
        self.f1 = f1
        self.f2 = f2
        self.flag_list = []
        self.number = number

    def is_excluded(self):
        if 'x' in self.flag_list:
            return True
        return False

    def add_to_cluster(self,cluster):
        self.cluster = cluster

