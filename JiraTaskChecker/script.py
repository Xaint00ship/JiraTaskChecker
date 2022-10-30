from asyncio import tasks
import tgAnnunciator
import jiraApi
import time


class Collector():
    def __init__(self,delayBetweenRepeat):
        self.delayBetweenRepeat = delayBetweenRepeat
        self.tasks = jiraApi.ApiJiraCheckTask('логин', 'пароль')
    
        self.stockTasksForMe = self.tasks.checkTask()[1]
        #print(self.tasks.checkTask())
        self.stockTasksStack = self.tasks.checkTask()[0]
        #print(self.stockTasksStack[0])
    def start(self):
        while True:

            if len(self.tasks.checkTask()[1]) != 0:
                
                tgAnnunciator.SendMessage(self.tasks.checkTask()[1]).messageAboutMyTasks()
                self.stockTasksForMe = self.tasks.checkTask()[1]

            if len(self.tasks.checkTask()[0]) != 0:
                if self.tasks.checkTask()[0][0] != self.stockTasksStack[0] and len(self.tasks.checkTask()[0]) >= len(self.stockTasksStack):
                    tgAnnunciator.SendMessage(self.tasks.checkTask()[0]).messageAboutMyTasks()
                    self.stockTasksStack = self.tasks.checkTask()[0]
                    
            time.sleep(self.delayBetweenRepeat)




test = Collector(10)
test.start()

