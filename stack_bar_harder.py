from tkinter import Y
import matplotlib.pyplot as plt
import utils

def stacked_bar_chart(xaxis, yaxis1, yaxis2, label1, label2, ylabel):
  plt.bar(xaxis, yaxis1, color='r')
  plt.bar(xaxis, yaxis2, bottom=yaxis1, color='b')
  plt.ylabel(ylabel)
  plt.legend([label1, label2])
  plt.show()

def ageAndGenderBasedBullied():
  data = utils.getdata("school_safety.csv")
  rows = list(filter(lambda n: n[3] == "Yes", data))
  ageSet = utils.getuniques(utils.extractcolumn(rows, 0))
  male, female = [], []
  for age in ageSet:
    male.append(utils.getcountofunique(list(map(lambda o: o[1], filter(lambda n: n[0] == age, rows))), "Male"))
    female.append(utils.getcountofunique(list(map(lambda o: o[1], filter(lambda n: n[0] == age, rows))), "Female"))
  stacked_bar_chart(ageSet, male, female, "Male", "Female", "Number of People Bullied")