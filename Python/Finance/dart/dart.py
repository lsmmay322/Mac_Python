import dart_fss as dart

api_key = '218475592ddca934158d40aa18a719b0d2a00a64'
dart.set_api_key(api_key = api_key)

corp_list = dart.get_corp_list()

samsung = corp_list.find_by_corp_name('삼성전자',exactly=True)[0]

fs = samsung.extract_fs(bgn_de = '20120101')

fs.save()