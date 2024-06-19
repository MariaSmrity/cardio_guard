from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import pandas as pd

class PopulationPresenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["population"]
        self.figure = None
        self._bind()

    def _bind(self):
        self.frame.back_button.config(command=self.back)
        self.frame.bmi_option.config(command=self._create_bmi_figure)
        self.frame.bp_option.config(command=self._create_bp_figure)
        self.frame.risk_option.config(command=self._create_risk_figure)

    def _create_risk_figure(self):
        top = Toplevel(self.frame)
        data, n_of_samples = self.calculate_data(variable="risk")
        fig = Figure(figsize=(12, 6))
        t = pd.date_range(min(data.keys()), max(data.keys()), freq='ME')
        t = t.strftime('%Y-%m')
        values = []
        n = []
        for date in t:
            if date in data.keys():
                values.append(data[date])
                n.append(n_of_samples[date])
            else:
                values.append(None)
                n.append(0)
        ticks = np.arange(0, len(t), 6)
        ax = fig.add_subplot()
        ax.set_xlabel("time")
        ax.set_title('Risk levels over time')
        ax.set_xticks(ticks)
        ax.set_xticklabels(list(t[ticks]), rotation=45)
        ax.set_ylabel("risk")
        ax.plot(t, values)
        ax2 = ax.twinx()
        ax2.plot(t, n, c = 'lightgray')
        ax2.set_ylabel('n of patients')
        fig.legend(['risk', 'n of patients'])
        self.canvas = FigureCanvasTkAgg(fig, top)
        self.canvas.draw()
        
        self.canvas.get_tk_widget().grid()

    def _create_bp_figure(self):
        top = Toplevel(self.frame)
        data_sys, n_of_samples = self.calculate_data(variable="bp_sys")
        data_dia, n = self.calculate_data(variable="bp_dia")
        fig = Figure(figsize=(12, 6))
        t = pd.date_range(min(data_sys.keys()), max(data_sys.keys()), freq='ME')
        t = t.strftime('%Y-%m')
        values_sys = []
        values_dia = []
        n = []
        for date in t:
            if date in data_sys.keys():
                values_sys.append(data_sys[date])
                values_dia.append(data_dia[date])
                n.append(n_of_samples[date])
            else:
                values_sys.append(None)
                values_dia.append(None)
                n.append(0)
        ax = fig.add_subplot()
        line, = ax.plot(t, values_sys)
        line2, = ax.plot(t, values_dia)
        ax.set_title('Blood pressure levels over time')
        ax.set_xlabel("time")
        ticks = np.arange(0, len(t), 4)
        ax.set_xticks(ticks)
        ax.set_xticklabels(list(t[ticks]), rotation=45)
        ax.set_ylabel("blood pressure (mmHg)")
        ax2 = ax.twinx()
        ax2.set_ylabel('n of patients')
        ax2.plot(t, n, c='lightgray')
        fig.legend(['systolic', 'diastolic', 'n of patients'])
        self.canvas = FigureCanvasTkAgg(fig, master=top)
        self.canvas.draw()

        self.canvas.get_tk_widget().grid()

    def _create_bmi_figure(self):
        top = Toplevel(self.frame)
        data, n_of_samples = self.calculate_data(variable="bmi")
        fig = Figure(figsize=(12, 6))
        t = pd.date_range(min(data.keys()), max(data.keys()), freq='ME')
        t = t.strftime('%Y-%m')
        values = []
        n = []
        for date in t:
            if date in data.keys():
                values.append(data[date])
                n.append(n_of_samples[date])
            else:
                values.append(None)
                n.append(0)
        ax = fig.add_subplot()
        line, = ax.plot(t, values)
        ax.set_title('Body Mass Index levels over time')
        ax.set_xlabel("time")
        ticks = np.arange(0, len(t), 4)
        ax.set_xticks(ticks)
        ax.set_xticklabels(list(t[ticks]), rotation=45)
        ax.set_ylabel("bmi")
        ax2 = ax.twinx()
        ax2.set_ylabel('n of patients')
        ax2.plot(t, n, c='lightgray')
        fig.legend(['bmi', 'n of patients'])
        self.canvas = FigureCanvasTkAgg(fig, top)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid() 

    # Check that a variable exists and add its value to sum if so.
    # Parameters: data, variable name, cumulative sum, count of successful additions
    def add_result(self, data, variable):
        if data.get(variable) != None:
             return data[variable]
        return False
    
    # Parse dates to only include year and month
    def parse_date(self, date):
        parts = date.split("-")
        new_date = parts[0]+ "-"+parts[1]
        return new_date

    # Calculate population average of one variable
    def calculate_one(self, variable, data):
        vals = {}
        result = {}
        n_of_samples = {}

        for patient in data:
            labs = data[patient].get_lab_values()
            for date in labs:
                res = self.add_result(labs[date], variable)
                if res:
                    d = self.parse_date(date)
                    if d in vals.keys():
                        vals[d].append(res)
                    else:
                        vals[d] = [res]
        
        for date in vals:
            result[date] = sum(vals[date]) / len(vals[date])
            n_of_samples[date] = len(vals[date])
            
        return result, n_of_samples
  
    # Calculate population average of all variables
    def calculate_all(self, data):

        result = {}
        bmi = self.calculate_one("bmi", data)
        for date in bmi:
            result[date] = [bmi[date]]

        bsys = self.calculate_one("bp_sys", data)
        for date in bsys:
            if date not in result:
                result[date] = ["", bsys[date]]
            else:
                result[date].append(bsys[date])

        bdia = self.calculate_one("bp_dia", data)
        for date in bdia:
            if date not in result:
                result[date] = ["", "", bdia[date]]
            else:
                result[date].append(bdia[date])

        risk = self.calculate_one("risk", data)
        for date in risk:
            if date not in result:
                result[date] = ["", "", "", risk[date]]
            else:
                result[date].append(risk[date])

        return result

    # Calculates average bmi and blood pressure for all patients
    # Returns: a tuple of the averages
    def calculate_data(self, variable="all"):
        data = self.model.patient_dict
        if variable != "all":
            return self.calculate_one(variable, data)
        else:
            return self.calculate_all(data)
       
       
    def back(self):
        self.view.switch("home")