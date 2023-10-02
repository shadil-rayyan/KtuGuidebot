import telebot
from telebot.types import KeyboardButton, ReplyKeyboardMarkup

bot = telebot.TeleBot('6217202010:AAG0nYaNj_JX2t79t1ns_fgUo_buHeYF2Ts')

# Define a dictionary to keep track of user states
user_states = {}

@bot.message_handler(commands=['start'])
def start(message):
    # Create a custom keyboard with a "Category" button and a "Student" button
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(('S1'), ('S2'))
    keyboard.row(('S3'), ('S4'))
    keyboard.row(('S5'), ('S6'))
    keyboard.row(('S7'), ('S8'))
    #keyboard.row(back_button, main_menu_button)
    bot.send_message(message.chat.id, 'Welcome to my bot!', reply_markup=keyboard)

    # Set the user's initial state to the main menu
    user_states[message.chat.id] = "main_menu"

@bot.message_handler(func=lambda message: message.text == "Back")
def back_button_clicked(message):
    chat_id = message.chat.id
    
    if chat_id in user_states:
        current_state = user_states[chat_id]
        
        # Handle "Back" button based on the user's current state
        if current_state == "category_selected":
            # User was in the "travel brochure" section, go back to the main menu
            start(message)
        # Add more cases for other states as needed
        
        # Update the user's current state
        user_states[chat_id] = current_state

@bot.message_handler(func=lambda message: message.text == "Main Menu")
def main_menu_button_clicked(message):
    # Handle the "Main Menu" button click by sending the main menu again
    start(message)
@bot.message_handler(func=lambda message: message.text == "S1")
def S1_button_selected(message):
    nested_keyboard = ReplyKeyboardMarkup(resize_keyboard=True) 
    # Create two separate rows for buttons
    nested_keyboard.row(('subject 1'))
    nested_keyboard.row(('subject 1'))
    nested_keyboard.row(('subject 1 '))
    #nested_keyboard.row((' '))
    nested_keyboard.row(('back_button'),('main_menu_button'), ('category_selected'))


    # Respond with a message when the user selects the "travel brochure" button and include the nested keyboard
    bot.send_message(message.chat.id, 'Hello! Welcome to the "travel brochure" section.', reply_markup=nested_keyboard)

    # Update the user's current state to reflect the current menu
    #user_states[message.chat.id] = "category_selected"

@bot.message_handler(func=lambda message: message.text == "subject 1")
def subject1_button_selected(message):
    nested_nest_keyboard = ReplyKeyboardMarkup(resize_keyboard=True) 
    # Create two separate rows for buttons
    nested_nest_keyboard.row(('note'))
    nested_nest_keyboard.row(('syullbus'))
    nested_nest_keyboard.row(('Textbook '))
    #nested_keyboard.row((' '))
    nested_nest_keyboard.row(('back_button'),('main_menu_button'),('category_selected'))


    # Respond with a message when the user selects the "travel brochure" button and include the nested keyboard
    bot.send_message(message.chat.id, 'Hello! Welcome to the "travel brochure" section.', reply_markup=nested_nest_keyboard)

    # Update the user's current state to reflect the current menu
    #user_states[message.chat.id] = "category_selected"

bot.polling()