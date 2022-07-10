# 设计师:Pan YuDong
# 编写者:God's hand
# 时间:2022/6/17 20:13
import random
import math
from operator import itemgetter

from collections import defaultdict

class UserBasedCF():
    ''' TopN recommendation - User Based Collaborative Filtering '''
    def __init__(self):
        self.train_dataset = {}
        self.test_dataset = {}

        self.n_sim_user = 20  # number of similar users
        self.n_rec_item = 10  # number of recommend items

        self.user_sim_mat = {}
        self.item_popular = {}
        self.item_count = 0

        print(f'similar user number = {self.n_sim_user}')
        print(f'recommended item number = {self.n_rec_item}')

    @staticmethod
    def loadfile(filename):
        '''load a file, return a generator'''
        fp = open(filename, 'r')
        for i, line in enumerate(fp):
            yield line.strip('\r\n')
            if i % 1000000 == 0:
                print(f'loading {filename}, {i}')
        fp.close()
        print(f'load{filename} success')

    def generate_dataset(self, filename, pivot=0.7):
        '''load data and split it to training dataset and test dataset'''
        train_dataset_len = 0
        test_dataset_len = 0

        raw_dataset = self.loadfile(filename)
        for line in raw_dataset:
            user, item, rating, _ = line.split('::')
            # split the data by pivot
            if random.random() < pivot:
                self.train_dataset.setdefault(user, {})
                self.train_dataset[user][item] = int(rating)
                train_dataset_len += 1
            else:
                self.test_dataset.setdefault(user, {})
                self.test_dataset[user][item] = int(rating)
                test_dataset_len += 1


        print('split training dataset and test dataset success')
        print(f'length of training dataset: {train_dataset_len}')
        print(f'length of test dataset: {test_dataset_len}')

    def calc_user_sim(self):
        '''calculate user similarity matrix'''
        # build inverse table for item-users
        # key = itemID, value=list of userIDs who have seen this item
        print('building item-users inverse table...')
        item2users = dict()

        for user, items in self.train_dataset.items():
            for item in items:
                # inverse table for item-users
                if item not in item2users:
                    item2users[item] = set()  # make sure no repeated users
                item2users[item].add(user)
                # count item popularity at the same time
                if item not in self.item_popular:
                    self.item_popular[item] = 0
                self.item_popular[item] += 1
        print('build item-users inverse table success')

        # save the total item number, which will be used in evaluation phase
        self.item_count = len(item2users)
        print(f'total item number {self.item_count}')

        # count co-rated items between users
        user_sim_mat = self.user_sim_mat
        print('building user co-rated items matrix...')

        for item, users in item2users.items():
            for u in users:
                user_sim_mat.setdefault(u, defaultdict(int))
                for v in users:
                    if u == v:
                        continue
                    user_sim_mat[u][v] += 1
        print('build user co-rated items matrix success')

        # calculate similarity matrix
        print('calculating user similarity matrix...')
        sim_factor_count = 0
        PRINT_STEP = 200000

        for u, related_users in user_sim_mat.items():
            for v, count in related_users.items():
                user_sim_mat[u][v] = count / math.sqrt(len(self.train_dataset[u]) * len(self.train_dataset[v]))
                sim_factor_count += 1
                if sim_factor_count % PRINT_STEP == 0:
                    print(f'calculating user similarity factor {sim_factor_count}')

        print('calculate user similarity matrix success')
        print(f'Total similarity factor number {sim_factor_count}')

    def recommend(self, user):
        '''Find K similar users and recommend N items'''
        K = self.n_sim_user
        N = self.n_rec_item
        rank = dict()
        watched_items = self.train_dataset[user]

        for similar_user, similar_factor in sorted(self.user_sim_mat[user].items(), key=itemgetter(1), reverse=True)[0:K]:
            for item in self.train_dataset[similar_user]:
                if item in watched_items:
                    continue
                # predict the user's interest for each item
                rank.setdefault(item, 0)
                rank[item] += similar_factor

        # return the N best items
        return sorted(rank.items(), key=itemgetter(1), reverse=True)[0:N]


    def evaluate(self):
        '''print evaluation measurement:precision, recall, coverage and popularity'''
        print('Evaluation start...')

        N = self.n_rec_item
        # variables for precision and recall
        hit = 0
        rec_count = 0
        test_count = 0
        # variables for coverage
        all_rec_items = set()
        # variables for popularity
        popular_sum = 0

        for i, user in enumerate(self.train_dataset):
            if i % 500 == 0:
                print(f'recommend for {i} users')
            test_items = self.test_dataset.get(user, {})  # if user doesn't exist in training dataset, return {}
            rec_items = self.recommend(user)
            # print("rec_items:", rec_items)
            for item, _ in rec_items:
                if item in test_items:
                    hit += 1
                all_rec_items.add(item)
                popular_sum += math.log(1 + self.item_popular[item])
            rec_count += N
            test_count += len(test_items)

        print("item_popular:", self.item_popular)

        # The ratio of the user's favorite products to all recommended products in the system's recommendation list
        precision = 1.0 * hit / rec_count
        # The ratio of products that users like in the recommendation list to all products that users like in the system
        recall = 1.0 * hit / test_count
        # Describe the ability of a recommendation system to mine the long tail of an item
        coverage = 1.0 * len(all_rec_items) / self.item_count
        # Popularity bias
        popularity = 1.0 * popular_sum / rec_count

        print(f'precision={precision:.4f}, recall={recall:.4f}, coverage={coverage:.4f}, '
              f'popularity={popularity:.4f}')






























