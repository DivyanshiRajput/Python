day= raw_input ("day: ")
month= raw_input ("month: ")
month= month.lower()
if month == 'december':
   zodiac = "sagittarius" if (day < 22) else "capricornus" 

elif month == 'january':
   zodiac = "capricornus" if (day < 21) else "aquarius"

elif month == 'february':
   zodiac = "aquarius" if (day < 20) else "pisces"

elif month == 'march':
   zodiac = "pisces" if (day < 21) else "aries"

elif month == 'april':
   zodiac = "aries" if (day < 21) else "taurus"

elif month == 'may':
   zodiac = "taurus" if (day < 22) else "gemini"

elif month == 'june':
   zodiac = "gemini" if (day < 22) else "cancer"

elif month == 'july':
   zodiac = "cancer" if (day < 23) else "leo"

elif month == 'august':
   zodiac = "leo" if (day < 23) else "virgo"

elif month == 'september':
   zodiac = "virgo" if (day < 24) else "libra"

elif month == 'october':
   zodiac = "libra" if (day < 24) else "scorpius"

elif month == 'november':
   zodiac = "scorpius" if (day < 23) else "sagittarius"

print "zodiac: " ,zodiac 



