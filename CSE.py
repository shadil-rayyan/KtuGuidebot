import telebot
from telebot.types import BotDescription, KeyboardButton, ReplyKeyboardMarkup
bot = telebot.TeleBot('6217202010:AAG0nYaNj_JX2t79t1ns_fgUo_buHeYF2Ts')
user_states = {}
# from here start departement "CSE"
@bot.message_handler(commands=['start'])
def start(message):
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
    nested_keyboard = ReplyKeyboardMarkup(resize_keyboard=True) 
    # Create two separate rows for buttons
    nested_keyboard.row(('subject 1'))
    nested_keyboard.row(('subject 2'))
    nested_keyboard.row(('subject 3 '))
    nested_keyboard.row(('subject 4'))
    nested_keyboard.row(('Lab '))
    nested_keyboard.row(('back_button'),('main_menu_button'))
    nested_keyboard.row(('contribute '))
    nested_keyboard.row(('Whatsapp channel'))

    bot.send_message(message.chat.id, 'Hello! ', reply_markup=nested_keyboard)
    #user_states[message.chat.id] = "category_selected"

# from here start subject for S1M1

@bot.message_handler(func=lambda message: message.text == "subject 1")
def subject1_button_selected(message):
    nested_nest_keyboard = ReplyKeyboardMarkup(resize_keyboard=True) 

    nested_nest_keyboard.row(('Note'))
    nested_nest_keyboard.row(('Syullbus'))
    nested_nest_keyboard.row(('Textbook '))
    nested_nest_keyboard.row(('Question paper'))
    nested_nest_keyboard.row(('Solved Question paper'))
    nested_nest_keyboard.row(('contribute'))
    nested_nest_keyboard.row(('back_button'),('main_menu_button'),('category_selected'))
    bot.send_message(message.chat.id, 'H.', reply_markup=nested_nest_keyboard)

    
    #user_states[message.chat.id] = "category_selected"

@bot.message_handler(func=lambda message: message.text == "Note")
def note_button_selected(message):
    nested_nest2_keyboard = ReplyKeyboardMarkup(resize_keyboard=True) 
    nested_nest2_keyboard.row(('module  1'),('module 2'))
    nested_nest2_keyboard.row(('module  3'),('module 4'))
    nested_nest2_keyboard.row(('module  5'),('module 2'))
    nested_nest2_keyboard.row(('back_button'),('main_menu_button'),('category_selected'))
    bot.send_message(message.chat.id, 'H.', reply_markup=nested_nest2_keyboard)

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

@bot.message_handler(func=lambda message: message.text == "subject 2")
def subject1_button_selected(message):
    nested_nest_keyboard = ReplyKeyboardMarkup(resize_keyboard=True) 

    nested_nest_keyboard.row(('Note'))
    nested_nest_keyboard.row(('Syullbus'))
    nested_nest_keyboard.row(('Textbook '))
    nested_nest_keyboard.row(('Question paper'))
    nested_nest_keyboard.row(('Solved Question paper'))
    nested_nest_keyboard.row(('contribute'))
    nested_nest_keyboard.row(('back_button'),('main_menu_button'),('category_selected'))
    bot.send_message(message.chat.id, 'H.', reply_markup=nested_nest_keyboard)


@bot.message_handler(func=lambda message: message.text == "Syullbus")
def s1csesub2_Syullbus_selected(message):
    #pdf_url = '#' 
    #(message.chat.id,pdf_url)
    
    description = "the shadil am "
    bot.send.message(message.chat.id,description)
    



bot.polling()
