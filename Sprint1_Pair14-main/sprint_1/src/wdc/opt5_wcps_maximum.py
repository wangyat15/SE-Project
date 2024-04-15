# option 5
def main():
      print ("option 5")
      # WCPS query with aggregation operation to retrieve the maximum temperature of Bremen City in 2014
      import requests

      # Set base url which can be used in further code examples
      service_endpoint = "https://ows.rasdaman.org/rasdaman/ows"
      base_wcs_url = service_endpoint + "?service=WCS&version=2.0.1"

      # WCPS query with aggregation operation - maximum

      query = '''
      for $c in (AvgLandTemp) 
      return
        max ( $c[Lat(53.08), Long(8.80),ansi("2014-01-01T00:00":"2014-12-31T18:00")] )
      '''

      response = requests.post(service_endpoint, data = {'query': query}, verify=False)
      my_concat_str = "maximum temperature of Bremen City in 2014 : " + str(response.content.decode() + "C")
      print(my_concat_str)  
      print("==============================")
      print(" ")
   
if __name__ == "__main__":
    main()