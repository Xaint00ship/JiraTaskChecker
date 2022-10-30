from jira import JIRA

class ApiJiraCheckTask():

    def __init__(self,login,password):
        self.login = login
        self.password = password


    def _authorization(self):
        jira_options = {'': ''}
        jira = JIRA(options=jira_options, basic_auth=(self.login, self.password))
        return jira


    def checkTask(self):
        tasksResolved = self._authorization().search_issues('project = SERVICE AND status in (Ожидание, Эскалирован, Возвращена)')
        myTaskResponseRes = self._authorization().search_issues('project = SERVICE AND issuetype in ("Запрос на изменение (SD2)", "Запрос на обслуживание", "Запрос на обслуживание (SD2)", "Инцидент (SD2)") AND status in (Ожидание, "Ответ принят", Возвращена) AND assignee in (currentUser()) ORDER BY "Time to resolution" ASC')
        return([tasksResolved,myTaskResponseRes])



