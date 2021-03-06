import matplotlib.pyplot as plt
import utils

def pie_chart(labels, values, title):
  fig1, ax1 = plt.subplots()
  newLabels = []
  for i in range(len(values)):
    newLabels.append(str(labels[i]) + " - " + str(values[i]))
  ax1.pie(values, labels=newLabels)
  ax1.axis('equal')
  plt.title(title)
  plt.show()

def genderedSadnessPieChart():
  data = utils.getdata("school_safety.csv")
  rows = list(filter(lambda n: n[12] == "Yes", data))
  numberOfMales = list(map(lambda n: n[1], rows)).count("Male")
  pie_chart(['Male', 'Female'], [numberOfMales, len(rows) - numberOfMales], "# of Sad People Based On Gender")