# 设计师:Pan YuDong
# 编写者:God's hand
# 时间:2022/6/29 21:43
import Model.UserbasedCF as UbCF


data_filename = '../data/Github/data_demo.csv'
usercf = UbCF.UserbasedCF()
usercf.generate_dataset(data_filename, pivot=0.5)
usercf.calc_user_sim()

usercf.evaluate()



