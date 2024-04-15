# option 6
def main():
      print ("option 2")
      # Get a subset coverage by slicing on time axis, trimming on spatial axes, and encoding result in image/jpeg.

      from IPython.display import Image
      import requests

      # Set base url which can be used in further code examples
      service_endpoint = "https://ows.rasdaman.org/rasdaman/ows"
      base_wcs_url = service_endpoint + "?service=WCS&version=2.0.1"

      request = "&REQUEST=GetCoverage"
      cov_id = "&COVERAGEID=S2_L2A_32631_TCI_60m"
      subset_time = "&SUBSET=ansi(\"2021-04-09\")"
      subset_e = "&SUBSET=E(669960,729960)"
      subset_n = "&SUBSET=N(4990200,5015220)"
      encode_format = "&FORMAT=image/jpeg"

      response = requests.get(base_wcs_url + request + cov_id + subset_time + subset_e + subset_n + encode_format, verify=False)

      # Display result directly
      Image(data=response.content)
   
if __name__ == "__main__":
    main()