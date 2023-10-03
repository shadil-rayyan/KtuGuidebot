import telebot
from telebot.types import BotDescription,nest1_keyboardButton, ReplyKeyboardMarkup
bot = telebot.TeleBot('6217202010:AAG0nYaNj_JX2t79t1ns_fgUo_buHeYF2Ts')
user_states = {}

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(('Annocement'))
    keyboard.row(('Departement'))
    keyboard.row(('Academic calender'))
    keyboard.row(('KTU credit calculator'))
    keyboard.row(('Scholorship'))
    keyboard.row(('Whatsapp'),('contribute'))
    keyboard.row(('Contact us'))
    keyboard.row(('other bots'))
    bot.send_message(message.chat.id, '', reply_markup=keyboard)
@bot.message_handler(func=lambda message: message.text == "Annocement")
def Annocement_selected(message):
    bot.send_message(message.chat.id, 'coming soon')
    
@bot.message_handler(func=lambda message: message.text == "Departement")
def Departement_selected(message):
    nest1_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    nest1_keyboard.row(('CSE'), ('ECE'))
    nest1_keyboard.row(('EEE'), ('IT'))
    nest1_keyboard.row(('CIVIL'), ('MECH'))
    bot.send_message(message.chat.id, '', reply_markup=nest1_keyboard)

#@bot.message_handler(func=lambda message: message.text == "CSE")

@bot.message_handler(func=lambda message: message.text == "CSE")
def back_button_clicked(message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(('S1'), ('S2'))
    keyboard.row(('S3'), ('S4'))
    keyboard.row(('S5'), ('S6'))
    keyboard.row(('S7'), ('S8'))
    keyboard.row(('contribute'))
    keyboard.row(('Whatsapp channel'))
    bot.send_message(message.chat.id, 'Welcome to my bot!', reply_markup=keyboard)

 #user_states[message.chat.id] = "main_menu"

@bot.message_handler(func=lambda message: message.text == "Back")
def back_button_clicked(message):
    chat_id = message.chat.id
    
    if chat_id in user_states:
        current_state = user_states[chat_id]
        
        if current_state == "category_selected":
           
            start(message)
        
    
        user_states[chat_id] = current_state

@bot.message_handler(func=lambda message: message.text == "Main Menu")
def main_menu_button_clicked(message):
    # Handle the "Main Menu" button click by sending the main menu again
    start(message)

#from here start s1 for CSE
@bot.message_handler(func=lambda message: message.text == "S1")
def S1_button_selected(message):
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

# from here start subject for S1M1

@bot.message_handler(func=lambda message: message.text == "subject 1")
def subject1_button_selected(message):
   nest2_keyboard = ReplyKeyboardMarkup(resize_keyboard=True) 

   nest2_keyboard.row(('Note'))
   nest2_keyboard.row(('Syullbus'))
   nest2_keyboard.row(('Textbook '))
   nest2_keyboard.row(('Question paper'))
   nest2_keyboard.row(('Solved Question paper'))
   nest2_keyboard.row(('contribute'))
   nest2_keyboard.row(('back_button'),('main_menu_button'),('category_selected'))
    bot.send_message(message.chat.id, 'H.', reply_markup=nest2_keyboard)

    
    #user_states[message.chat.id] = "category_selected"

@bot.message_handler(func=lambda message: message.text == "Note")
def note_button_selected(message):
  nest3_keyboard = ReplyKeyboardMarkup(resize_keyboard=True) 
  nest3_keyboard.row(('module  1'),('module 2'))
  nest3_keyboard.row(('module  3'),('module 4'))
  nest3_keyboard.row(('module  5'),('module 2'))
  nest3_keyboard.row(('back_button'),('main_menu_button'),('category_selected'))
    bot.send_message(message.chat.id, 'H.', reply_markup=nest3_keyboard)

@bot.message_handler(func=lambda message: message.text == "module 1")
def s1Module1_selected(message):
   #pdf_url = '#' 
    #bot.send.document(message.chat.id,#pdf_url)
@bot.message_handler(func=lambda message: message.text == "module 2")
def s1Module1_selected(message):
   #pdf_url = '#' 
    #bot.send.document(message.chat.id,#pdf_url)
@bot.message_handler(func=lambda message: message.text == "module 3")
def s1Module1_selected(message):
   #pdf_url = '#' 
    #bot.send.document(message.chat.id,#pdf_url)
@bot.message_handler(func=lambda message: message.text == "module 4")
def s1Module1_selected(message):
   #pdf_url = '#' 
    #bot.send_document(message.chat.id,#pdf_url)

@bot.message_handler(func=lambda message: message.text == "module 5")
def s1m5_selected(message):
   #pdf_url = '#' 
    #bot.send.document(message.chat.id,#pdf_url)

# from here start syullbus for S1 m1 
@bot.message_handler(func=lambda message: message.text == "syullbus")
def s1cse_Syullbus_selected(message):

   #pdf_url = '#' 
    #bot.send_photo(message.chat.id,#pdf_url)


@bot.message_handler(func=lambda message: message.text == "textbook")
def s1cse_textbook_selected(message):

    #photo_url = '#' 
    #bot.send_photo(message.chat.id, photo_url)


@bot.message_handler(func=lambda message: message.text == "Question paper")
def s1cse_Qp_selected(message):
   #pdf_url = '#' 
#bot.send.document(message.chat.id,#pdf_url)



@bot.message_handler(func=lambda message: message.text == "Solved QP")
def s1cse_SQp_selected(message):

    bot.send_message(message.chat.id, '2022')
   #pdf_url = '#' 
    #bot.send.document(message.chat.id,#pdf_url)

@bot.message_handler(func=lambda message: message.text == "lab")
def s1cse_lab_selected(message):

   nest4_keyboard = ReplyKeyboardMarkup(resize_keyboard=True) 

   nest4_keyboard.row(('Lab 1'))
   nest4_keyboard.row(('Lab 2'))
   bot.send_message(message.chat.id, 'H.', reply_markup=nest4_keyboard)


@bot.message_handler(func=lambda message: message.text == "lab 1")
def s1cse_lab_selected(message):
  nest5_keyboard = ReplyKeyboardMarkup(resize_keyboard=True) 
   nest5_keyboard.row(('Lab manual'))
   nest5_keyboard.row(('viva question'))
   bot.send_message(message.chat.id, 'H.', reply_markup=nest5_keyboard)

@bot.message_handler(func=lambda message: message.text == "lab maual")
def labmanual_selected(message):

@bot.message_handler(func=lambda message: message.text == "viva question")
def vivaQuestion_selected(message):

# from here academic calender starts
@bot.message_handler(func=lambda message: message.text == "Academic calender")
def Academic_selected(message):
     bot.send_message(message.chat.id, 'coming soon')

@bot.message_handler(func=lambda message: message.text == "KTU credit calculator'")
def ktucredit_selected(message):
     bot.send_message(message.chat.id, 'coming soon')

@bot.message_handler(func=lambda message: message.text == "Scholorship")
def Scholorship_selected(message):
     bot.send_message(message.chat.id, 'coming soon')

@bot.message_handler(func=lambda message: message.text == "contribute")
def contribute_selected(message):
     bot.send_message(message.chat.id, 'coming soon')

@bot.message_handler(func=lambda message: message.text == "Whatsapp")
def whatsapp_selected(message):
     bot.send_message(message.chat.id, 'coming soon')

@bot.message_handler(func=lambda message: message.text == "Other bots")
def otherbot_selected(message):
     bot.send_message(message.chat.id, 'coming soon')

