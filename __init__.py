from mycroft import MycroftSkill, intent_file_handler


class TerminalGo(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('go.terminal.intent')
    def handle_go_terminal(self, message):
        self.speak_dialog('go.terminal')


def create_skill():
    return TerminalGo()

