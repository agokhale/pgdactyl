import psycopg2
import os
from psycopg2 import  sql
import random
import faker
import string
import sys
import psycopg2.extensions as ext

finst={}; 
#https://faker.readthedocs.io/en/master/providers/baseprovider.html
def setupfake():
	global finst; 
	finst = faker.Faker(); 
	faker.Faker.seed(0); 

def gender_redact(): 
	global finst;
	return (finst.bothify(text="?", letters="MF"));  ##XX is this right?
def mi_redact(): 
	global finst;
	return (finst.bothify(text="?")); 
def ssn4_redact():
	global finst;
	return (finst.bothify(text="####")); 
def country_redact():
	return ("USA"); 
def address1_redact():
	global finst;
	adr = finst.address();
	##returs Out[49]: '47015 Sullivan Gardens Apt. 949\nEast Kristyberg, OR 71739'
	## so cut it into lines to match database
	line1 =  adr.split("\n")[0];
	return (line1 ); 

def zip4_redact():
	#tricksy , sometimes null
	global finst;
	maybe4 = finst.bothify(text="####"); 
	return( random.choice ([ maybe4, None])); 
def email2_redact():
	#tricksy , sometimes null
	global finst;
	maybeemail =  finst.email();
	return( random.choice ([ maybeemail, None])); 

def fname_redact():
	global finst;
	return (finst.name().split(" ")[0] ); 
def lname_redact():
	global finst;
	return (finst.name().split(" ")[1] ); 
	
def ssno_redact():
	global finst; 
	sn  = finst.bothify(text="#########"); 
	return  (  sn); 

def payee_redact():
	return( random.choice ([ "Provider", "payee"])); 
def phone_redact():
	#XX we have inconsistant phone storage varchar lengths, so slice to :16
	global finst;
	return( finst.phone_number()[:16] ); 
def secQ_redact():
	global finst;
	jsontxt = """[ {"answer": "One two three", "question": "Respond One two thre"}, {"answer": "One two three", "question": "Respond One two three"}, {"answer": "One two three", "question": "Respond One two three"} ]"""
	return ( jsontxt)
	

setupfake();  # run before starting  relation defn'
