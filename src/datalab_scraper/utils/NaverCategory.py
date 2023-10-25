import os
import json

class NaverCategory:
    def __init__(self):
        self.path = os.getcwd()

        with open(self.path + "/src/datalab_scraper/json/cid_list.json", "r", encoding="UTF-8") as f:
            self.cate_dict = json.load(f)['category_list']

    def get_cid_list(self):
        cid_list = []
        for cate_lev1 in self.cate_dict['childList']:
            cid_list.append((cate_lev1['cid'], cate_lev1['name']))
            for cate_lev2 in cate_lev1['childList']:
                cid_list.append((cate_lev2['cid'], cate_lev2['name']))
                for cate_lev3 in cate_lev2['childList']:
                    cid_list.append((cate_lev3['cid'], cate_lev3['name']))
        return cid_list
        
# for test
def main():
    cid_list = NaverCategory().get_cid_list()
    for cid, cname in cid_list:
        print(cid, cname)
    print(len(cid_list))
    
if __name__ == '__main__':
    main()
