import requests
def make_requests(url):
	r = requests.get(url)
	if r.status_code ==200 :
		print("sucess", r.status_code)
	else:
		print("invaild")
make_requests("https://google.com")

	 
		