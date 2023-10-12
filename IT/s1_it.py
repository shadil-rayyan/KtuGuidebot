import telebot
from telebot.types import BotDescription, KeyboardButton, ReplyKeyboardMarkup
bot = telebot.TeleBot('')

# from here start departement "IT"
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(('S1'), ('s1'))
    keyboard.row(('s1'), ('S4'))
    keyboard.row(('S5'), ('S6'))
    keyboard.row(('S7'), ('S8'))
    #keyboard.row(('back '),('Main menu'))
    keyboard.row(('contribute'))
    keyboard.row(('Whatsapp channel'))
    bot.send_message(message.chat.id, 'Welcome to my bot!', reply_markup=keyboard)



#from here start s1 for IT
@bot.message_handler(func=lambda message: message.text == "s1")
def s1_IT_button_selected(message):
    nest1_keyboard = ReplyKeyboardMarkup(resize_keyboard=True) 
    # Create two separate rows for buttons
    nest1_keyboard.row(('subject 1'))
    nest1_keyboard.row(('subject 2'))
    nest1_keyboard.row(('subject 3 '))
    nest1_keyboard.row(('subject 4'))
    nest1_keyboard.row(('Lab '))
    nest1_keyboard.row(('back_button'),('main_menu_button'))
    nest1_keyboard.row(('contribute '))
    nest1_keyboard.row(('Whatsapp channel'))

    bot.send_message(message.chat.id, 'Hello! ', reply_markup=nest1_keyboard)
    #user_states[message.chat.id] = "category_selected"

#............................. subject1 .......................................................

@bot.message_handler(func=lambda message: message.text == "subject 1")
def s1_IT_subject1_button_selected(message):
    nest2_keyboard = ReplyKeyboardMarkup(resize_keyboard=True) 
    nest2_keyboard.row(('Note'))
    nest2_keyboard.row(('Syullbus'))
    nest2_keyboard.row(('Textbook '))
    nest2_keyboard.row(('Question paper & Solved Question paper'))
    nest2_keyboard.row(('importent topics '))
    nest2_keyboard.row(('contribute'))
    nest2_keyboard.row(('back_button'),('main_menu_button'),('category_selected'))
    bot.send_message(message.chat.id, 'H.', reply_markup=nest2_keyboard)

    
    #user_states[message.chat.id] = "category_selected"

@bot.message_handler(func=lambda message: message.text == "Note")
def s1_IT_subject1_note_button_selected(message):
    nest3_keyboard = ReplyKeyboardMarkup(resize_keyboard=True) 
    nest3_keyboard.row(('module  1'),('module 2'))
    nest3_keyboard.row(('module  3'),('module 4'))
    nest3_keyboard.row(('module  5'),('module 2'))
    nest3_keyboard.row(('back_button'),('main_menu_button'),('category_selected'))
    bot.send_message(message.chat.id, 'H.', reply_markup=nest3_keyboard)

@bot.message_handler(func=lambda message: message.text == "module 1")
def s1_IT_subject1_Module1_selected(message):
   #pdf_url = '#' 
   #bot.send.document(message.chat.id,#pdf_url)
@bot.message_handler(func=lambda message: message.text == "module 2")
def s1_IT_subject1_Module2_selected(message):
   #pdf_url = '#' 
   #bot.send.document(message.chat.id,#pdf_url)
@bot.message_handler(func=lambda message: message.text == "module 3")
def s1_IT_subject1_Module3_selected(message):
   #pdf_url = '#' 
   #bot.send.document(message.chat.id,#pdf_url)
@bot.message_handler(func=lambda message: message.text == "module 4")
def s1_IT_subject1_Module4_selected(message):
   #pdf_url = '#' 
   #bot.send_document(message.chat.id,#pdf_url)

@bot.message_handler(func=lambda message: message.text == "module 5")
def s1_IT_subject1_module5_selected(message):
   #pdf_url = '#' 
    #bot.send.document(message.chat.id,#pdf_url)

# from here start syullbus for s1 m1 
@bot.message_handler(func=lambda message: message.text == "syullbus")
def s1_IT_subject1_Syullbus_selected(message):

   #pdf_url = '#' 
    #bot.send_photo(message.chat.id,#pdf_url)


@bot.message_handler(func=lambda message: message.text == "textbook")
def s1_IT_subject1_textbook_selected(message):

    #photo_url = '#' 
    #bot.send_photo(message.chat.id, photo_url)


@bot.message_handler(func=lambda message: message.text == "Question paper & solved Question paper")
def s1_IT_subject1_Qp_selected(message):
  nest4_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
  nest4_keyboard.row(("2022"))
  nest4_keyboard.row(('2021'))
  nest4_keyboard.row(("2020"))
  nest4_keyboard.row("2019")
  nest4_keyboard.row(('back '),('Main menu'))
  bot.send.message(message.chat.id,'',reply_markup=nest4_keyboard)

@bot.message_handler(func=lambda message: message.text == "2022")
def s1_IT_subject1_Qp2022_selected(message):
    #pdf_url = '#' 
    #bot.send_photo(message.chat.id,#pdf_url)
@bot.message_handler(func=lambda message: message.text == ('2021'))
def s1_IT_subject1_Qp2021_selected(message):
    #pdf_url = '#' 
    #bot.send_photo(message.chat.id,#pdf_url)
@bot.message_handler(func=lambda message: message.text == "2020")
def s1_IT_subject1_Qp2020_selected(message):
    #pdf_url = '#' 
    #bot.send_photo(message.chat.id,#pdf_url)
@bot.message_handler(func=lambda message: message.text == "2019")
def s1_IT_subject1_Qp2019_selected(message):
    #pdf_url = '#' 
    #bot.send_photo(message.chat.id,#pdf_url)

@bot.message_handler(func=lambda message: message.text == "Importent topics")
def s1_IT_subject1_Imp_selected(message):
    #pdf_url = '#' 
    #bot.send_photo(message.chat.id,#pdf_url)
 #............................. subject1ject 2.......................................................


@bot.message_handler(func=lambda message: message.text == "subject 2")
def s1_IT_subject2_button_selected(message):
    nest2_keyboard = ReplyKeyboardMarkup(resize_keyboard=True) 
    nest2_keyboard.row(('Note'))
    nest2_keyboard.row(('Syullbus'))
    nest2_keyboard.row(('Textbook '))
    nest2_keyboard.row(('Question paper'))
    nest2_keyboard.row(('Solved Question paper'))
    nest2_keyboard.row(('importent topics '))
    nest2_keyboard.row(('contribute'))
    nest2_keyboard.row(('back_button'),('main_menu_button'),('category_selected'))
    bot.send_message(message.chat.id, 'H.', reply_markup=nest2_keyboard)

@bot.message_handler(func=lambda message: message.text == "Note")
def subject2_note_button_selected(message):
    nest3_keyboard = ReplyKeyboardMarkup(resize_keyboard=True) 
    nest3_keyboard.row(('module  1'),('module 2'))
    nest3_keyboard.row(('module  3'),('module 4'))
    nest3_keyboard.row(('module  5'),('module 2'))
    nest3_keyboard.row(('back_button'),('main_menu_button'),('category_selected'))
    bot.send_message(message.chat.id, 'H.', reply_markup=nest3_keyboard)

@bot.message_handler(func=lambda message: message.text == "module 1")
def s1_IT_subject2_Module1_selected(message):
   #pdf_url = '#' 
   #bot.send.document(message.chat.id,#pdf_url)
@bot.message_handler(func=lambda message: message.text == "module 2")
def s1_IT_subject2_Module2_selected(message):
   #pdf_url = '#' 
   #bot.send.document(message.chat.id,#pdf_url)
@bot.message_handler(func=lambda message: message.text == "module 3")
def s1_IT_subject1_Module3_selected(message):
   #pdf_url = '#' 
   #bot.send.document(message.chat.id,#pdf_url)
@bot.message_handler(func=lambda message: message.text == "module 4")
def s1_IT_subject2_Module4_selected(message):
   #pdf_url = '#' 
   #bot.send_document(message.chat.id,#pdf_url)

@bot.message_handler(func=lambda message: message.text == "module 5")
def s1_IT_subject2_Module5_selected(message):
   #pdf_url = '#' 
    #bot.send.document(message.chat.id,#pdf_url)

# from here start syullbus for s1 m1 
@bot.message_handler(func=lambda message: message.text == "syullbus")
def s1_IT_subject2_Syullbus_selected(message):

   #pdf_url = '#' 
    #bot.send_photo(message.chat.id,#pdf_url)


@bot.message_handler(func=lambda message: message.text == "textbook")
def s1_IT_subject2_textbook_selected(message):

    #photo_url = '#' 
    #bot.send_photo(message.chat.id, photo_url)


@bot.message_handler(func=lambda message: message.text == "Question paper & solved Question paper")
def s1_IT_subject2_Qp_selected(message):
  nest4_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
  nest4_keyboard.row(("2022"))
  nest4_keyboard.row(('2021'))
  nest4_keyboard.row(("2019"))
  nest4_keyboard.row(('2019'))
  nest4_keyboard.row(('back'),('menu'))
  #keyboard.row(('back '),('Main menu'))
  bot.send.message(message.chat.id,'',reply_markup=nest4_keyboard)

@bot.message_handler(func=lambda message: message.text == "2022")
def  s1_IT_subject2_Qp2022_selected(message):
    #pdf_url = '#' 
    #bot.send_photo(message.chat.id,#pdf_url)
@bot.message_handler(func=lambda message: message.text == ('2021'))
def s1_IT_subject2_Qp2021_selected(message):
    #pdf_url = '#' 
    #bot.send_photo(message.chat.id,#pdf_url)
@bot.message_handler(func=lambda message: message.text == "2020")
def s1_IT_subject2_Qp2022_selected(message):
    #pdf_url = '#' 
    #bot.send_photo(message.chat.id,#pdf_url)
@bot.message_handler(func=lambda message: message.text == "2019")
def s1_IT_subject2_Qp2022_selected(message):
    #pdf_url = '#' 
    #bot.send_photo(message.chat.id,#pdf_url)

@bot.message_handler(func=lambda message: message.text == "Importent topics")
def s1_IT_subject2_Imp_selected(message):
    #pdf_url = '#' 
    #bot.send_photo(message.chat.id,#pdf_url)

#......................subject1ject 3......................................................................

@bot.message_handler(func=lambda message: message.text == "subject 3")
def s1_IT_subject4_button_selected(message):
    nest2_keyboard = ReplyKeyboardMarkup(resize_keyboard=True) 
    nest2_keyboard.row(('Note'))
    nest2_keyboard.row(('Syullbus'))
    nest2_keyboard.row(('Textbook '))
    nest2_keyboard.row(('Question paper'))
    nest2_keyboard.row(('Solved Question paper'))
    nest2_keyboard.row(('importent topics '))
    nest2_keyboard.row(('contribute'))
    nest2_keyboard.row(('back_button'),('main_menu_button'),('category_selected'))
    bot.send_message(message.chat.id, 'H.', reply_markup=nest2_keyboard)

@bot.message_handler(func=lambda message: message.text == "Note")
def subject3_note_button_selected(message):
    nest3_keyboard = ReplyKeyboardMarkup(resize_keyboard=True) 
    nest3_keyboard.row(('module  1'),('module 2'))
    nest3_keyboard.row(('module  3'),('module 4'))
    nest3_keyboard.row(('module  5'),('module 2'))
    nest3_keyboard.row(('back_button'),('main_menu_button'),('category_selected'))
    bot.send_message(message.chat.id, 'H.', reply_markup=nest3_keyboard)

@bot.message_handler(func=lambda message: message.text == "module 1")
def s1_IT_subject3_Module1_selected(message):
   #pdf_url = '#' 
   #bot.send.document(message.chat.id,#pdf_url)
@bot.message_handler(func=lambda message: message.text == "module 2")
def s1_IT_subject3_Module2_selected(message):
   #pdf_url = '#' 
   #bot.send.document(message.chat.id,#pdf_url)
@bot.message_handler(func=lambda message: message.text == "module 3")
def s1_IT_subject1_Module3_selected(message):
   #pdf_url = '#' 
   #bot.send.document(message.chat.id,#pdf_url)
@bot.message_handler(func=lambda message: message.text == "module 4")
def s1_IT_subject3_Module4_selected(message):
   #pdf_url = '#' 
   #bot.send_document(message.chat.id,#pdf_url)

@bot.message_handler(func=lambda message: message.text == "module 5")
def s1_IT_subject3_Module5_selected(message):
   #pdf_url = '#' 
    #bot.send.document(message.chat.id,#pdf_url)

# from here start syullbus for s1 m1 
@bot.message_handler(func=lambda message: message.text == "syullbus")
def s1_IT_subject3_Syullbus_selected(message):

   #pdf_url = '#' 
    #bot.send_photo(message.chat.id,#pdf_url)


@bot.message_handler(func=lambda message: message.text == "textbook")
def s1_IT_subject3_textbook_selected(message):

    #photo_url = '#' 
    #bot.send_photo(message.chat.id, photo_url)


@bot.message_handler(func=lambda message: message.text == "Question paper & solved Question paper")
def s1_IT_subject3_Qp_selected(message):
  nest4_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
  nest4_keyboard.row(("2022"))
  nest4_keyboard.row(('2021'))
  nest4_keyboard.row(("2019"))
  nest4_keyboard.row(('2019'))
  nest4_keyboard.row(('back'),('menu'))
  bot.send.message(message.chat.id,'',reply_markup=nest4_keyboard)

@bot.message_handler(func=lambda message: message.text == "2022")
def s1_IT_subject3_Qp2022_selected(message):
    #pdf_url = '#' 
    #bot.send_photo(message.chat.id,#pdf_url)
@bot.message_handler(func=lambda message: message.text == ('2021'))
def s1_IT_subject3_Qp2021_selected(message):
    #pdf_url = '#' 
    #bot.send_photo(message.chat.id,#pdf_url)
@bot.message_handler(func=lambda message: message.text == "2020")
def s1_IT_subject3_Qp2022_selected(message):
    #pdf_url = '#' 
    #bot.send_photo(message.chat.id,#pdf_url)
@bot.message_handler(func=lambda message: message.text == ('2019'))
def s1_IT_subject3_Qp2022_selected(message):
    #pdf_url = '#' 
    #bot.send_photo(message.chat.id,#pdf_url)

@bot.message_handler(func=lambda message: message.text == "Importent topics")
def s1_IT_subject3_Imp_selected(message):
    #pdf_url = '#' 
    #bot.send_photo(message.chat.id,#pdf_url)

#......................subject 4..........................................................................

@bot.message_handler(func=lambda message: message.text == "subject 4")
def s1_IT_subject4_button_selected(message):
    nest2_keyboard = ReplyKeyboardMarkup(resize_keyboard=True) 
    nest2_keyboard.row(('Note'))
    nest2_keyboard.row(('Syullbus'))
    nest2_keyboard.row(('Textbook '))
    nest2_keyboard.row(('Question paper'))
    nest2_keyboard.row(('Solved Question paper'))
    nest2_keyboard.row(('importent topics '))
    nest2_keyboard.row(('contribute'))
    nest2_keyboard.row(('back_button'),('main_menu_button'),('category_selected'))
    bot.send_message(message.chat.id, 'H.', reply_markup=nest2_keyboard)

@bot.message_handler(func=lambda message: message.text == "Note")
def subject4_note_button_selected(message):
    nest3_keyboard = ReplyKeyboardMarkup(resize_keyboard=True) 
    nest3_keyboard.row(('module  1'),('module 2'))
    nest3_keyboard.row(('module  3'),('module 4'))
    nest3_keyboard.row(('module  5'),('module 2'))
    nest3_keyboard.row(('back_button'),('main_menu_button'),('category_selected'))
    bot.send_message(message.chat.id, 'H.', reply_markup=nest3_keyboard)

@bot.message_handler(func=lambda message: message.text == "module 1")
def s1_IT_subject4_Module1_selected(message):
   #pdf_url = '#' 
   #bot.send.document(message.chat.id,#pdf_url)
@bot.message_handler(func=lambda message: message.text == "module 2")
def s1_IT_subject4_Module2_selected(message):
   #pdf_url = '#' 
   #bot.send.document(message.chat.id,#pdf_url)
@bot.message_handler(func=lambda message: message.text == "module 3")
def s1_IT_subject1_Module3_selected(message):
   #pdf_url = '#' 
   #bot.send.document(message.chat.id,#pdf_url)
@bot.message_handler(func=lambda message: message.text == "module 4")
def s1_IT_subject4_Module4_selected(message):
   #pdf_url = '#' 
   #bot.send_document(message.chat.id,#pdf_url)

@bot.message_handler(func=lambda message: message.text == "module 5")
def s1_IT_subject4_Module5_selected(message):
   #pdf_url = '#' 
    #bot.send.document(message.chat.id,#pdf_url)

# from here start syullbus for s1 m1 
@bot.message_handler(func=lambda message: message.text == "syullbus")
def s1_IT_subject4_Syullbus_selected(message):

   #pdf_url = '#' 
    #bot.send_photo(message.chat.id,#pdf_url)


@bot.message_handler(func=lambda message: message.text == "textbook")
def s1_IT_subject4_textbook_selected(message):

    #photo_url = '#' 
    #bot.send_photo(message.chat.id, photo_url)


@bot.message_handler(func=lambda message: message.text == "Question paper & solved Question paper")
def s1_IT_subject4_Qp_selected(message):
  nest4_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
  nest4_keyboard.row(("2022"))
  nest4_keyboard.row(('2021'))
  nest4_keyboard.row(("2019"))
  nest4_keyboard.row(('2019'))
  nest4_keyboard.row(('back'),('menu'))
  bot.send.message(message.chat.id,'',reply_markup=nest4_keyboard)

@bot.message_handler(func=lambda message: message.text == "2022")
def s1_IT_subject4_Qp2022_selected(message):
    #pdf_url = '#' 
    #bot.send_photo(message.chat.id,#pdf_url)
@bot.message_handler(func=lambda message: message.text == "2021")
def s1_IT_subject4_Qp2021_selected(message):
    #pdf_url = '#' 
    #bot.send_photo(message.chat.id,#pdf_url)
@bot.message_handler(func=lambda message: message.text == "2020")
def s1_IT_subject4_Qp2022_selected(message):
    #pdf_url = '#' 
    #bot.send_photo(message.chat.id,#pdf_url)
@bot.message_handler(func=lambda message: message.text == "2019")
def s1_IT_subject4_Qp2022_selected(message):
    #pdf_url = '#' 
    #bot.send_photo(message.chat.id,#pdf_url)

@bot.message_handler(func=lambda message: message.text == "Importent topics")
def s1_IT_subject4_Imp_selected(message):
    #pdf_url = '#' 
    #bot.send_photo(message.chat.id,#pdf_url)

#....................subject 5......................................................

@bot.message_handler(func=lambda message: message.text == "subject 5")
def s1_IT_subject5_button_selected(message):
    nest2_keyboard = ReplyKeyboardMarkup(resize_keyboard=True) 
    nest2_keyboard.row(('Note'))
    nest2_keyboard.row(('Syullbus'))
    nest2_keyboard.row(('Textbook '))
    nest2_keyboard.row(('Question paper'))
    nest2_keyboard.row(('Solved Question paper'))
    nest2_keyboard.row(('importent topics '))
    nest2_keyboard.row(('contribute'))
    nest2_keyboard.row(('back_button'),('main_menu_button'),('category_selected'))
    bot.send_message(message.chat.id, 'H.', reply_markup=nest2_keyboard)

@bot.message_handler(func=lambda message: message.text == "Note")
def subject5_note_button_selected(message):
    nest3_keyboard = ReplyKeyboardMarkup(resize_keyboard=True) 
    nest3_keyboard.row(('module  1'),('module 2'))
    nest3_keyboard.row(('module  3'),('module 4'))
    nest3_keyboard.row(('module  5'),('module 2'))
    nest3_keyboard.row(('back_button'),('main_menu_button'),('category_selected'))
    bot.send_message(message.chat.id, 'H.', reply_markup=nest3_keyboard)

@bot.message_handler(func=lambda message: message.text == "module 1")
def s1_IT_subject5_Module1_selected(message):
   #pdf_url = '#' 
   #bot.send.document(message.chat.id,#pdf_url)
@bot.message_handler(func=lambda message: message.text == "module 2")
def s1_IT_subject5_Module2_selected(message):
   #pdf_url = '#' 
   #bot.send.document(message.chat.id,#pdf_url)
@bot.message_handler(func=lambda message: message.text == "module 3")
def s1_IT_subject1_Module3_selected(message):
   #pdf_url = '#' 
   #bot.send.document(message.chat.id,#pdf_url)
@bot.message_handler(func=lambda message: message.text == "module 4")
def s1_IT_subject5_Module4_selected(message):
   #pdf_url = '#' 
   #bot.send_document(message.chat.id,#pdf_url)

@bot.message_handler(func=lambda message: message.text == "module 5")
def s1_IT_subject5_Module5_selected(message):
   #pdf_url = '#' 
    #bot.send.document(message.chat.id,#pdf_url)

# from here start syullbus for s1 m1 
@bot.message_handler(func=lambda message: message.text == "syullbus")
def s1_IT_subject5_Syullbus_selected(message):

   #pdf_url = '#' 
    #bot.send_photo(message.chat.id,#pdf_url)


@bot.message_handler(func=lambda message: message.text == "textbook")
def s1_IT_subject5_textbook_selected(message):

    #photo_url = '#' 
    #bot.send_photo(message.chat.id, photo_url)


@bot.message_handler(func=lambda message: message.text == "Question paper & solved Question paper")
def s1_IT_subject5_Qp_selected(message):
  nest4_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
  nest4_keyboard.row(("2022"))
  nest4_keyboard.row(('2021'))
  nest4_keyboard.row(("2019"))
  nest4_keyboard.row(('2019'))
  nest4_keyboard.row(('back'),('menu'))
  bot.send.message(message.chat.id,'',reply_markup=nest4_keyboard)

@bot.message_handler(func=lambda message: message.text == "2022")
def s1_IT_subject5_Qp2022_selected(message):
    #pdf_url = '#' 
    #bot.send_photo(message.chat.id,#pdf_url)
@bot.message_handler(func=lambda message: message.text == "2021")
def s1_IT_subject5_Qp2021_selected(message):
    #pdf_url = '#' 
    #bot.send_photo(message.chat.id,#pdf_url)
@bot.message_handler(func=lambda message: message.text == "2020")
def s1_IT_subject5_Qp2022_selected(message):
    #pdf_url = '#' 
    #bot.send_photo(message.chat.id,#pdf_url)
@bot.message_handler(func=lambda message: message.text == "2019")
def s1_IT_subject5_Qp2022_selected(message):
    #pdf_url = '#' 
    #bot.send_photo(message.chat.id,#pdf_url)

@bot.message_handler(func=lambda message: message.text == "Importent topics")
def s1_IT_subject5_Imp_selected(message):
    #pdf_url = '#' 
    #bot.send_photo(message.chat.id,#pdf_url)

#....................Lab..................................................
@bot.message_handler(func=lambda message: message.text == "Lab 1")
def s1_IT_Lab1_button_selected(message):
    nest21_keyboard = ReplyKeyboardMarkup(resize_keyboard=True) 
    nest21_keyboard.row(('Lab manual'))
    nest21_keyboard.row(('Viva Questions'))
    nest21_keyboard.row(('Practical Record'))
    nest21_keyboard.row(('contribute'))
    nest21_keyboard.row(('back_button'),('main_menu_button'),('category_selected'))
    bot.send_message(message.chat.id, 'H.', reply_markup=nest21_keyboard)

@bot.message_handler(func=lambda message: message.text == "Lab 1")
def s1_IT_Lab1_Labmanual_selected(message):
    #pdf_url = '#' 
    #bot.send_photo(message.chat.id,#pdf_url)

@bot.message_handler(func=lambda message: message.text == "Lab 1")
def s1_IT_Lab1_vivaQuestion_selected(message):
    #pdf_url = '#' 
    #bot.send_photo(message.chat.id,#pdf_url)

@bot.message_handler(func=lambda message: message.text == "Lab 1")
def s1_IT_Lab1_PracticalRecord_selected(message):
    #pdf_url = '#' 
    #bot.send_photo(message.chat.id,#pdf_url

#................Lab 2...............................
@bot.message_handler(func=lambda message: message.text == "Lab 2")
def s1_IT_lab2_button_selected(message):
    nest21_keyboard = ReplyKeyboardMarkup(resize_keyboard=True) 
    nest21_keyboard.row(('Lab manual'))
    nest21_keyboard.row(('Viva Questions'))
    nest21_keyboard.row(('Practical Record'))
    nest21_keyboard.row(('contribute'))
    nest21_keyboard.row(('back_button'),('main_menu_button'),('category_selected'))
    bot.send_message(message.chat.id, 'H.', reply_markup=nest21_keyboard)

@bot.message_handler(func=lambda message: message.text == "Lab 1")
def s1_IT_lab2_Labmanual_selected(message):
    #pdf_url = '#' 
    #bot.send_photo(message.chat.id,#pdf_url)

@bot.message_handler(func=lambda message: message.text == "Lab 1")
def s1_IT_lab2_vivaQuestion_selected(message):
    #pdf_url = '#' 
    #bot.send_photo(message.chat.id,#pdf_url)

@bot.message_handler(func=lambda message: message.text == "Lab 1")
def s1_IT_lab2_PracticalRecord_selected(message):
    #pdf_url = '#' 
    #bot.send_photo(message.chat.id,#pdf_url
#.............................................................
@bot.message_handler(func=lambda message: message.text == "Contribute")
def s1_IT_Contribute_selected(message):

    #message_url=''
    #bot.send.message(message.chat.id,message_url)
@bot.message_handler(func=lambda message: message.text == "Whatsapp Group")
def s1_IT_whatsappGroup_selected(message):
    #message_url=''
    #bot.send.message(message.chat.id,message_url)
