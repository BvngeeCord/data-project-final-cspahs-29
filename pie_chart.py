import matplotlib.pyplot as plt
import utils

def pie_chart(labels, values, title):
  fig1, ax1 = plt.subplots()
  ax1.pie(values, labels=labels)
  ax1.axis('equal')
  plt.title(title)
  plt.show()

def genderedSadnessPieChart():
  data = utils.getdata("school_safety.csv")
  rows = list(filter(lambda n: n[12] == "Yes", data))
  numberOfMales = list(map(lambda n: n[1], rows)).count("Male")
  pie_chart(['Male', 'Female'], [numberOfMales, len(rows) - numberOfMales], "Sad People that are Male or Female")