import sys
sys.path.append('../')
from ModelCreate import user,db
from argparse  import ArgumentParser



args = ArgumentParser()

args.add_argument('u',help = 'UserName')
args.add_argument('p',help = 'password')

a=args.parse_args()

ADuser = user(users = a.u , password = a.p)

db.session.add(ADuser)

db.session.commit()



