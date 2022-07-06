# 设计师:Pan YuDong
# 编写者:God's hand
# 时间:2022/6/18 0:58
import Model.UserbasedCF_demo as UbCF


data_filename = '../data/Movie/ratings.dat'
usercf = UbCF.UserBasedCF()
usercf.generate_dataset(data_filename, pivot=0.6)
usercf.calc_user_sim()
usercf.evaluate()

