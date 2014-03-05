import datetime, sys
def lottoChecker(querydate=datetime.datetime.now()):
	if(type(querydate) == datetime.datetime):
		word = 'Today'
		testTime = True
	else:
		querydate = datetime.datetime.strptime(querydate, '%Y-%m-%d')
		word = 'That day'
		testTime = False
	Wed_draw = 2
	Sat_draw = 5
	drawtime = datetime.time(20, 0, 0)
	word = ""
	word2 = ""
	firstSearch = True
	def testLotto(testDate, word, word2):
		if testDate.weekday() == 2 or testDate.weekday() == 5 or testDate.weekday() == 6:
			days = {2:'Wednesday', 5:'Saturday'}
			timenow = datetime.datetime.time(datetime.datetime.now())
			print '%s (%s) is the%s Irish Lotto! \n' % (days[testDate.weekday()], word, word2)
			if(testTime == True):
				if(timenow<drawtime):
					print 'Still time to buy a ticket!'
		else:
			firstSearch = False
			testDate = testDate + datetime.timedelta(days=1)
			word = str(testDate.date())
			word2 = ' next'
			testLotto(testDate, word, word2)
	testLotto(querydate, word, word2)
if(len(sys.argv) > 1):
	lottoChecker(sys.argv[1])
else:
	lottoChecker()