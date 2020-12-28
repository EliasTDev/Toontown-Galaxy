import argparse
import sys

from pypperoni.cmake import CMakeFileGenerator

parser = argparse.ArgumentParser()
parser.add_argument('--nthreads', '-t', type=int, default=4,
                    help='Number of threads to use')
args = parser.parse_args()

c = CMakeFileGenerator('TTGGameEngine', outputdir='build', nthreads=args.nthreads)
c.add_tree('toontown')
c.add_tree('otp')
c.add_tree('direct')
c.add_tree('pandac')
c.add_tree('pytz')
c.add_tree('dependencies/panda/python/Lib/site-packages/MySQLdb')
c.add_file('main.py')
c.modules['main'].set_as_main()
c.run()