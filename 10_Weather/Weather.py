# Design and develop a distributed application to find the coolest/hottest year from the
# available weather data. Use weather data from the Internet and process it using MapReduce

# pip install mrjob

from mrjob.job import MRJob
from mrjob.step import MRStep

def steps():
    return [
        MRStep(mapper=mapper_get_temps, reducer=reducer_get_max_temp),
        MRStep(reducer=reducer_find_max_temp_year)
    ]

def mapper_get_temps(_, line):
    parts = line.split(',')
    try:
        year = parts[3] # Fetching the year 
        temp = float(parts[4])
        yield year, temp
    except ValueError:
        pass  # Ignore lines with invalid data

def reducer_get_max_temp(year, temps):
    yield None, (max(temps), year)
    # yield None, (min(temps), year)

def reducer_find_max_temp_year(_, year_temp_pairs):
    yield max(year_temp_pairs)
    # yield min(year_temp_pairs)

class MRWeatherAnalysis(MRJob):
    def steps(self):
        return steps()

if __name__ == '__main__':
    MRWeatherAnalysis.run()



# python Weather.py weather.csv