import telebot

class SendMessage():
    
    def __init__(self,tasks):
        self.tasks = tasks        
        self.bot = telebot.TeleBot('токен')

    def messageAboutMyTasks(self):
        message = "Появились задачи: \n"
        for taskMe in self.tasks:
            message = message + str(taskMe) + "\n"

        self.bot.send_message(0000000, message)
    
    

