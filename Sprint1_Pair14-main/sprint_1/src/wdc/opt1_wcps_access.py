# option 1
def main():
      print ("option 1")
      # Sample WCPS query request in a python code with access and encoding operations
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
             ,"image.jpeg")
      '''

      response = requests.post(service_endpoint, data = {'query': query}, verify=False)

      # Display result directly
      # print response.content
      Image(data=response.content)
      print("==============================")
      print(" ")
   
if __name__ == "__main__":
    main()