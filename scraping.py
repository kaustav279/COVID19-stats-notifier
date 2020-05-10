from bs4 import BeautifulSoup
from requests_html import HTMLSession

def get_webpage(link):
	session = HTMLSession()
	resp = session.get(link)
	try:
		resp.html.render(timeout=15)
	except Exception as e:
		print("Issue with render.")
		print(e)

	return resp.html.html

def extract_info(html_page,state):
	bs = BeautifulSoup(html_page, 'html5lib')
	search = bs.select("table tbody tr td")
	size = len(search)

	data = {"India":[] , state:[]}
	for i in range(size):
		reach = search[i].get_text()
		if (reach == "Total" or reach == state):
			if reach == "Total":
				reach = "India"

			for j in range(1,5):
				search_item = search[i+j]
				dpt = search_item.get_text()

				search_span = search_item.select("span")
				if len(search_span) > 0:
					extra_chars_len = len(search_span[0].get_text())
				else:
					extra_chars_len = 0

				if extra_chars_len > 0:
					dpt = dpt[extra_chars_len:]
					#dpt = dpt[:-extra_chars_len]
				
				data[reach].append(int(dpt.replace(",","")))

	return data