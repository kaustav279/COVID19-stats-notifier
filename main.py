from datetime import datetime,time
from scraping import get_webpage,extract_info
from visualizations import makeARDPieChart,makeDailyGraph
from mailing import createMail,sendMail

link = "https://www.covid19india.org/"
indiapc = "ind.jpg"
statepc = "sta.jpg"
statsfile = "daily_total.txt"
dailygraph = "growth.jpg" #add any jpg file named growth.jpg to folder when running for first time
state = " " #add name of your state
receiver_list = [" "] #add email addresses of receivers

html_page = get_webpage(link)
data = extract_info(html_page,state)

makeARDPieChart(data["India"][1:],indiapc)
makeARDPieChart(data[state][1:],statepc)

if datetime.now().time().replace(minute=0,second=0,microsecond=0) == time(12):	# graph is plotted daily using data at 1200 hours
	makeDailyGraph(data["India"][0],statsfile,dailygraph)

msg = createMail(data["India"][0],data[state][0],indiapc,statepc,dailygraph,state)
sendMail(msg,receiver_list)