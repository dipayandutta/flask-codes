import urllib3

urls = ['https://google.com',"https://facebook.com"]
http = urllib3.PoolManager()
result_status = []
for url in urls:
	r = http.request('GET',url)
	result_status.append(r.status)
print (result_status)

result_dict = {}
result_dict = dict(zip(urls,result_status))
print(type(result_dict))

for key,value in result_dict.items():
	print(key)
	print(value)
