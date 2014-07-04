#!/usr/bin/python

from SixDB import *
from SixDir import *
from DA_FullStat_v2 import *
from DA_FullStat_public import *
from mad6t import *
import os

if __name__ == "__main__":
	try:
		opts, args = getopt.getopt(sys.argv[1:], "h", ["help","loaddir","loaddb","DA","mad","join10"])
	except getopt.error, msg:
		print msg
		print "for help use --help"
		sys.exit(2)
	for o, a in opts:
		if o in ("-h", "--help"):
			print "use: main <option>" 
			print "loaddir <optional: studydir> LOAD A COMPLETE OR UPDATED STUDY INTO DATABASE"
			print "loaddb <studyname> CREATE STUDY FROM DATABASE"
			print "DA <studyname> CREATE DARE FILES FOR STUDIES"
			print "mad <studyname> MAD RUN ANALYSIS AND CHECK"
			print "join10 <studyname> PERFORM RUN_JOIN10 FOR STUDY PROVIDED"
		if o in ("--loaddir","-loaddir"):
			if len(args)<1:
				a = SixDB()
			if len(args)==1:
				a = SixDB(args[0])
				a.st_control()
				a.st_mask()
				a.st_env()
				a.st_mad6t_run()
				a.st_mad6t_run2()
				a.st_mad6t_results()
				a.st_six_beta()
				a.st_six_input()
				a.st_six_results()
			else:
				print "too many arguments see help with -h or --help"
				sys.exit(0)
		if o in ("--loaddb","-loaddb"):
			if len(args)==1:
				a = SixDir(args[0])
				a.load_extra()
				a.load_mad6t_run()
				a.load_mad6t_run2()
				a.load_mad6t_results()
				a.load_six_beta()
				a.load_six_input_results()
			else:
				print "invalid see help with -h or --help"
				sys.exit(0)
		if o in ("--DA","-DA"):
			if len(args)==1:
				main2(args[0])
				main1(args[0])
			else:
				print "invalid see help with -h or --help"
				sys.exit(0)
		if o in ("--mad","-mad"):
			if len(args)==1:
				a = SixDir(args[0])
				m = Mad6tOut(**a.env_var)
				m.check_all()
			else:
				print "invalid see help with -h or --help"
				sys.exit(0)
		if o in ("--join10","-join10"):
			if len(args)==1:
				a = SixDir(args[0])
				if a.get_missing_fort10 == 0 and a.get_incomplete_fort10 == 0:
					a.join10
			else:
				print "invalid see help with -h or --help"
				sys.exit(0)
	if len(args)<1 :
	    print "too few options: please see help with -h or --help"
	    sys.exit()
	print opts
	print args
# a = SixDB('./files/w7/sixjobs/') #SixDB.py
# a.st_control()
# a.st_mask()
# a.st_env()
# a.st_mad6t_run()
# a.st_mad6t_run2()
# a.st_mad6t_results()
# a.st_six_beta()
# a.st_six_input_results()
# a = SixDir('jobslhc31b_inj55_itv19') #SixDir.py
# a.load_extra()
# a.load_mad6t_run()
# a.load_mad6t_run2()
# a.load_mad6t_results()
# a.load_six_beta()
# a.load_six_input_results()
# a.join10()
# main1(a.env_var['LHCDescrip']) #DA_FullStat_public.py
# main1(a.env_var['LHCDescrip']) #DA_FullStat_v2.py
# m = Mad6tOut(**a.env_var)
# print m.get_outdirnames()
# print m.get_outfnames()
# m.check_all()