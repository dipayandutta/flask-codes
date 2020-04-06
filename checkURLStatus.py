import time
import urllib.request
from threading import Thread

class GetURLThread(Thread):
	def __init__(self,url):
		self.url = url
		super(GetURLThread,self).__init__()

	def run(self):
		response = urllib.request.urlopen(self.url)
		print (self.url , response.getcode())
	'''	
		url_list   = []
		status_list= []

		url_list.append(self.url)
		status_list.append(response.getcode())

		print(url_list)
		print(status_list)
		result_dict = {}
		result_dict = dict(zip(url_list,status_list))
'''
def get_response():

	urls = ['https://dev.to', 'https://www.ebay.com', 'https://www.github.com']	
	start = time.time()
	threads = []
	for url in urls:
		t = GetURLThread(url)
		threads.append(t)
		t.start()
	for t in threads:
		t.join()

	print("Elapsed time: %s"%(time.time()-start))
if __name__ == '__main__':
	get_response()
