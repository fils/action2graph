import sys, getopt
import rdflib
from pyshacl import Validator
from pathlib import Path

def main(argv):
  datagraph = ''
  report = ''
  try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
  except getopt.GetoptError:
      print ('test.py -i <datagraph> -o <report>')
      sys.exit(2)
  for opt, arg in opts:
      if opt == '-h':
         print ('test.py -i <datagraph> -o <report>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         datagraph = arg
      elif opt in ("-o", "--ofile"):
         report = arg
  print ('Input file is:', datagraph)
  print ('Output file is: ', report)

  with open(datagraph, 'rb') as f:
          df = f.read()

  # dataUrl = urllib.request.urlopen("https://pacific-data.sprep.org/sites/default/files/pod_data/data.json")
  # df = dataUrl.read()
  dg = rdflib.Graph()
  dg.parse(data=df, format="json-ld")

  sf = Path('./shapes/sosoShape.ttl').read_text()  # in actions script are run from repo root
  # shapeUrl = urllib.request.urlopen("https://raw.githubusercontent.com/iodepo/odis-arch/schema-dev/book/tooling/notebooks/Mapping/DCATmapping/shapes/dcatsdoOLD.ttl")
  # sf = shapeUrl.read()
  sg = rdflib.Graph()
  sg.parse(data=sf, format="ttl")

  v = Validator(data_graph=dg, shacl_graph=sg,  options={"inference": "none", "advanced": True})  # turn off rdfs inferencing
  conforms, report_graph, report_text = v.run()
  expanded_graph = v.target_graph
  # print(report_text)

  # og = bytes(expanded_graph.serialize(format="ttl"), 'utf-8') #.decode("utf-8")
  og = bytes(report_graph.serialize(format="ttl"), 'utf-8') #.decode("utf-8")

  with open(report, 'wb') as f:
          f.write(og)

if __name__ == "__main__":
   main(sys.argv[1:])


