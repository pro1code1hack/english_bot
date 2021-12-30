
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton



TOKEN = '1935890794:AAG1pkfgdSy9wjEq8tnA3ZzXz3FrXy0YNvQ'


# # BOT_TOKEN = '1806131427:AAG7BhdiWV2obEa8IaEBig6CxCHdIaCxcw4'
# # PAYMENTS_PROVIDER_TOKEN = '410694247:TEST:94f224d7-cd87-46e4-b1be-d05e52965191'
# #PAYMENTS_PROVIDER_TOKEN = '401643678:TEST:cbfed0a8-dba6-44df-90e4-a8945560c79a'
# Creator = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSgUhkETjfhmNzNmlCq0BGvr4yDI7NLLOhkKw&usqp=CAU'
# TIME_MACHINE_IMAGE_URL = 'http://erkelzaar.tsudao.com/models/perrotta/TIME_MACHINE.jpg'
# #import aiogram

Cancel_button = KeyboardButton("Отменить прохождение теста")
Cancel_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(Cancel_button)


# --------------------A1_grammar--------------------#
A1_inlineKeyboard1= InlineKeyboardButton('To be', callback_data='Test 45')
A1_inlineKeyboard2= InlineKeyboardButton('Question Word Order', callback_data='Test 46')
A1_inlineKeyboard3= InlineKeyboardButton('Nouns', callback_data='Test 47')
A1_inlineKeyboard4= InlineKeyboardButton('Present Simple', callback_data='Test 48')
A1_inlineKeyboard5= InlineKeyboardButton('Pronouns', callback_data='Test 49')
A1_inlineKeyboard6= InlineKeyboardButton('Present Continious', callback_data='Test 50')
A1_inlineKeyboard7= InlineKeyboardButton('Articles', callback_data='Test 51')
A1_inlineKeyboard8= InlineKeyboardButton('Past Simple', callback_data='Test 52')
A1_inlineKeyboard9= InlineKeyboardButton('Prepositions', callback_data='Test 53')
A1_inlineKeyboard10= InlineKeyboardButton('Demonstratives', callback_data='Test 54')
#A1_inlineKeyboard11= InlineKeyboardButton('Possessive case', callback_data='Test 55') -no tests!
A1_inlineKeyboard12= InlineKeyboardButton('There is/There are', callback_data='Test 56')
A1_inlineKeyboard13= InlineKeyboardButton('Future Simple', callback_data='Test 57')
A1_inlineKeyboard14= InlineKeyboardButton('Modal Verbs', callback_data='Test 58')
A1_inlineKeyboard16= InlineKeyboardButton('Adverbs of Frequency', callback_data='Test 59')
A1_inlineKeyboard17= InlineKeyboardButton('Adverbs of manner', callback_data='Test 60')
A1_get_konspekt = InlineKeyboardButton('Получить конспект' , callback_data='Get A1')

"""
A1_inlineKeyboard11, 
"""
#####################################################################################################
A1_GrammarFull=InlineKeyboardMarkup(row_width=2).add(A1_inlineKeyboard1,A1_inlineKeyboard2,A1_inlineKeyboard3,A1_inlineKeyboard4,A1_inlineKeyboard5,A1_inlineKeyboard6
,A1_inlineKeyboard7,A1_inlineKeyboard8,A1_inlineKeyboard9,A1_inlineKeyboard10,A1_inlineKeyboard12,A1_inlineKeyboard13,A1_inlineKeyboard14
,A1_inlineKeyboard16,A1_inlineKeyboard17, A1_get_konspekt)
#####################################################################################################
# --------------------A1_grammar--------------------#



# --------------------A1_listening--------------------#
A1_inlineListening1=InlineKeyboardButton('Topic 1. World Of Movies' , callback_data='Listening/2')
A1_inlineListening2=InlineKeyboardButton('Topic 2. Bookworms' , callback_data='Listening/3')
A1_inlineListening3=InlineKeyboardButton('Topic 3. Leaving On A Jet Plane' , callback_data='Listening/4')
A1_inlineListening4=InlineKeyboardButton('Topic 4. At The Airport' , callback_data='Listening/5')
A1_inlineListening5=InlineKeyboardButton('Topic 5. At The Department Store' , callback_data='Listening/6')
A1_inlineListening6=InlineKeyboardButton('Topic 6. Better Learning' , callback_data='Listening/7')
A1_inlineListening7=InlineKeyboardButton('Topic 7. Perchance To Dream' , callback_data='Listening/8')
A1_inlineListening8=InlineKeyboardButton('Topic 8. Do It Like This' , callback_data='Listening/9')

A1_inlineGetScript = InlineKeyboardButton("Получить скрипт(A1)", callback_data='Script(A1)')

A1_inlineListeningTest1=InlineKeyboardButton('Пройти тест 1' , callback_data='Test 139')
A1_inlineListeningTest2=InlineKeyboardButton('Пройти тест 2' , callback_data='Test 140')
A1_inlineListeningTest3=InlineKeyboardButton('Пройти тест 3' , callback_data='Test 141')
A1_inlineListeningTest4=InlineKeyboardButton('Пройти тест 4' , callback_data='Test 142')
A1_inlineListeningTest5=InlineKeyboardButton('Пройти тест 5' , callback_data='Test 143')
A1_inlineListeningTest6=InlineKeyboardButton('Пройти тест 6' , callback_data='Test 144')
A1_inlineListeningTest7=InlineKeyboardButton('Пройти тест 7' , callback_data='Test 145')
A1_inlineListeningTest8=InlineKeyboardButton('Пройти тест 8' , callback_data='Test 146')

#####################################################################################################
A1_ListeningFull=InlineKeyboardMarkup(row_width=2).add(A1_inlineListening1,A1_inlineListeningTest1, A1_inlineListening2,A1_inlineListeningTest2,
A1_inlineListening3,A1_inlineListeningTest3, A1_inlineListening4,A1_inlineListeningTest4,
A1_inlineListening5,A1_inlineListeningTest5, A1_inlineListening6,A1_inlineListeningTest6,
A1_inlineListening7,A1_inlineListeningTest7, A1_inlineListening8,A1_inlineListeningTest8,A1_inlineGetScript)
###########################################################################################
# --------------------A1_listening--------------------#
# A1_inlineListeningTest1
# A1_inlineListeningTest2
# A1_inlineListeningTest3
# A1_inlineListeningTest4
# A1_inlineListeningTest5
# A1_inlineListeningTest6
# A1_inlineListeningTest7
# A1_inlineListeningTest8
#--------------------A1_Reading--------------------#
A1_inlineReading1=InlineKeyboardButton('Topic 1.Memories of my first day at school' , callback_data='Topic/16')
A1_inlineReading2=InlineKeyboardButton('Topic 2.Famous people’s first jobs' , callback_data='Topic/17')
A1_inlineReading3=InlineKeyboardButton('Topic 3.Tips for travelling alone' , callback_data='Topic/19')
A1_inlineReading4=InlineKeyboardButton('Topic 4.Brecon Beacons National Park' , callback_data='Topic/21')
A1_inlineReading5=InlineKeyboardButton('Topic 5.Read the letter and answer the questions' , callback_data='Topic/22')
A1_inlineReading6=InlineKeyboardButton('Topic 6.Tom\'s Day' , callback_data='Topic/23')
A1_inlineReading7=InlineKeyboardButton('Topic 7.My Working Day' , callback_data='Topic/24')
A1_inlineReading8=InlineKeyboardButton('Topic 8.Tomas From Vienna' , callback_data='Topic/26')

A1_inlineReadingTest1=InlineKeyboardButton('Пройти тест 1' , callback_data='Test 87')
A1_inlineReadingTest2=InlineKeyboardButton('Пройти тест 2' , callback_data='Test 88')
A1_inlineReadingTest3=InlineKeyboardButton('Пройти тест 3' , callback_data='Test 89')
A1_inlineReadingTest4=InlineKeyboardButton('Пройти тест 4' , callback_data='Test 90')
A1_inlineReadingTest5=InlineKeyboardButton('Пройти тест 5' , callback_data='Test 91')
A1_inlineReadingTest6=InlineKeyboardButton('Пройти тест 6' , callback_data='Test 92')
A1_inlineReadingTest7=InlineKeyboardButton('Пройти тест 7' , callback_data='Test 93')
A1_inlineReadingTest8=InlineKeyboardButton('Пройти тест 8' , callback_data='Test 94')

#####################################################################################################
A1_ReadingFull=InlineKeyboardMarkup(row_width=2).add(A1_inlineReading1,A1_inlineReadingTest1, A1_inlineReading2,A1_inlineReadingTest2,
A1_inlineReading3,A1_inlineReadingTest3, A1_inlineReading4,A1_inlineReadingTest4,
A1_inlineReading5,A1_inlineReadingTest5, A1_inlineReading6,A1_inlineReadingTest6, A1_inlineReading7,
A1_inlineReadingTest7,A1_inlineReading8, A1_inlineReadingTest8)
#####################################################################################################
# --------------------A1_Reading--------------------#



# --------------------A2_grammar--------------------#
A2_inlineKeyboard1= InlineKeyboardButton('Present Simple', callback_data='Test 22')
A2_inlineKeyboard2= InlineKeyboardButton('Present Continuous', callback_data='Test 23')
A2_inlineKeyboard3= InlineKeyboardButton('Past Simple', callback_data='Test 24')
A2_inlineKeyboard4= InlineKeyboardButton('Infinitive', callback_data='Test 25')
A2_inlineKeyboard5= InlineKeyboardButton('Past Continuous', callback_data='Test 26')
A2_inlineKeyboard6= InlineKeyboardButton('Present Perfect', callback_data='Test 27')
A2_inlineKeyboard7= InlineKeyboardButton('Past Perfect', callback_data='Test 28')
#A2_inlineKeyboard8= InlineKeyboardButton('Gerund', callback_data='Test 29')    #####
A2_inlineKeyboard9= InlineKeyboardButton('Conditionals', callback_data='Test 30')
A2_inlineKeyboard10= InlineKeyboardButton('Passive Voice', callback_data='Test 31')
A2_inlineKeyboard11= InlineKeyboardButton('Used to', callback_data='Test 32')
A2_inlineKeyboard12= InlineKeyboardButton('Comparative Adjectives', callback_data='Test 33')
A2_inlineKeyboard13= InlineKeyboardButton('Modal verbs ', callback_data='Test 34')
A2_inlineKeyboard14= InlineKeyboardButton('Future Simple', callback_data='Test 35')
A2_inlineKeyboard15= InlineKeyboardButton('Prepositions', callback_data='Test 36')
A2_inlineKeyboard16= InlineKeyboardButton('Quantifiers ', callback_data='Test 37')
A2_get_konspekt = InlineKeyboardButton('Получить конспект' , callback_data='Get A2')

#####################################################################################################
A2_GrammarFull=InlineKeyboardMarkup(row_width=2).add(A2_inlineKeyboard1,A2_inlineKeyboard2,A2_inlineKeyboard3
,A2_inlineKeyboard4,A2_inlineKeyboard5,A2_inlineKeyboard6,A2_inlineKeyboard7,A2_inlineKeyboard9
,A2_inlineKeyboard10,A2_inlineKeyboard11,A2_inlineKeyboard12,A2_inlineKeyboard13,A2_inlineKeyboard14, A2_inlineKeyboard15,A2_inlineKeyboard16,A2_get_konspekt)
#####################################################################################################
# --------------------A2_grammar--------------------#



# --------------------A2_listening--------------------#
#####################################################################################################
#A2_inlineListening1=InlineKeyboardButton('Topic 1. The Charity Show' , callback_data='Listening/')
A2_inlineListening2=InlineKeyboardButton('Topic 2. Diana\'s New Job' , callback_data='Listening/24')
A2_inlineListening3=InlineKeyboardButton('Topic 3. The Inspector Calls' , callback_data='Listening/25')
A2_inlineListening4=InlineKeyboardButton('Topic 4. Best Friends' , callback_data='Listening/26')
A2_inlineListening5=InlineKeyboardButton('Topic 5. Checking in' , callback_data='Listening/27')
A2_inlineListening6=InlineKeyboardButton('Topic 6. Choices, Choices!' , callback_data='Listening/28')
A2_inlineListening7=InlineKeyboardButton('Topic 7. Evening Classes' , callback_data='Listening/29')
A2_inlineListening8=InlineKeyboardButton('Topic 8. Images From The Past' , callback_data='Listening/30')
A2_inlineGetScript = InlineKeyboardButton("Получить скрипт(A2)", callback_data='Listening/')

#A2_inlineListeningTest1=InlineKeyboardButton('Пройти тест 1' , callback_data='Test 1')
A2_inlineListeningTest2=InlineKeyboardButton('Пройти тест 2' , callback_data='Test 117')
A2_inlineListeningTest3=InlineKeyboardButton('Пройти тест 3' , callback_data='Test 118')
A2_inlineListeningTest4=InlineKeyboardButton('Пройти тест 4' , callback_data='Test 119')
A2_inlineListeningTest5=InlineKeyboardButton('Пройти тест 5' , callback_data='Test 120')
A2_inlineListeningTest6=InlineKeyboardButton('Пройти тест 6' , callback_data='Test 121')
A2_inlineListeningTest7=InlineKeyboardButton('Пройти тест 7' , callback_data='Test 122')
A2_inlineListeningTest8=InlineKeyboardButton('Пройти тест 8' , callback_data='Test 123')

#A2_inlineListening1,A2_inlineListeningTest1
A2_ListeningFull=InlineKeyboardMarkup(row_width=2).add(A2_inlineListening2,A2_inlineListeningTest2,
A2_inlineListening3,A2_inlineListeningTest3, A2_inlineListening4,A2_inlineListeningTest4,
A2_inlineListening5,A2_inlineListeningTest5, A2_inlineListening6,A2_inlineListeningTest6,
A2_inlineListening7,A2_inlineListeningTest7, A2_inlineListening8, A2_inlineListeningTest8,A2_inlineGetScript)
#####################################################################################################
# --------------------A2_listening--------------------#


# --------------------A2_reading--------------------#
A2_inlineReading1=InlineKeyboardButton('Topic 1. A great summer vacation' , callback_data='Topic/3')
A2_inlineReading2=InlineKeyboardButton('Topic 2. Letter to a Friend' , callback_data='Topic/6')
A2_inlineReading3=InlineKeyboardButton('Topic 3. Study skills tips' , callback_data='Topic/7')
A2_inlineReading4=InlineKeyboardButton('Topic 4. Caribbean Cruise' , callback_data='Topic/10')
A2_inlineReading5=InlineKeyboardButton('Topic 5. Weather' , callback_data='Topic/12')
A2_inlineReading6=InlineKeyboardButton('Topic 6. A day in the life of Marathon Runner' , callback_data='Topic/13')
A2_inlineReading7=InlineKeyboardButton('Topic 7. Chess' , callback_data='Topic/14')

A2_inlineReadingTest1=InlineKeyboardButton('Пройти тест 1' , callback_data='Test 95')
A2_inlineReadingTest2=InlineKeyboardButton('Пройти тест 2' , callback_data='Test 96')
A2_inlineReadingTest3=InlineKeyboardButton('Пройти тест 3' , callback_data='Test 97')
A2_inlineReadingTest4=InlineKeyboardButton('Пройти тест 4' , callback_data='Test 98')
A2_inlineReadingTest5=InlineKeyboardButton('Пройти тест 5' , callback_data='Test 99')
A2_inlineReadingTest6=InlineKeyboardButton('Пройти тест 6' , callback_data='Test 100')
A2_inlineReadingTest7=InlineKeyboardButton('Пройти тест 7' , callback_data='Test 101')
#####################################################################################################
A2_ReadingFull=InlineKeyboardMarkup(row_width=2).add(A2_inlineReading1,A2_inlineReadingTest1, A2_inlineReading2,A2_inlineReadingTest2,
A2_inlineReading3,A2_inlineReadingTest3, A2_inlineReading4,A2_inlineReadingTest4,
A2_inlineReading5,A2_inlineReadingTest5, A2_inlineReading6,A2_inlineReadingTest6, A2_inlineReading7, A2_inlineReadingTest7)
#####################################################################################################
# --------------------A2_reading--------------------#



# --------------------B1_grammar--------------------#
B1_inlineKeyboard1=InlineKeyboardButton('State Verbs and Action verbs', callback_data='Test 4')
B1_inlineKeyboard2=InlineKeyboardButton('Present Simple', callback_data='Test 2') #####!!!!!
B1_inlineKeyboard3=InlineKeyboardButton('Present Continuous', callback_data='Test 6')
B1_inlineKeyboard4=InlineKeyboardButton('Past Simple', callback_data='Test 7')
B1_inlineKeyboard5=InlineKeyboardButton('Articles', callback_data='Test 8')
B1_inlineKeyboard6=InlineKeyboardButton('Past Continuous', callback_data='Test 9')
B1_inlineKeyboard7=InlineKeyboardButton('Present Perfect', callback_data='Test 10')
B1_inlineKeyboard8=InlineKeyboardButton('Gerund and Infinitive', callback_data='Test 11')
B1_inlineKeyboard9=InlineKeyboardButton('Future Simple', callback_data='Test 12') #####!!!!!########################
B1_inlineKeyboard10=InlineKeyboardButton('Past Perfect', callback_data='Test 13')  #####!!!!!####!!!!!#######################
# B1_inlineKeyboard11=InlineKeyboardButton('Used to', callback_data='/Test1')
# B1_inlineKeyboard12=InlineKeyboardButton('Would', callback_data='/Test1')
B1_inlineKeyboard13=InlineKeyboardButton('Used to/Would/Be used to + Gerund/noun', callback_data='Test 12')
B1_inlineKeyboard14=InlineKeyboardButton('Comparative and superlative degrees of adjectives', callback_data='Test 13')
B1_inlineKeyboard15=InlineKeyboardButton('Modal verbs', callback_data='Test 14')
B1_inlineKeyboard16=InlineKeyboardButton('Past Perfect Continious', callback_data='Test 15')    
B1_inlineKeyboard17=InlineKeyboardButton('Present Perfect Continious', callback_data='Test 16')
#indirect speech!!!!
B1_inlineKeyboard18=InlineKeyboardButton('Expression of the future', callback_data='Test 18')
B1_inlineKeyboard19=InlineKeyboardButton('Passive Voice', callback_data='Test 19')
B1_inlineKeyboard20=InlineKeyboardButton('Conditionals', callback_data='Test 20')
B1_inlineKeyboard21=InlineKeyboardButton('Quantifiers', callback_data='Test 21')
B1_inlineKeyboard22=InlineKeyboardButton('Indirect speech', callback_data='Test 17')

B1_get_konspekt = InlineKeyboardButton("Получить конспект", callback_data ='Get B1')


###Check B1!!!!!!!!!!###########


####################################################################################
B1_GrammarFull=InlineKeyboardMarkup(row_width=2).add(B1_inlineKeyboard1
,B1_inlineKeyboard2, B1_inlineKeyboard3, B1_inlineKeyboard4, B1_inlineKeyboard5,B1_inlineKeyboard6, B1_inlineKeyboard7,
B1_inlineKeyboard8, B1_inlineKeyboard9, B1_inlineKeyboard10, B1_inlineKeyboard10, B1_inlineKeyboard13, B1_inlineKeyboard14, B1_inlineKeyboard15, B1_inlineKeyboard16, B1_inlineKeyboard17
, B1_inlineKeyboard18,B1_inlineKeyboard22,  B1_inlineKeyboard19,  B1_inlineKeyboard20,B1_inlineKeyboard21, B1_get_konspekt)
####################################################################################
# --------------------B1_grammar--------------------#



# --------------------B1_listening--------------------#
B1_inlineListening1=InlineKeyboardButton('Topic 1. Online Trouble' , callback_data='Listening/10')
#B1_inlineListening2=InlineKeyboardButton('Topic 2. Parent/Teacher Meeting' , callback_data='Listening/')
B1_inlineListening3=InlineKeyboardButton('Topic 3. Love Is In The Air' , callback_data='Listening/11')
B1_inlineListening4=InlineKeyboardButton('Topic 4. The Room-Mates' , callback_data='Listening/12')
B1_inlineListening5=InlineKeyboardButton('Topic 5. The Island Of Vanuatu' , callback_data='Listening/13')
B1_inlineListening6=InlineKeyboardButton('Topic 6. Remembering A Life' , callback_data='Listening/14')
B1_inlineListening7=InlineKeyboardButton('Topic 7. Getting Away From It All' , callback_data='Listening/15')
B1_inlineListening8=InlineKeyboardButton('Topic 8. Far From The Office' , callback_data='Listening/16')
B1_inlineGetScript = InlineKeyboardButton("Получить скрипт(B1)", callback_data='Listening/')

#####################################################################################################
B1_inlineListeningTest1=InlineKeyboardButton('Пройти тест 1' , callback_data='Test 124')
#B1_inlineListeningTest2=InlineKeyboardButton('Пройти тест 2' , callback_data='Test 1')
B1_inlineListeningTest3=InlineKeyboardButton('Пройти тест 3' , callback_data='Test 126')
B1_inlineListeningTest4=InlineKeyboardButton('Пройти тест 4' , callback_data='Test 127')
B1_inlineListeningTest5=InlineKeyboardButton('Пройти тест 5' , callback_data='Test 128')
B1_inlineListeningTest6=InlineKeyboardButton('Пройти тест 6' , callback_data='Test 129')
B1_inlineListeningTest7=InlineKeyboardButton('Пройти тест 7' , callback_data='Test 130')
B1_inlineListeningTest8=InlineKeyboardButton('Пройти тест 8' , callback_data='Test 131')

#B1_inlineListening2,B1_inlineListeningTest2,!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
B1_ListeningFull=InlineKeyboardMarkup(row_width=2).add(B1_inlineListening1,B1_inlineListeningTest1,
B1_inlineListening3,B1_inlineListeningTest3, B1_inlineListening4,B1_inlineListeningTest4, B1_inlineListening5,B1_inlineListeningTest5, B1_inlineListening6,B1_inlineListeningTest6,
                                                       B1_inlineListening7,B1_inlineListeningTest7, B1_inlineListening8, B1_inlineListeningTest8, B1_inlineGetScript)
#####################################################################################################
# --------------------B1_listening--------------------#



# --------------------B1_reading--------------------#
B1_inlineReading1=InlineKeyboardButton('Topic 1. A Traditional Wedding' , callback_data='Topic/1')
B1_inlineReading2=InlineKeyboardButton('Topic 2. The Hotel Of The Famous' , callback_data='Topic/2')
B1_inlineReading3=InlineKeyboardButton('Topic 3. Abraham Lincoln' , callback_data='Topic/4')
B1_inlineReading4=InlineKeyboardButton('Topic 4. Charlie Chaplin\'s Early Life' , callback_data='Topic/5')
B1_inlineReading5=InlineKeyboardButton('Topic 5. Pet Doctor' , callback_data='Topic/8')
B1_inlineReading6=InlineKeyboardButton('Topic 6. The Western Alphabet' , callback_data='Topic/9')
B1_inlineReading7=InlineKeyboardButton('Topic 7. Facebook' , callback_data='Topic/11')

B1_inlineReadingTest1=InlineKeyboardButton('Пройти тест 1' , callback_data='Test 109')
B1_inlineReadingTest2=InlineKeyboardButton('Пройти тест 2' , callback_data='Test 110')
B1_inlineReadingTest3=InlineKeyboardButton('Пройти тест 3' , callback_data='Test 111')
B1_inlineReadingTest4=InlineKeyboardButton('Пройти тест 4' , callback_data='Test 112')
B1_inlineReadingTest5=InlineKeyboardButton('Пройти тест 5' , callback_data='Test 113')
B1_inlineReadingTest6=InlineKeyboardButton('Пройти тест 6' , callback_data='Test 114')
B1_inlineReadingTest7=InlineKeyboardButton('Пройти тест 7' , callback_data='Test 115')


#####################################################################################################
B1_ReadingFull=InlineKeyboardMarkup(row_width=2).add(B1_inlineReading1,B1_inlineReadingTest1, B1_inlineReading2,B1_inlineReadingTest2,
B1_inlineReading3,B1_inlineReadingTest3, B1_inlineReading4,B1_inlineReadingTest4, B1_inlineReading5,B1_inlineReadingTest5, B1_inlineReading6,B1_inlineReadingTest6, B1_inlineReading7, B1_inlineReadingTest7,)
#####################################################################################################
# --------------------B1_reading--------------------#


# --------------------B2_grammar--------------------#

B2_inlineKeyboard1=InlineKeyboardButton('Present Simple', callback_data='Test 62')
B2_inlineKeyboard2=InlineKeyboardButton('Present Continuous', callback_data='Test 63')
B2_inlineKeyboard3=InlineKeyboardButton('Present Perfect', callback_data='Test 64')
B2_inlineKeyboard4=InlineKeyboardButton('Present Perfect Continuous', callback_data='Test 65')
B2_inlineKeyboard5=InlineKeyboardButton('Past Simple', callback_data='Test 68')
B2_inlineKeyboard6=InlineKeyboardButton('Past Continuous', callback_data='Test 69')
B2_inlineKeyboard7=InlineKeyboardButton('Past Perfect', callback_data='Test67')
B2_inlineKeyboard8=InlineKeyboardButton('Past Perfect Continuous', callback_data='Test66')
B2_inlineKeyboard9=InlineKeyboardButton('Future Simple', callback_data='Test 71')
B2_inlineKeyboard10=InlineKeyboardButton('Future Continuous', callback_data='Test 70')
B2_inlineKeyboard11=InlineKeyboardButton('Future Perfect', callback_data='Test 73')
B2_inlineKeyboard12=InlineKeyboardButton('Future Perfect Continuous', callback_data='Test 72')
B2_inlineKeyboard13=InlineKeyboardButton('Passive Voice', callback_data='Test 74')
B2_inlineKeyboard14=InlineKeyboardButton('Used to/be used to/get used to', callback_data='Test 75')
B2_inlineKeyboard15=InlineKeyboardButton('Quantifiers', callback_data='Test 76')
B2_inlineKeyboard16=InlineKeyboardButton('Comparative structures', callback_data='Test 77')
B2_inlineKeyboard17=InlineKeyboardButton('Conditionals', callback_data='Test 78')
B2_inlineKeyboard18=InlineKeyboardButton(r"I wish/If only/I'd rather", callback_data='Test 79')
B2_inlineKeyboard19=InlineKeyboardButton(r"Clauses", callback_data='Test 80')
B2_inlineKeyboard20=InlineKeyboardButton(r"Modal verbs V2.0", callback_data='Test 81')
B2_inlineKeyboard21=InlineKeyboardButton(r"Reported Speech", callback_data='Test 82')
B2_inlineKeyboard22=InlineKeyboardButton(r"Gerund and Infinitive", callback_data='Test 83')
B2_inlineKeyboard23=InlineKeyboardButton(r"All Passive Voice forms", callback_data='Test 84')
B2_inlineKeyboard24=InlineKeyboardButton(r"Linking Words", callback_data='Test 85')
B2_inlineKeyboard25=InlineKeyboardButton(r"Expression of the Future", callback_data='Test 86')
B2_get_konspekt = InlineKeyboardButton("Получить конспект", callback_data ='Get B2')

B2_GrammarFull=InlineKeyboardMarkup(row_width=2).add(B2_inlineKeyboard1,B2_inlineKeyboard2,B2_inlineKeyboard3,B2_inlineKeyboard4,
B2_inlineKeyboard5,B2_inlineKeyboard6,B2_inlineKeyboard7,B2_inlineKeyboard8,B2_inlineKeyboard9,B2_inlineKeyboard10,B2_inlineKeyboard11,
B2_inlineKeyboard12,B2_inlineKeyboard13,B2_inlineKeyboard14,B2_inlineKeyboard15,B2_inlineKeyboard16,B2_inlineKeyboard17,B2_inlineKeyboard18,
B2_inlineKeyboard19,B2_inlineKeyboard20,B2_inlineKeyboard21,B2_inlineKeyboard22,B2_inlineKeyboard23,B2_inlineKeyboard24,B2_inlineKeyboard25, B2_get_konspekt)
# --------------------B2_grammar--------------------#




# --------------------B2_reading--------------------#
B2_inlineReading1=InlineKeyboardButton('Topic 1. The Environment' , callback_data='Topic/15')
B2_inlineReading2=InlineKeyboardButton('Topic 2. The World of Parkour' , callback_data='Topic/18')
B2_inlineReading3=InlineKeyboardButton('Topic 3. Description of places' , callback_data='Topic/20')
B2_inlineReading4=InlineKeyboardButton('Topic 4. My working day' , callback_data='Topic/24')   ############@@@@@
B2_inlineReading5=InlineKeyboardButton('Topic 5. The History Of Time' , callback_data='Topic/25')
B2_inlineReading6=InlineKeyboardButton('Topic 6. Lisa Tyler' , callback_data= 'Topic/27')
B2_inlineReading7=InlineKeyboardButton('Topic 7. Are celebrities bad for you?' , callback_data='Topic/28')
#B2_inlineReading8=InlineKeyboardButton('Topic 8.' , callback_data='Test 1')

B2_inlineReadingTest1=InlineKeyboardButton('Пройти тест 1', callback_data='Test 102')
B2_inlineReadingTest2=InlineKeyboardButton('Пройти тест 2', callback_data='Test 103')
B2_inlineReadingTest3=InlineKeyboardButton('Пройти тест 3', callback_data='Test 104')
B2_inlineReadingTest4=InlineKeyboardButton('Пройти тест 4' , callback_data='Test 105')
B2_inlineReadingTest5=InlineKeyboardButton('Пройти тест 5', callback_data='Test 106')
B2_inlineReadingTest6=InlineKeyboardButton('Пройти тест 6', callback_data='Test 107')
B2_inlineReadingTest7=InlineKeyboardButton('Пройти тест 7', callback_data='Test 108')
#B2_inlineReadingTest8=InlineKeyboardButton('Пройти тест 8' , callback_data='Test 1')
#####################################################################################################
B2_ReadingFull=InlineKeyboardMarkup(row_width=2).add(B2_inlineReading1,B2_inlineReadingTest1, B2_inlineReading2,B2_inlineReadingTest2,
B2_inlineReading3,B2_inlineReadingTest3,  B2_inlineReading5,B2_inlineReadingTest5, B2_inlineReading6,B2_inlineReadingTest6,
B2_inlineReading7, B2_inlineReadingTest7,)
# --------------------B2_reading--------------------#

# B2_inlineReading4,B2_inlineReadingTest4,
# --------------------B2_listening--------------------#
B2_inlineListening1=InlineKeyboardButton('Topic 1. Boys bands' , callback_data='Listening/17')
B2_inlineListening2=InlineKeyboardButton('Topic 2. My hero' , callback_data='Listening/18')
B2_inlineListening3=InlineKeyboardButton('Topic 3. Unusual British festivals' , callback_data='Listening/19')
B2_inlineListening4=InlineKeyboardButton('Topic 4. Entertainment' , callback_data='Listening/20')
#B2_inlineListening5=InlineKeyboardButton('Topic 5. American Thanksgiving' , callback_data='Listening/21')
B2_inlineListening6=InlineKeyboardButton('Topic 6. PlayStation – Xbox Rivalry' , callback_data='Listening/21')
B2_inlineListening7=InlineKeyboardButton('Topic 7. Teenagers Who Argue' , callback_data='Listening/22')
B2_inlineListening8=InlineKeyboardButton('Topic 8. A New Kind of Snowboard Pants', callback_data='Listening/23')

B2_inlineGetScript = InlineKeyboardButton("Получить скрипт(B2)",callback_data='Script(B2)')

# --------------------Test buttons--------------------#
B2_inlineListeningTest1=InlineKeyboardButton('Пройти тест 1' , callback_data='Test 132')
B2_inlineListeningTest2=InlineKeyboardButton('Пройти тест 2' , callback_data='Test 133')
B2_inlineListeningTest3=InlineKeyboardButton('Пройти тест 3' , callback_data='Test 134')
B2_inlineListeningTest4=InlineKeyboardButton('Пройти тест 4' , callback_data='Test 135')
#B2_inlineListeningTest5=InlineKeyboardButton('Пройти тест 5' , callback_data='Test 1')
B2_inlineListeningTest6=InlineKeyboardButton('Пройти тест 6' , callback_data='Test 136')
B2_inlineListeningTest7=InlineKeyboardButton('Пройти тест 7' , callback_data='Test 137')
B2_inlineListeningTest8=InlineKeyboardButton('Пройти тест 8' , callback_data='Test 138')
# --------------------Test buttons--------------------#
#####################################################################################################   #B2_inlineListening5,B2_inlineListeningTest5,
B2_ListeningFull=InlineKeyboardMarkup(row_width=2).add(B2_inlineListening1,B2_inlineListeningTest1, B2_inlineListening2,B2_inlineListeningTest2,
B2_inlineListening3,B2_inlineListeningTest3, B2_inlineListening4,B2_inlineListeningTest4,
 B2_inlineListening6,B2_inlineListeningTest6, B2_inlineListening7,B2_inlineListeningTest7,
B2_inlineListening8, B2_inlineListeningTest8, B2_inlineGetScript)
#####################################################################################################
# --------------------B2_listening--------------------#




# -------------menu#1 the main menu ------------------#
button_name = KeyboardButton('Программа работы🎓')
button_contacts = KeyboardButton('О нас☎️')
button_test = KeyboardButton('Определить уровень❓')
button_payments = KeyboardButton('Оплатить обучение💵')
check_the_bot = KeyboardButton('Ознакомиться с ботом👀')
button_chk = KeyboardButton('Test (id)')
button_info= KeyboardButton('Информация о курсеℹ')
Main_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(button_name, button_contacts, button_test , button_payments, check_the_bot, button_info)    #(location, contact)
# -------------menu#1 the main menu ------------------#


# -------------test#1 the test menu ------------------#
button_test_info1 = KeyboardButton('Test 1')
button_test_info2 = KeyboardButton('Test 2')
button_test_info3 = KeyboardButton('Test 3')
Test_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(button_test_info1, button_test_info2, button_test_info3)
# -------------test#1 the test menu ------------------#


# ------------------ lvl menu ----------------------#
button_a1 = KeyboardButton("Beginner(A1)👶")
button_a2 = KeyboardButton("Pre-Intermediate(A2)🧒")
button_b1 = KeyboardButton("Intermediate(B1)🧑‍🎓")
button_b2 = KeyboardButton("Upper-Intermediate(B2)🧙")
button_back =KeyboardButton("Main Menu🏠")
lvl_menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(button_a1,button_a2, button_b1, button_b2, button_back)
# ------------------ lvl menu ----------------------#


# ------------------ The course A1 menu ----------------------#
button_grammarA1 = KeyboardButton('Grammar(A1)')             # название кнопки
button_backA1 = KeyboardButton('Назад')
button_listeningA1 = KeyboardButton('Listening(A1)')
button_vocabularyA1 = KeyboardButton('Vocabulary(A1)')
button_readingA1 = KeyboardButton('Reading(A1)')
MenuA1 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_grammarA1, button_readingA1, button_listeningA1, button_vocabularyA1 , button_backA1)
# ------------------ The course A1 menu ----------------------#


# ------------------ The course A2 menu ----------------------#
button_grammarA2 = KeyboardButton('Grammar(A2)')             # название кнопки
button_backA2 = KeyboardButton('Назад')
button_listeningA2 = KeyboardButton('Listening(A2)')
button_vocabularyA2 = KeyboardButton('Vocabulary(A2)')
button_readingA2 = KeyboardButton('Reading(A2)')
MenuA2 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_grammarA2, button_readingA2, button_listeningA2, button_vocabularyA2 , button_backA2)
# ------------------ The course A2 menu ----------------------#


# ------------------ The course B1 menu ----------------------#
button_grammarB1 = KeyboardButton('Grammar(B1)')             # название кнопки
button_backB1 = KeyboardButton('Назад')
button_listeningB1 = KeyboardButton('Listening(B1)')
button_vocabularyB1 = KeyboardButton('Vocabulary(B1)')
button_readingB1 = KeyboardButton('Reading(B1)')
MenuB1 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_grammarB1, button_readingB1, button_listeningB1, button_vocabularyB1 , button_backB1)
# ------------------ The course B1 menu ----------------------#

# ------------------ The course B2 menu ----------------------#
button_grammarB2 = KeyboardButton('Grammar(B2)')             # название кнопки
button_backB2 = KeyboardButton('Назад')
button_listeningB2 = KeyboardButton('Listening(B2)')
button_vocabularyB2 = KeyboardButton('Vocabulary(B2)')
button_readingB2 = KeyboardButton('Reading(B2)')
MenuB2 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_grammarB2, button_readingB2, button_listeningB2, button_vocabularyB2 , button_backB2)
# ------------------ The course B2 menu ----------------------#



cancel_test_button = KeyboardButton('Прервать тест')
cancel_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(cancel_test_button)





# payment
a1_paymentButton = InlineKeyboardButton('A1', callback_data='pay/1')
a2_paymentButton = InlineKeyboardButton('A2', callback_data='pay/2')
b1_paymentButton = InlineKeyboardButton('B1', callback_data='pay/3')
b2_paymentButton = InlineKeyboardButton('B2', callback_data='pay/4')
#full_course_paymentButton = InlineKeyboardButton('Весь курс', callback_data='pay/5')


payment_keyboard= InlineKeyboardMarkup(resize_keyboard=True).add(a1_paymentButton,
                        a2_paymentButton, b1_paymentButton,b2_paymentButton)        # check_subscriptions