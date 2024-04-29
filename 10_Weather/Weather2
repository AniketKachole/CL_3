from mrjob.job import MRJob
from mrjob.step import MRStep
import csv

class FindHotCoolWeather:

    def mapper_init(self):
        self.min_temp = float('inf')
        self.max_temp = float('-inf')

    
    def mapper(self,_,line):
        try:
            row = next(csv.reader([line]))
            month,day,temp= int(row[2]),int(row[3]),float(row[3])

            if temp < self.min_temp:
                self.min_temp = temp
            if temp>self.max_temp:
                self.max_temp = temp


        except(ValueError,IndexError):
            pass


    def mapper_final(self):
        yield "min temp", self.min_temp
        yield "max temp", self.max_temp


    def reducer(self,key,values):
        yield key, min(values) if key=="min" else max(values)



    def steps(self): 
        return [
        MRStep(
            mapper_init = self.mapper_init,
            mapper=self.mapper,
            mapper_final = self.mapper_final,
            reducer = self.reducer
        )
        ]
    


if _name== "main_":
    FindHotCoolWeather.run()
