
import telebot
from telebot.types import BotDescription, KeyboardButton, ReplyKeyboardMarkup
bot = telebot.TeleBot('6217202010:AAHKt02eMHuJp6X2OVB-3iQ7Fj58jqmYdjU')

# User states dictionary to keep track of user's current state
user_states = {}
# from here start departement "CSE"

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(('s1'), ('S2'))
    keyboard.row(('s1'), ('S4'))
    keyboard.row(('S5'), ('S6'))
    keyboard.row(('S7'), ('S8'))
    keyboard.row(('Contribute'))
    keyboard.row(('Whatsapp channel'))
    bot.send_message(message.chat.id, 'Welcome to my bot!', reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "Main menu")
def main_menu_button_clicked(message):
    # Handle the "Main Menu" button click by sending the main menu again
    start(message)

#from here start s1 for CSE
@bot.message_handler(func=lambda message: message.text == "s1")
def s1_cse_button_selected(message):
    nest1_keyboard = ReplyKeyboardMarkup(resize_keyboard=True) 
    # Create two separate rows for buttons
    nest1_keyboard.row(('subject 1'))
    nest1_keyboard.row(('subject 2'))
    nest1_keyboard.row(('subject 3 '))
    nest1_keyboard.row(('subject 4'))
    nest1_keyboard.row(('subject 5'))
    nest1_keyboard.row(('subject 6'))
    nest1_keyboard.row(('Lab '))
    nest1_keyboard.row(('Back'),('Main menu'))
    nest1_keyboard.row(('contribute '))
    nest1_keyboard.row(('Whatsapp channel'))

    bot.send_message(message.chat.id, 'Hello! ', reply_markup=nest1_keyboard)
    user_states[message.chat.id] = "s1_cse_button_selected"

#............................. subject1 .......................................................

@bot.message_handler(func=lambda message: message.text == "subject 1")
def s1_cse_subject1_button_selected(message):
    nest2_keyboard = ReplyKeyboardMarkup(resize_keyboard=True) 
    nest2_keyboard.row(('Note'))
    nest2_keyboard.row(('Syullbus'))
    #nest2_keyboard.row(('Textbook '))
    nest2_keyboard.row(('Question paper & Solved Question paper'))
    #nest2_keyboard.row(('importent topics '))
    nest2_keyboard.row(('contribute'))
    nest2_keyboard.row(('Back'),('Main menu'))
    bot.send_message(message.chat.id, 'H.', reply_markup=nest2_keyboard)
    user_states[message.chat.id] = "s1_cse_subject1_button_selected"

@bot.message_handler(func=lambda message: message.text == "Note")
def s1_cse_subject1_note_button_selected(message):
    nest3_keyboard = ReplyKeyboardMarkup(resize_keyboard=True) 
    nest3_keyboard.row(('module  1'),('module 2'))
    nest3_keyboard.row(('module  3'),('module 4'))
    nest3_keyboard.row(('module  5'))
    nest3_keyboard.row(('Back'),('Main menu'))
    bot.send_message(message.chat.id, 'H.', reply_markup=nest3_keyboard)
    user_states[message.chat.id] = "s1_cse_subject1_note_button_selected"

# @bot.message_handler(func=lambda message: message.text == "module 1")
# def s1_cse_subject1_Module1_selected(message):
#    #pdf_url = '#' 
#    #bot.send.document(message.chat.id,#pdf_url)
# @bot.message_handler(func=lambda message: message.text == "module 2")
# def s1_cse_subject1_Module2_selected(message):
#    #pdf_url = '#' 
#    #bot.send.document(message.chat.id,#pdf_url)
# @bot.message_handler(func=lambda message: message.text == "module 3")
# def s1_cse_subject1_Module3_selected(message):
#    #pdf_url = '#' 
#    #bot.send.document(message.chat.id,#pdf_url)
# @bot.message_handler(func=lambda message: message.text == "module 4")
# def s1_cse_subject1_Module4_selected(message):
#    #pdf_url = '#' 
#    #bot.send_document(message.chat.id,#pdf_url)

# @bot.message_handler(func=lambda message: message.text == "module 5")
# def s1_cse_subject1_module5_selected(message):
#    #pdf_url = '#' 
#     #bot.send.document(message.chat.id,#pdf_url)

# # from here start syullbus for s1 m1 
# @bot.message_handler(func=lambda message: message.text == "syullbus")
# def s1_cse_subject1_Syullbus_selected(message):

#    #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)


# @bot.message_handler(func=lambda message: message.text == "textbook")
# def s1_cse_subject1_textbook_selected(message):

#     #photo_url = '#' 
#     #bot.send_photo(message.chat.id, photo_url)


@bot.message_handler(func=lambda message: message.text == "Question paper & solved Question paper")
def s1_cse_subject1_Qp_selected(message):
  nest4_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
  nest4_keyboard.row(("2022"))
  nest4_keyboard.row(('2021'))
  nest4_keyboard.row(("2020"))
  nest4_keyboard.row("2019")
  nest4_keyboard.row(('back '),('Main menu'))
  bot.send.message(message.chat.id,'',reply_markup=nest4_keyboard)
  user_states[message.chat.id] = "s1_cse_subject1_Qp_selected"

# @bot.message_handler(func=lambda message: message.text == "2022")
# def s1_cse_subject1_Qp2022_selected(message):
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
# @bot.message_handler(func=lambda message: message.text == ('2021'))
# def s1_cse_subject1_Qp2021_selected(message):
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
# @bot.message_handler(func=lambda message: message.text == "2020")
# def s1_cse_subject1_Qp2020_selected(message):
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
# @bot.message_handler(func=lambda message: message.text == "2019")
# def s1_cse_subject1_Qp2019_selected(message):
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
# @bot.message_handler(func=lambda message: message.text == "Importent topics")
# def s1_cse_subject1_Imp_selected(message):
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
 #............................. subject1ject 2.......................................................


@bot.message_handler(func=lambda message: message.text == "subject 2")
def s1_cse_subject2_button_selected(message):
    nest2_keyboard = ReplyKeyboardMarkup(resize_keyboard=True) 
    nest2_keyboard.row(('Note'))
    nest2_keyboard.row(('Syullbus'))
    #nest2_keyboard.row(('Textbook '))
    nest2_keyboard.row(('Question paper & solved Question paper'))
    #nest2_keyboard.row(('Solved Question paper'))
    #nest2_keyboard.row(('importent topics '))
    nest2_keyboard.row(('contribute'))
    nest2_keyboard.row(('Back'),('Main menu'))
    bot.send_message(message.chat.id, 'H.', reply_markup=nest2_keyboard)
    user_states[message.chat.id] = "s1_cse_subject2_button_selected"

@bot.message_handler(func=lambda message: message.text == "Note")
def subject2_note_button_selected(message):
    nest3_keyboard = ReplyKeyboardMarkup(resize_keyboard=True) 
    nest3_keyboard.row(('module  1'),('module 2'))
    nest3_keyboard.row(('module  3'),('module 4'))
    nest3_keyboard.row(('module  5'),('module 2'))
    nest3_keyboard.row(('Back'),('Main menu'))
    bot.send_message(message.chat.id, 'H.', reply_markup=nest3_keyboard)
    user_states[message.chat.id] = "subject2_note_button_selected"

# @bot.message_handler(func=lambda message: message.text == "module 1")
# def s1_cse_subject2_Module1_selected(message):
#    #pdf_url = '#' 
#    #bot.send.document(message.chat.id,#pdf_url)
# @bot.message_handler(func=lambda message: message.text == "module 2")
# def s1_cse_subject2_Module2_selected(message):
#    #pdf_url = '#' 
#    #bot.send.document(message.chat.id,#pdf_url)
# @bot.message_handler(func=lambda message: message.text == "module 3")
# def s1_cse_subject1_Module3_selected(message):
#    #pdf_url = '#' 
#    #bot.send.document(message.chat.id,#pdf_url)
# @bot.message_handler(func=lambda message: message.text == "module 4")
# def s1_cse_subject2_Module4_selected(message):
#    #pdf_url = '#' 
#    #bot.send_document(message.chat.id,#pdf_url)

# @bot.message_handler(func=lambda message: message.text == "module 5")
# def s1_cse_subject2_Module5_selected(message):
#    #pdf_url = '#' 
#     #bot.send.document(message.chat.id,#pdf_url)

# # from here start syullbus for s1 m1 
# @bot.message_handler(func=lambda message: message.text == "syullbus")
# def s1_cse_subject2_Syullbus_selected(message):

#    #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)


# @bot.message_handler(func=lambda message: message.text == "textbook")
# def s1_cse_subject2_textbook_selected(message):

#     #photo_url = '#' 
#     #bot.send_photo(message.chat.id, photo_url)


@bot.message_handler(func=lambda message: message.text == "Question paper & solved Question paper")
def s1_cse_subject2_Qp_selected(message):
  nest4_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
  nest4_keyboard.row(("2022"))
  nest4_keyboard.row(('2021'))
  nest4_keyboard.row(("2019"))
  nest4_keyboard.row(('2019'))
  nest4_keyboard.row(('back'),('menu'))
  nest4_keyboard.row(('back '),('Main menu'))
  bot.send.message(message.chat.id,'',reply_markup=nest4_keyboard)
  user_states[message.chat.id] = "s1_cse_subject2_Qp_selected"

# @bot.message_handler(func=lambda message: message.text == "2022")
# def s1_cse_subject2_Qp2022_selected(message):
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
# @bot.message_handler(func=lambda message: message.text == ('2021'))
# def s1_cse_subject2_Qp2021_selected(message):
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
# @bot.message_handler(func=lambda message: message.text == "2020")
# def s1_cse_subject2_Qp2020_selected(message):
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
# @bot.message_handler(func=lambda message: message.text == "2019")
# def s1_cse_subject2_Qp2019_selected(message):
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
# @bot.message_handler(func=lambda message: message.text == "Importent topics")
# def s1_cse_subject2_Imp_selected(message):
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)

#......................subject1ject 3......................................................................

@bot.message_handler(func=lambda message: message.text == "subject 3")
def s1_cse_subject3_button_selected(message):
    nest2_keyboard = ReplyKeyboardMarkup(resize_keyboard=True) 
    nest2_keyboard.row(('Note'))
    nest2_keyboard.row(('Syullbus'))
    #nest2_keyboard.row(('Textbook '))
    nest2_keyboard.row(('Question paper & solved Question paper'))
    #nest2_keyboard.row(('importent topics '))
    nest2_keyboard.row(('contribute'))
    nest2_keyboard.row(('Back'),('Main menu'))
    bot.send_message(message.chat.id, 'H.', reply_markup=nest2_keyboard)
    user_states[message.chat.id] = "s1_cse_subject4_button_selected"

@bot.message_handler(func=lambda message: message.text == "Note")
def s1_subject3_note_button_selected(message):
    nest3_keyboard = ReplyKeyboardMarkup(resize_keyboard=True) 
    nest3_keyboard.row(('module  1'),('module 2'))
    nest3_keyboard.row(('module  3'),('module 4'))
    nest3_keyboard.row(('module  5'),('module 2'))
    nest3_keyboard.row(('Back'),('Main menu'))
    bot.send_message(message.chat.id, 'H.', reply_markup=nest3_keyboard)
    user_states[message.chat.id] = "subject3_note_button_selected"

# @bot.message_handler(func=lambda message: message.text == "module 1")
# def s1_cse_subject3_Module1_selected(message):
#    #pdf_url = '#' 
#    #bot.send.document(message.chat.id,#pdf_url)
# @bot.message_handler(func=lambda message: message.text == "module 2")
# def s1_cse_subject3_Module2_selected(message):
#    #pdf_url = '#' 
#    #bot.send.document(message.chat.id,#pdf_url)
# @bot.message_handler(func=lambda message: message.text == "module 3")
# def s1_cse_subject1_Module3_selected(message):
#    #pdf_url = '#' 
#    #bot.send.document(message.chat.id,#pdf_url)
# @bot.message_handler(func=lambda message: message.text == "module 4")
# def s1_cse_subject3_Module4_selected(message):
#    #pdf_url = '#' 
#    #bot.send_document(message.chat.id,#pdf_url)

# @bot.message_handler(func=lambda message: message.text == "module 5")
# def s1_cse_subject3_Module5_selected(message):
#    #pdf_url = '#' 
#     #bot.send.document(message.chat.id,#pdf_url)

# # from here start syullbus for s1 m1 
# @bot.message_handler(func=lambda message: message.text == "syullbus")
# def s1_cse_subject3_Syullbus_selected(message):

#    #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)


# @bot.message_handler(func=lambda message: message.text == "textbook")
# def s1_cse_subject3_textbook_selected(message):

#     #photo_url = '#' 
#     #bot.send_photo(message.chat.id, photo_url)


@bot.message_handler(func=lambda message: message.text == "Question paper & solved Question paper")
def s1_cse_subject3_Qp_selected(message):
  nest4_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
  nest4_keyboard.row(("2022"))
  nest4_keyboard.row(('2021'))
  nest4_keyboard.row(("2019"))
  nest4_keyboard.row(('2019'))
  nest4_keyboard.row(('back'),('Menu menu'))
  bot.send.message(message.chat.id,'',reply_markup=nest4_keyboard)
  user_states[message.chat.id] = "s1_cse_subject3_Qp_selected"

# @bot.message_handler(func=lambda message: message.text == "2022")
# def s1_cse_subject3_Qp2022_selected(message):
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
# @bot.message_handler(func=lambda message: message.text == ('2021'))
# def s1_cse_subject3_Qp2021_selected(message):
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
# @bot.message_handler(func=lambda message: message.text == "2020")
# def s1_cse_subject3_Qp2020_selected(message):
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
# @bot.message_handler(func=lambda message: message.text == "2019")
# def s1_cse_subject3_Qp2019_selected(message):
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
# @bot.message_handler(func=lambda message: message.text == "Importent topics")
# def s1_cse_subject3_Imp_selected(message):
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)

#......................subject 4..........................................................................

@bot.message_handler(func=lambda message: message.text == "subject 4")
def s1_cse_subject4_button_selected(message):
    nest2_keyboard = ReplyKeyboardMarkup(resize_keyboard=True) 
    nest2_keyboard.row(('Note'))
    nest2_keyboard.row(('Syullbus'))
    #nest2_keyboard.row(('Textbook '))
    nest2_keyboard.row(('Question paper & solved Question paper'))
    #nest2_keyboard.row(('importent topics '))
    nest2_keyboard.row(('contribute'))
    nest2_keyboard.row(('Back'),('Main menu'))
    bot.send_message(message.chat.id, 'H.', reply_markup=nest2_keyboard)
    user_states[message.chat.id] = "s1_cse_subject4_button_selected"

@bot.message_handler(func=lambda message: message.text == "Note")
def subject4_note_button_selected(message):
    nest3_keyboard = ReplyKeyboardMarkup(resize_keyboard=True) 
    nest3_keyboard.row(('module  1'),('module 2'))
    nest3_keyboard.row(('module  3'),('module 4'))
    nest3_keyboard.row(('module  5'),('module 2'))
    nest3_keyboard.row(('Back'),('main menu'),)
    bot.send_message(message.chat.id, 'H.', reply_markup=nest3_keyboard)
    user_states[message.chat.id] = "subject4_note_button_selected"

# @bot.message_handler(func=lambda message: message.text == "module 1")
# def s1_cse_subject4_Module1_selected(message):
#    #pdf_url = '#' 
#    #bot.send.document(message.chat.id,#pdf_url)
# @bot.message_handler(func=lambda message: message.text == "module 2")
# def s1_cse_subject4_Module2_selected(message):
#    #pdf_url = '#' 
#    #bot.send.document(message.chat.id,#pdf_url)
# @bot.message_handler(func=lambda message: message.text == "module 3")
# def s1_cse_subject1_Module3_selected(message):
#    #pdf_url = '#' 
#    #bot.send.document(message.chat.id,#pdf_url)
# @bot.message_handler(func=lambda message: message.text == "module 4")
# def s1_cse_subject4_Module4_selected(message):
#    #pdf_url = '#' 
#    #bot.send_document(message.chat.id,#pdf_url)

# @bot.message_handler(func=lambda message: message.text == "module 5")
# def s1_cse_subject4_Module5_selected(message):
#    #pdf_url = '#' 
#     #bot.send.document(message.chat.id,#pdf_url)

# # from here start syullbus for s1 m1 
# @bot.message_handler(func=lambda message: message.text == "syullbus")
# def s1_cse_subject4_Syullbus_selected(message):

#    #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)


# @bot.message_handler(func=lambda message: message.text == "textbook")
# def s1_cse_subject4_textbook_selected(message):

#     #photo_url = '#' 
#     #bot.send_photo(message.chat.id, photo_url)


@bot.message_handler(func=lambda message: message.text == "Question paper & solved Question paper")
def s1_cse_subject4_Qp_selected(message):
  nest4_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
  nest4_keyboard.row(("2022"))
  nest4_keyboard.row(('2021'))
  nest4_keyboard.row(("2019"))
  nest4_keyboard.row(('2019'))
  nest4_keyboard.row(('back'),('Menu menu'))
  bot.send.message(message.chat.id,'',reply_markup=nest4_keyboard)
  user_states[message.chat.id] = "s1_cse_subject4_Qp_selected"

# @bot.message_handler(func=lambda message: message.text == "2022")
# def s1_cse_subject4_Qp2022_selected(message):
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
# @bot.message_handler(func=lambda message: message.text == ('2021'))
# def s1_cse_subject4_Qp2021_selected(message):
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
# @bot.message_handler(func=lambda message: message.text == "2020")
# def s1_cse_subject4_Qp2020_selected(message):
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
# @bot.message_handler(func=lambda message: message.text == "2019")
# def s1_cse_subject4_Qp2019_selected(message):
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
# @bot.message_handler(func=lambda message: message.text == "Importent topics")
# def s1_cse_subject4_Imp_selected(message):
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)

#....................subject 5......................................................

@bot.message_handler(func=lambda message: message.text == "subject 5")
def s1_cse_subject5_button_selected(message):
    nest2_keyboard = ReplyKeyboardMarkup(resize_keyboard=True) 
    nest2_keyboard.row(('Note'))
    nest2_keyboard.row(('Syullbus'))
    nest2_keyboard.row(('Textbook '))
    nest2_keyboard.row(('Question paper'))
    nest2_keyboard.row(('Solved Question paper'))
    nest2_keyboard.row(('importent topics '))
    nest2_keyboard.row(('contribute'))
    nest2_keyboard.row(('Back'),('Main menu'))
    bot.send_message(message.chat.id, 'H.', reply_markup=nest2_keyboard)
    user_states[message.chat.id] = "s1_cse_subject5_button_selected"

@bot.message_handler(func=lambda message: message.text == "Note")
def subject5_note_button_selected(message):
    nest3_keyboard = ReplyKeyboardMarkup(resize_keyboard=True) 
    nest3_keyboard.row(('module  1'),('module 2'))
    nest3_keyboard.row(('module  3'),('module 4'))
    nest3_keyboard.row(('module  5'),('module 2'))
    nest3_keyboard.row(('Back'),('Main menu'))
    bot.send_message(message.chat.id, 'H.', reply_markup=nest3_keyboard)
    user_states[message.chat.id] = "subject5_note_button_selected"

# @bot.message_handler(func=lambda message: message.text == "module 1")
# def s1_cse_subject5_Module1_selected(message):
#    #pdf_url = '#' 
#    #bot.send.document(message.chat.id,#pdf_url)
# @bot.message_handler(func=lambda message: message.text == "module 2")
# def s1_cse_subject5_Module2_selected(message):
#    #pdf_url = '#' 
#    #bot.send.document(message.chat.id,#pdf_url)
# @bot.message_handler(func=lambda message: message.text == "module 3")
# def s1_cse_subject1_Module3_selected(message):
#    #pdf_url = '#' 
#    #bot.send.document(message.chat.id,#pdf_url)
# @bot.message_handler(func=lambda message: message.text == "module 4")
# def s1_cse_subject5_Module4_selected(message):
#    #pdf_url = '#' 
#    #bot.send_document(message.chat.id,#pdf_url)

# @bot.message_handler(func=lambda message: message.text == "module 5")
# def s1_cse_subject5_Module5_selected(message):
#    #pdf_url = '#' 
#     #bot.send.document(message.chat.id,#pdf_url)

# # from here start syullbus for s1 m1 
# @bot.message_handler(func=lambda message: message.text == "syullbus")
# def s1_cse_subject5_Syullbus_selected(message):

#    #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)


# @bot.message_handler(func=lambda message: message.text == "textbook")
# def s1_cse_subject5_textbook_selected(message):

#     #photo_url = '#' 
#     #bot.send_photo(message.chat.id, photo_url)


@bot.message_handler(func=lambda message: message.text == "Question paper & solved Question paper")
def s1_cse_subject5_Qp_selected(message):
  nest4_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
  nest4_keyboard.row(("2022"))
  nest4_keyboard.row(('2021'))
  nest4_keyboard.row(("2019"))
  nest4_keyboard.row(('2019'))
  nest4_keyboard.row(('back'),('Menu menu'))
  bot.send.message(message.chat.id,'',reply_markup=nest4_keyboard)
  user_states[message.chat.id] = "s1_cse_subject5_Qp_selected"

# @bot.message_handler(func=lambda message: message.text == "2022")
# def s1_cse_subject5_Qp2022_selected(message):
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
# @bot.message_handler(func=lambda message: message.text == ('2021'))
# def s1_cse_subject5_Qp2021_selected(message):
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
# @bot.message_handler(func=lambda message: message.text == "2020")
# def s1_cse_subject5_Qp2020_selected(message):
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
# @bot.message_handler(func=lambda message: message.text == "2019")
# def s1_cse_subject5_Qp2019_selected(message):
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
# @bot.message_handler(func=lambda message: message.text == "Importent topics")
# def s1_cse_subject5_Imp_selected(message):
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)

#....................subject 6......................................................

@bot.message_handler(func=lambda message: message.text == "subject 6")
def s1_cse_subject6_button_selected(message):
    nest2_keyboard = ReplyKeyboardMarkup(resize_keyboard=True) 
    nest2_keyboard.row(('Note'))
    nest2_keyboard.row(('Syullbus'))
    nest2_keyboard.row(('Textbook '))
    nest2_keyboard.row(('Question paper'))
    nest2_keyboard.row(('Solved Question paper'))
    nest2_keyboard.row(('importent topics '))
    nest2_keyboard.row(('contribute'))
    nest2_keyboard.row(('Back'),('Main menu'))
    bot.send_message(message.chat.id, 'H.', reply_markup=nest2_keyboard)
    user_states[message.chat.id] = "s1_cse_subject6_button_selected"

@bot.message_handler(func=lambda message: message.text == "Note")
def subject6_note_button_selected(message):
    nest3_keyboard = ReplyKeyboardMarkup(resize_keyboard=True) 
    nest3_keyboard.row(('module  1'),('module 2'))
    nest3_keyboard.row(('module  3'),('module 4'))
    nest3_keyboard.row(('module  5'),('module 2'))
    nest3_keyboard.row(('Back'),('Main menu'))
    bot.send_message(message.chat.id, 'H.', reply_markup=nest3_keyboard)
    user_states[message.chat.id] = "subject6_note_button_selected"

# @bot.message_handler(func=lambda message: message.text == "module 1")
# def s1_cse_subject6_Module1_selected(message):
#    #pdf_url = '#' 
#    #bot.send.document(message.chat.id,#pdf_url)
# @bot.message_handler(func=lambda message: message.text == "module 2")
# def s1_cse_subject6_Module2_selected(message):
#    #pdf_url = '#' 
#    #bot.send.document(message.chat.id,#pdf_url)
# @bot.message_handler(func=lambda message: message.text == "module 3")
# def s1_cse_subject1_Module3_selected(message):
#    #pdf_url = '#' 
#    #bot.send.document(message.chat.id,#pdf_url)
# @bot.message_handler(func=lambda message: message.text == "module 4")
# def s1_cse_subject6_Module4_selected(message):
#    #pdf_url = '#' 
#    #bot.send_document(message.chat.id,#pdf_url)

# @bot.message_handler(func=lambda message: message.text == "module 5")
# def s1_cse_subject6_Module5_selected(message):
#    #pdf_url = '#' 
#     #bot.send.document(message.chat.id,#pdf_url)

# # from here start syullbus for s1 m1 
# @bot.message_handler(func=lambda message: message.text == "syullbus")
# def s1_cse_subject6_Syullbus_selected(message):

#    #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)


# @bot.message_handler(func=lambda message: message.text == "textbook")
# def s1_cse_subject6_textbook_selected(message):

#     #photo_url = '#' 
#     #bot.send_photo(message.chat.id, photo_url)


@bot.message_handler(func=lambda message: message.text == "Question paper & solved Question paper")
def s1_cse_subject6_Qp_selected(message):
  nest4_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
  nest4_keyboard.row(("2022"))
  nest4_keyboard.row(('2021'))
  nest4_keyboard.row(("2019"))
  nest4_keyboard.row(('2019'))
  nest4_keyboard.row(('back'),('Menu menu'))
  bot.send.message(message.chat.id,'',reply_markup=nest4_keyboard)
  user_states[message.chat.id] = "s1_cse_subject6_Qp_selected"

# @bot.message_handler(func=lambda message: message.text == "2022")
# def s1_cse_subject6_Qp2022_selected(message):
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
# @bot.message_handler(func=lambda message: message.text == ('2021'))
# def s1_cse_subject6_Qp2021_selected(message):
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
# @bot.message_handler(func=lambda message: message.text == "2020")
# def s1_cse_subject6_Qp2020_selected(message):
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
# @bot.message_handler(func=lambda message: message.text == "2019")
# def s1_cse_subject6_Qp2019_selected(message):
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
# @bot.message_handler(func=lambda message: message.text == "Importent topics")
# def s1_cse_subject6_Imp_selected(message):
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)
#....................Lab..................................................
@bot.message_handler(func=lambda message: message.text == "Lab 1")
def s1_cse_Lab1_button_selected(message):
    nest21_keyboard = ReplyKeyboardMarkup(resize_keyboard=True) 
    nest21_keyboard.row(('Lab manual'))
    nest21_keyboard.row(('Viva Questions'))
    nest21_keyboard.row(('Practical Record'))
    nest21_keyboard.row(('contribute'))
    nest21_keyboard.row(('Back'),('Main menu'))
    bot.send_message(message.chat.id, 'H.', reply_markup=nest21_keyboard)
    user_states[message.chat.id] = "s1_cse_Lab1_button_selected"

# # @bot.message_handler(func=lambda message: message.text == "Lab manual")
# # def s1_cse_Lab1_Labmanual_selected(message):
# #     #pdf_url = '#' 
# #     #bot.send_photo(message.chat.id,#pdf_url)

# # @bot.message_handler(func=lambda message: message.text == "Viva Questions")
# # def s1_cse_Lab1_vivaQuestion_selected(message):
# #     #pdf_url = '#' 
# #     #bot.send_photo(message.chat.id,#pdf_url)

# # @bot.message_handler(func=lambda message: message.text == "Practical Record")
# # def s1_cse_Lab1_PracticalRecord_selected(message):
# #     #pdf_url = '#' 
# #     #bot.send_photo(message.chat.id,#pdf_url

#................Lab 2...............................
@bot.message_handler(func=lambda message: message.text == "Lab 2")
def s1_cse_lab2_button_selected(message):
    nest21_keyboard = ReplyKeyboardMarkup(resize_keyboard=True) 
    nest21_keyboard.row(('Lab manual'))
    nest21_keyboard.row(('Viva Questions'))
    nest21_keyboard.row(('Practical Record'))
    nest21_keyboard.row(('contribute'))
    nest21_keyboard.row(('Back'),('Main menu'),('category_selected'))
    bot.send_message(message.chat.id, 'H.', reply_markup=nest21_keyboard)
    user_states[message.chat.id] = "s1_cse_lab2_button_selected"

# @bot.message_handler(func=lambda message: message.text == "Lab manual")
# def s1_cse_lab2_Labmanual_selected(message):
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)

# @bot.message_handler(func=lambda message: message.text == "Viva Questions")
# def s1_cse_lab2_vivaQuestion_selected(message):
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url)

# @bot.message_handler(func=lambda message: message.text == "Practical Record")
# def s1_cse_lab2_PracticalRecord_selected(message):
#     #pdf_url = '#' 
#     #bot.send_photo(message.chat.id,#pdf_url
# #.............................................................
@bot.message_handler(func=lambda message: message.text == "Back")
def Back_pressed(message):
    # Get the user's current state
    current_state = user_states.get(message.chat.id)

    # Check the current state and send the user back to the appropriate menu
    if current_state == "s1_cse_button_selected":
        start(message)
    elif current_state == "s1_cse_subject1_button_selected":
        s1_cse_button_selected(message)
    elif current_state == "s1_cse_subject2_button_selected":
        s1_cse_button_selected(message)
    elif current_state == "s1_cse_subject3_button_selected":
        s1_cse_button_selected(message)
    elif current_state == "s1_cse_subject4_button_selected":
        s1_cse_button_selected(message)
    elif current_state == "s1_cse_subject5_button_selected":
        s1_cse_button_selected(message)
    elif current_state == "s1_cse_subject6_button_selected":
        s1_cse_button_selected(message)
        #-----------------------------------
    elif current_state == " s1_cse_lab2_button_selected":
        s1_cse_button_selected(message)
    elif current_state == " s1_cse_lab2_button_selected":
        s1_cse_button_selected(message)
        #-----------------------------------------------
    elif current_state == "s1_cse_subject1_note_button_selected":
        s1_cse_subject1_button_selected(message)
    elif current_state == "s1_cse_subject2_button_selected":
      s1_cse_subject2_button_selected(message)
    elif current_state == "s1_cse_subject3_note_button_selected":
        s1_cse_subject3_button_selected(message)
    elif current_state == "s1_cse_subject4_button_selected":
      s1_cse_subject4_button_selected(message)
    elif current_state == "s1_cse_subject5_note_button_selected":
        s1_cse_subject5_button_selected(message)
    elif current_state == "s1_cse_subject6_note_button_selected":
        s1_cse_subject6_button_selected(message)
        #---------------------------------------
    elif current_state == "s1_cse_subject1_Qp_selected":
        s1_cse_subject1_button_selected(message)
    elif current_state == "s1_cse_subject2_Qp_selected":
      s1_cse_subject2_button_selected(message)
    elif current_state == "s1_cse_subject3_Qp_selected":
        s1_cse_subject3_button_selected(message)
    elif current_state == "s1_cse_subject4_Qp_selected":
      s1_cse_subject4_button_selected(message)
    elif current_state == "s1_cse_subject5_Qp_selected":
        s1_cse_subject5_button_selected(message)
    elif current_state == "s1_cse_subject6_Qp_selected":
        s1_cse_subject6_button_selected(message)
    
    
    

bot.polling()
