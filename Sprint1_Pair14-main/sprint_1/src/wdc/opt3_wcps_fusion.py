# option 3
def main():
      print ("option 3")
      # WCPS query request in a python code with fusion of different coverages

      from IPython.display import Image
      import requests

      # Set base url which can be used in further code examples
      service_endpoint = "https://ows.rasdaman.org/rasdaman/ows"
      base_wcs_url = service_endpoint + "?service=WCS&version=2.0.1"

      # WCPS query with fusion operation from different coverages and encoding result in image/jep

      query = '''
      for $c in (S2_L2A_32631_B12_20m), 
          $d in (S2_L2A_32631_B08_10m),
          $e in (S2_L2A_32631_B03_10m)

   
      return
       encode(
          {
            red: scale( $c[ ansi( "2021-04-09" ), E( 670000:679000 ), N( 4990220:4993220 ) ],
                       { E:"CRS:1"(0:599), N:"CRS:1"(0:299) }) ;
          green: scale( $d[ ansi( "2021-04-09" ), E( 670000:679000 ), N( 4990220:4993220 ) ],
                       { E:"CRS:1"(0:599), N:"CRS:1"(0:299) }) ;
          blue: scale( $e[ ansi( "2021-04-09" ), E( 670000:679000 ), N( 4990220:4993220 ) ], 
                        { E:"CRS:1"(0:599), N:"CRS:1"(0:299) })
          } / 15.0
        , "image/jpeg")
      '''

      response = requests.post(service_endpoint, data = {'query': query}, verify=False)

      # Display result directly
      Image(data=response.content)
   
if __name__ == "__main__":
    main()