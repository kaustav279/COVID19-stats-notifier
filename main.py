from datetime import datetime,time
from scraping import get_webpage,extract_info
from visualizations import makeARDPieChart,makeDailyGraph
from mailing import createMail,sendMail

link = "https://www.covid19india.org/"
indiapc = "ind.jpg"
delhipc = "del.jpg"
statsfile = "daily_total.txt"
dailygraph = "growth.jpg"
receiver_list = [" "] #add email addresses of receivers

html_page = get_webpage(link)
data = extract_info(html_page)

makeARDPieChart(data["India"][1:],indiapc)
makeARDPieChart(data["Delhi"][1:],delhipc)

if datetime.now().time().replace(minute=0,second=0,microsecond=0) == time(12):	# graph is plotted daily using data at 1200 hours
	makeDailyGraph(data["India"][0],statsfile,dailygraph)

msg = createMail(data["India"][0],data["Delhi"][0],indiapc,delhipc,dailygraph)
sendMail(msg,receiver_list)