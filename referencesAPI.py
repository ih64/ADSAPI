import os, sys, json, requests
import pandas as pd 

# base API search url
BASE_URL = 'http://adslabs.org/adsabs/api/search/'

# developer API access key
DEV_KEY = 'eZgX5PXnBjqcwbtc'

#reflists is a pything list holding the bibcodes of the publications we want to list out
#returns a pandas dataframe that has information on publications we are insterested in
def getBibInfo(reflist):

	df=pd.DataFrame(columns=['bibcode','title','pub','volume','page','author', 'year'])

	for i in reflist:
		params={}
		#querry we are sending
		params['q'] = "bibcode:%s" % i

		#stuff we want back
		params['fl'] = 'title,pub,volume,page,pubdate,author'

		#we just want the first response
		params['rows']=1

		#the developer acess key
		params['dev_key']=DEV_KEY

		#store the response to the requet to ads
		r=requests.get(BASE_URL, params=params)

		#response is in json as default, parse it
		data=json.loads(r.text)['results']['docs'][0]

		#we will store the data in the respons we are insterested in in 
		#the dictionary 'citation'
		citation={}

		citation['title']=data['title'][0].encode('utf-8')
		
		if len(data['author']) > 1:
			citation['author']=data['author'][0].encode('utf-8')+' et al.'
		else:
			citation['author']=writers.encode('utf-8')

		citation['bibcode']=i
		citation['pub']=data['pub'].encode('utf-8')
		citation['volume']=data['volume'].encode('utf-8')
		citation['page']=data['page'][0].encode('utf-8')
		citation['pubdate']=data['pubdate'].encode('utf-8')
		citation['year']=data['pubdate'].split('-')[0]
		#print(citation['author']+' '+citation['year']+', '+citation['pub']+', '+citation['volume']+', '+citation['page']+
		#	'. '+citation['title']+'\n')
		
		#add the citation information as a row in the pd dataframe
		df=df.append({
			'bibcode':citation['bibcode'],
			'pub':citation['pub'],
			'title':citation['title'],
			'volume':citation['volume'],
			'page':citation['page'],
			'year':citation['year'],
			'author':citation['author']
			}, ignore_index=True)

	return df

#recieves the data frame from above, changes it up so it is sorted by year of publication, 
#then subsorted in alphabetical order by last name
def sortYearName(df):
	pass

#recieves the sorted dataframe, then prints out all the stuff in html format
#so the user can paste the output in 'refereed.html'
def makeHTML(df):
	pass