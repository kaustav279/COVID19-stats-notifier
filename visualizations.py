import matplotlib.pyplot as plt
plt.switch_backend('agg')

def makeARDPieChart(sizes,name):

	def abs_val(val):
		val2 = val*sum(sizes)*0.01
		return f"{val2:.0f}"

	plt.figure()
	labels = ['Act.', 'Rec.', 'Dec.'] #Active, Recovered, Deceased
	plt.pie(sizes, labels=labels, autopct=abs_val, startangle=90)
	plt.axis("equal")
	
	plt.savefig(name)

def makeDailyGraph(datapt,filename,graphname):
	with open(filename,"a+") as f:
		f.write(str(datapt)+"\n")
		f.seek(0)
		data = f.readlines()

	X = range(1,len(data)+1)
	Y = [int(y) for y in data]

	plt.figure()
	plt.plot(X,Y,"--bo")
	plt.xticks(X)
	plt.xlabel("Day No.")
	plt.ylabel("Total Cases")
	plt.title("Growth of cases")

	plt.savefig(graphname)
