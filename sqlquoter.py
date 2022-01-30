import string
import decimal
import json
import datetime
import re

def freeze(x ):
#produce an sql safe representation of param x
#returns string
	typ = type (x) 
	output=" sqlquoter-error %s "%typ
	if (typ == list):
		output = """ '""" + json.dumps (x) + """' """
	if (typ == bool):
		output = """ """ + str(x) + """ """
	if ((typ == datetime.datetime) | (typ == datetime.date)):
		output = """ '""" + str(x) + """' """
	if (typ == str):
		output = """ '""" + x + """' """
	if ((typ == int) | (typ == decimal.Decimal)):
		output =" " + str(x) + " "
	if (str(type(x))  == "<class 'NoneType'>"): #I can't even... 
		output = " null " 
	return output

def assemblekeys ( x ):
#param x is a list of objects, freeze them and emit a string, no fancy quoting
	output = ",".join (x)
	return output
def assemblevalues ( x ):
#param x is a list of objects, freeze them and emit a string h
	output = ",".join (map(freeze,x))
	return output

assert """ 'felh' """ == freeze("felh")
assert """ 123 """ == freeze(123)
assert " 1234 , 'felh' , null " == assemblevalues( [ 1234, "felh" , None]) 
