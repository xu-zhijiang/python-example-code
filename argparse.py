import argparse

def get_args():
  """Parse command line."""
  filename_list = lambda x: x.split(";")
  parser = argparse.ArgumentParser()
  parser.add_argument("--input", type=filename_list,
                      help="paths to input libraries separated by semicolons",
                      required=True)
  parser.add_argument("--output", help="output deffile", required=True)
  parser.add_argument("--target", help="name of the target", required=True)
  args = parser.parse_args()
  return args


args = get_args()

args.input
args.output
