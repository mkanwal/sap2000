'''''''''''''''''''''''''''''''''
Files for dealing with input/output in the simulation
'''''''''''''''''''''''''''''''''
# local python files
import os


# importing SAP API
from SAP2000 import sap2000
from SAP2000.constants import UNITS

# importing helper function for filesystem input/output
from Helpers.helpers import path_exists

# program constants
from variables import PROGRAM

def io(inputfile = "", outputfile = "C:\SAP 2000\output.sdb"):
  """
  Opens the specified inputfile and outputfile. By default, it creates a new 
  model if no inputfile is specified and saves it as the specified outputfile. 
  If no outputfile is specified, the default location is 
  "C:\SAP 2000\output.sdb". Returns the program and model.
  """
  # start program
  program = sap2000.Sap2000()

  # This opens the model if it is passed in
  program.start(filename=inputfile)

  # If there was no model specified, open an empty one
  if inputfile == "":
    model = program.initializeModel()
    return_value = model.File.NewBlank()
    assert return_value == 0

  # Just point model to the right object
  else:
    model = program.sap_com_object.SapModel

  # save with new output file name (create directory if necessary)
  path = os.path.dirname(outputfile)
  path_exists(path)
  program.save(outputfile)

  # reset the correct units
  model.SetPresentUnits(UNITS[PROGRAM['units']])

  return program, model