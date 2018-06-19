# -*- coding: utf-8 -*-
import pandas as pd

class data:
    def __init__(self, Da, Re, data_name, period=False, nperiods=10):
        '''Initializes the data.
        Da: Darcy number.
        Re: Reynolds number.
        data_name: 'cdcl', 'Point1'-'Point4', 'resd', 'mid', 'unmon', 'flow',
                   'str'
        period: If setted, only the data at final n periods is loaded.
        nperiods
        '''
        self.Da = Da
        self.Re = Re
        self.data_name = data_name
        self.period = period
        self.nperiods = nperiods
#        self.fname = '../data/new/{0}_{1}/unpcy_{1}_{2}.dat'.format(Da, Re, data_name)
        self.fname = '../data/old/{0}_{1}/unpcy_{1}_{2}.dat'.format(Da, Re, data_name) #old
        
    def load_data(self):
        '''Load the calculated data as a DataFrame object.'''
        # Set names (variables)
        if self.data_name == 'Point3':
            variables = ["Time", "U", "V", "P"]
        elif self.data_name == 'cdcl':
            variables = ["Time", "Fx", "Fy", "Fpx", "Fpy", "Fxc", "Fyc"]
        elif self.data_name == 'resd':
            variables = ["Iter", "Resor0", "Resor1", "Resor2"]
        else: return None
        
        # Set skiprows
        with open(self.fname) as f:
            size = sum(1 for l in f)
        if self.period == False:
            if self.data_name == 'Point3': skiprows = 1     # ?
            if self.data_name == 'cdcl': skiprows = 1
            if self.data_name == 'resd': 
                # Only read iter which is 30 times
                skiprows = [i for i in range(size) if (i+1)%30!=0]
        else:
            dt = 1e-3        # Time step
            npoints = self.nperiods*int(self.period/dt)
            if self.data_name == 'Point3': skiprows = size - npoints - 1 # ?
            if self.data_name == 'cdcl': skiprows = size - npoints
            if self.data_name == 'resd': 
                skiprows = [i for i in range(size) if (i+1)%30!=0 or (i+1)/30<=(size/30-npoints)]
        
        # Load data
        self.data = pd.read_csv(self.fname, sep='\s+',
                                names=variables,
                                skiprows=skiprows)
        return self.data
    
    
if __name__ == "__main__":
    cdcl = data(1e-06, 200, 'cdcl', period=5.41, nperiods=1).load_data()
    meanCd = -2*cdcl['Fx'].mean()
    print(meanCd)
    
    