import matplotlib.pyplot as plt
import utils

def simple_bar_chart(xaxis, yaxis, label):
  fig, axes = plt.subplots()
  axes.bar(xaxis, yaxis, label=label, color="#06145F")
  axes.ticklabel_format(style='plain', useOffset=False, axis='y')
  axes.legend()
  plt.show()


def ageBasedSadness():
  data = utils.getdata("school_safety.csv")
  ageColumn = list(filter(lambda n: n!='', utils.extractcolumn(data, 0)))
  ageSet = utils.getuniques(ageColumn)
  ageCounts = []
  for age in ageSet:
    ageCounts.append(utils.getcountofunique(ageColumn, age))
  simple_bar_chart(ageSet, ageCounts, "Sadness Based on Age")