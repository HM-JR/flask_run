from ModelCreate import user
from argparse  import ArgumentParser


args = ArgumentParser()

args.add_argument('u',help = 'UserName')
args.add_argument('p',help = 'password')

a=args.parse_args()

print(a.u)
print(a.p)



