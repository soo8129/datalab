from utils.NaverCategory import NaverCategory

def _datalab_scraper():
    while True:
        try:
            urls = NaverCategory().get_cid_list()
            # rank_data = 
            # db_insert(rank_data)
        except Exception as e:
            pass

def main():
    _datalab_scraper()

if __name__ == '__main__':
    main()
