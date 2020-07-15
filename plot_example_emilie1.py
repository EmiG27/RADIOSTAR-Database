from utils.data_reader import DataModel 
import utils.data_plotter as dp
import utils.data_processor as dpr
import sys, os

#NOTE:
# grab  files' paths from command line ? this would be a really nice addition and 
# the plot.py file could be left unchanged when running on different data located
# elsewhere. Usage could be something like this: 
# plot.py -i input_file.txt -d data_file.txt -r rerence_file.txt
# -r could be optional
# (by Evelin)

print("This is this print statement", sys.argv)

#run plot.py fruityYields
whatever_input = sys.argv[1] # = fruityYields
sys.argv[1] = fruityYields

#Uploaded

# THERE IS SOME STUFF HERE THAT TRANSFORMS INPUT INTO THE APPROPRIATE VARIABLES
#yield_folder = "fruityYields"
#input_file = "fruityYields_input.txt"

# Getting the data model ready. It includes the species, input_dictionar and 
# a DataFrame with the imported yield data.
data_model = DataModel(input_file, yield_folder)

# Process the data for the plots
data_to_plot = dpr.process(data_model)

# Create figure(s)
dp.plot(data_to_plot)