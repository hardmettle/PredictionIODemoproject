import predictionio

client = predictionio.Client(appkey="NO3tJj3XC9JGnszPe9pUMvpq65IJOkMPpb64GeDIKt5iVA0Jwkv2oVS1KznjTUmI")

# Recommend 5 items to each user
#user_ids = [str(x) for x in range(1, 6)]
#for user_id in user_ids:
user_id =3 
print "Retrieve top 5 recommendations for user", user_id
try:
	client.identify(user_id)
	rec = client.get_itemrec_topn("recommendEngineDemo", 5)
	print rec
except predictionio.ItemRecNotFoundError as e:
	print 'Caught exception:', e.strerror()
