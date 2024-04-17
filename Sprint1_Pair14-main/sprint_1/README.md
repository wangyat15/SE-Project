# Project Specification and Documentation

## Introduction
This project utlilizes [Python](https://www.python.org/) to generate and visualize spatio-temporal earth data using transparent [WCPS](https://earthserver.eu/wcs/) query from the [Rasdaman Datacube](https://standards.rasdaman.com/), a multi-dimensional array database. It showcases the processing of datacube objects through a range of WCPS operations and functions.  The project is implmented in a traditional software development life cycle including specification, implementation, testing, integration and documentation. The project emphasizes collaboration and teamwork accross sprint cycles to achieve the planned outcomes. 

## Project Scope
+ This project using WCS and WCPS query requests to process the datacube data with a list of operations, including access, subsetting, processing, aggregation, fusion and encoding. The retrieved data is applied for further processing, including graph plotting.
+ Acknowledgments: We extend our grateful to following persons for the guidance throughout the project
  - Prof. Peter Baumann
  - Eremina Elizaveta
  - Sirotkina Veronika
  - Getahun Raey Addisu

## Design 
+ Python Library to provide a selection menu as an interface with the WCPS server that provides a list of WCS/WCPS operations and functions
  - A selection menu with a list of menu choices to showcase and execute the WCS and WCPS operations.[start_menu.py](src/wdc/start_menu.py) 
    - WCPS query request in a python code with access and encoding the output into image jpeg [opt1_wcps_access.py](src/wdc/opt1_wcps_access.py)
    - WCS request in a python code with subsetting by slicing on time axis and trimming on spatial axes, and encoding the output into image jpeg [opt2_wcps_subsetting.py](src/wdc/opt2_wcps_subsetting.py)
    - WCPS query request in a python code with fusion of different coverages [opt3_wcps_fusion.py](src/wdc/opt3_wcps_fusion.py)
    - WCPS query request in a python code with aggregation operation to retrieve the minimum temperature of Bremen City in 2014 [opt4_wcps_minimum.py](src/wdc/opt4_wcps_minimum.py)
    - WCPS query request in a python code with aggregation operation to retrieve the maximum temperature of Bremen City in 2014 [opt5_wcps_maximum.py](src/wdc/opt5_wcps_maximum.py)
    - WCPS query request in a python code with aggregation operation to retrieve the average temperature of Bremen City in 2014 [opt6_wcps_average.py](src/wdc/opt6_wcps_average.py)
    - WCPS query to retrieve the monthly average temperature of Bremen City in 2014 and plot it into a graph (not started yet) [opt7_wcps_mthly_average.py]
    - Quit [opt8_quit]
  
 + [System Design Diagram (Diagram/SystemDesignFlowchart.pdf) ](Diagram/SystemDesignFlowchart.pdf)
   
 + Implementation Schedule and Plan
   - Sprint#1(8 April to 18 April , 2 weeks):
     - Define project scope, project plan, project design, implementation schedule and setup the environment with some operations and functions, source codes and test cases
   - Sprint#2(19 April to 2 May, 2 weeks):
     - Implement the rest of the operations and features and perform unit testing
   - SPrint#3(3 May to 16 May, 2 weeks) :
     - Implement code integration, perform integration test, create/build python package for deployment and release, and refine the documentation  

+ Technical details:
  - [Python](https://www.python.org/)
  - [WCPS (Web Coverage Processing Service)](https://earthserver.eu/wcs/) of the [Rasdaman Datacube and query language](https://standards.rasdaman.com/) 
  - [Jupyter notebook](https://jupyter.org/install) (for testing and training materials)
  - [GitHub](https://github.com/) (for specification, documentation and source repository)
    
+ Test Plan :
  - Unit Testing : test the units of each operation and each feature with test cases and expected test results
  - Integration Test : test the whole system with the integration test cases after integrated all units of operations and features

## Implementation
### Source Library
Path: [sprint_1/src](src)

### Getting Started
+ Prerequisites
  - Install [Python](https://www.python.org/)
  - Install required Python Libraries
    ```
    $pip install requests IPython Image owslib numpy matplotlib
    ```   
+ Packaging and installation (not started yet)
+ Start running the project: run [start_menu.py](src/wdc/start_menu.py) 
  ```
  start_menu.py
  ```

### Sample Python Code using WCPS query and Rasdamen Datacube Server
This is a sample Python code using to submit WCPS query to datacube server and to visualize the response data in a JPEG image:
```
# Sample WCPS query request in a pythob code 
# Send a WCPS query for evaluation on the rasdaman server; as WCPS queries usually contain 
# special characters like '[', ']', '{', '}', it is necessary to send POST requests.

from IPython.display import Image
import requests

# Set base url which can be used in further code examples
service_endpoint = "https://ows.rasdaman.org/rasdaman/ows"
base_wcs_url = service_endpoint + "?service=WCS&version=2.0.1"

# WCPS query with encoding result in image/jep
query = '''
for $c in (S2_L2A_32631_B01_60m) 
return
  encode(
    ( 0.20 * ( 35.0 + ( 
                (float) $c[ ansi( "2021-04-09" ) ]  ) 
            ) 
    )[ E( 669960:729960 ), N( 4990200:5015220 )  ]
   , "image/jpeg")
'''

response = requests.post(service_endpoint, data = {'query': query}, verify=False)

# Display result directly
Image(data=response.content)
```

Sample output from Python code above
![image](image/sample.jpg)

### Testing Cases
+ Unit Test:
  - Path: [sprint_1/test_case/unit_test](test_case/unit_test)
+ Integration Test (not started yet):
  - Path: [sprint_1/test_case/Integration_test]


## Implementation Progress
### Sprint#1
+ Start date:
  - 8 April 2024
+ End date:
  - 18 April 2024
+ SprintPair14 and Members:
  - Daria SOLOVEVA and Wang Yat SIN 
+ Work done:
  - Defined and outlined the project scope and scope of operations and functions
  - Created the README.md project specification, documentation and project file structure
  - Completed the project design and prepared the swimlane diagram
  - Defined and outlined the project plan, implementation schedule and respective deliverable
  - Defined the test plan for unit test cases and integration test cases 
  - Completed and tested with unit test cases using jupytor notebook of below python codes
    - Interface main menu to select and execute one of the WCS/WCPS operations and features
    - WCPS query request in a python code with access and encoding the output into image jpeg
    - WCS request in a python code with subsetting by slicing on time axis and trimming on spatial axes, and encoding the output into image jpeg
    - WCPS query request in a python code with fusion of different coverages
    - WCPS query request in a python code with aggregation operation to retrieve the minimum temperature of Bremen City in 2014
    - WCPS query request in a python code with aggregation operation to retrieve the maximum temperature of Bremen City in 2014
    - WCPS query request in a python code with aggregation operation to retrieve the average temperature of Bremen City in 2014
    - Quit
  - Created unit_test cases and results using jupyter notebook  
+ Work partially done:
  - Python codes are tested individually but are not integrated for integration test 
+ Work not started yet:
  - operations and functions not started yet, and further enhancements:
    - WCPS query to retrieve the monthly average temperature of Bremen City in 2014 and plot it into a graph
    - make the query parameters as input variables to provide more dynamic query requests, including
      - the latitude and longitude of a City in retrieving the temperature data
      - from date and to date of a time period in retrieving the temperature data
  - Define the integration test cases and details
  - Conduct the integration test and modify the codes accordingly
  - Integrate the python codes into module and build the python library and package
  - Refine the documentation on packaging, installation and distribution
+ Overall completion %:
  -  completed 40% of the project
+ Handover notes:
  - To start and prepare the environment, follow the Prerequisites to install Python and required Python libraries
  - Can consider to add more operations and functions into the selection menu 
  - The Python codes are completed and tested individually, but are not tested integrationally.  

### Sprint#2
+ Start date: 19 April 2024
+ End date:　2 May 2024
+ Pair# and Members: 
+ Work done:
+ Work partially done:
+ Work not started yet:
+ Overall completion %:
+ Handover notes:
  
### Sprint#3
+ Start date: 3 May 2024
+ End date:　16 May 2024
+ Pair# and Members: 
+ Work done:
+ Work partially done:
+ Work not started yet:
+ Overall completion %:
+ Handover notes:
