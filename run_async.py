from soap_api import SoapApi

# run every 1 hour 
# 0 * * * * /path/to/run_async.py
def main():
    soap_api = SoapApi()
    soap_api.get_client()

    item = {
        'MaterialID': '00-06108034',
        'MaterialID': '00-06108035',
    }
    result_id = soap_api.get_available_goods_async(item)
    print(result_id)

if __name__ == '__main__':
    main()
