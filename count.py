import csv
from model.general_recommender import SGA
from data import dataset
class count(object):
    def __init__(self, conf):
        self.dataset = conf["data.input.dataset"]
        self.user_degree = self.dataset.get_user_degree()
        self.item_degree = self.dataset.get_item_degree()


    def write2csv(self):
        with open("%s_user.csv" % (self.dataset), "w") as f:
            writer = csv.writer(f)
            for key, value in self.user_degree:
                writer.writerow([key,value])
        f.close()

        with open("%s_item.csv" % (self.dataset), "w") as f:
            writer = csv.writer(f)
            for key, value in self.item_degree:
                writer.writerow([key, value])
        f.close()

count.write2csv()






