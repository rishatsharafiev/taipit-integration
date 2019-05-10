from soap_api import SoapApi

# run every 1 hour 
# 5/10 * * * * /path/to/update_result.py
def main():
    soap_api = SoapApi()
    soap_api.get_client()

    # get from mysql
    item = {
        'MaterialID': '00-06108034',
        'MaterialID': '00-06108035',
    }
    
    result_id = soap_api.get_available_goods_async(item)

    # write to sqlite
    print(result_id)

if __name__ == '__main__':
    main()
