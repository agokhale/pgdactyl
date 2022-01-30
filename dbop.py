import psycopg2
import os
from psycopg2 import  sql
import psycopg2.extras as p2extras
import random
import string
from pprint import pprint
import sqlquoter
import sys
import psycopg2.extensions as ext

_dbh = {};
_dbcurse = {};
gdatabase="clone"
gschema="portal"

def connectiondump():
	global _dbcurse;
	global _dbh
	pprint ( _dbcurse ) 
	pprint ( _dbcurse.query ) 
	pprint ( _dbcurse.description ) 
	pprint ( _dbcurse.rowcount ) 
	pprint ( _dbh ) 
	pprint ( _dbh.info.error_message ) 
	pprint ( _dbh.info.dsn_parameters )

def insertfactory(table, rowdict):
	sqltext = """insert into {table}  ({columns})  values ({rowvalues}) """
	
	columnnames =sqlquoter.assemblekeys( list( rowdict.keys()));
	rowvalues =sqlquoter.assemblevalues( list( rowdict.values()));
	qry = sql.SQL (sqltext).format(
		table=sql.Identifier(table),
		columns=sql.SQL(columnnames),
		rowvalues=sql.SQL(rowvalues ),
	)

	return qry
	

def exec(qry, *qargs): 
	global _dbcurse;
	try :
		_dbcurse.execute(qry, qargs ); 
	except (Exception, psycopg2.DatabaseError) as error:
		print (__name__,error); 
		connectiondump()
		sys.exit(10) 

def commit():
	global _dbcurse;
	global _dbh
	try :
		_dbh.commit( ); 
	except (Exception, psycopg2.DatabaseError) as error:
		print (__name__,error); 
		connectiondump()
		sys.exit(10) 

def fetch():
	global _dbcurse;
	rows=[];
	try :
		rows = _dbcurse.fetchall ()
		print (_dbcurse.statusmessage)
	except (Exception, psycopg2.DatabaseError) as error:
		print (__name__,error) 
		connectiondump()
		sys.exit(10) 
	return rows;

def fetchexec(qry):
	exec(qry)
	return (fetch())
def getprofile():
	return (fetchexec("select * from profile"))

## rows forms fetch()
## gin up array of   dictionaries from tuples
## thuis is obosoleted with the cursorFactory extra
def dictify_row(row ):
	global _dbcurse
	desc = _dbcurse.description	
	try:
		output = {}
		for rcursor in range ( 0, len(desc)):
			output[desc[rcursor].name] =  row[rcursor]
	except ( err ):
		print ( __name__, error) 
		pprint ( row, desc)
		connectiondump()
		sys.exit(10) 
	return output
	
def dbfetchone():
	return dbfetch()[0]; 

def start (pqdsn):
	try:
		global _dbh;
		global _dbcurse;
		_dbh  = psycopg2.connect(pqdsn);
		_dbcurse  = _dbh.cursor(cursor_factory=p2extras.RealDictCursor); 
	except (err):
		print ("unable to connect to the database",err)
		sys.exit(-4); 
	try:
		_dbcurse.execute ("SET search_path TO "+ gschema + " ;" ) ;
		#dbfetch(); 
	except (Exception, psycopg2.DatabaseError) as error:
		print ("I am unable to connect so cscema",error)
		sys.exit(-4); 

