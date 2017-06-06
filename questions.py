import sys

class Question:
    def __init__(self, question_text):
        self.question_text = question_text
        self.entity_to_response_dict = {}
        self.answered = False

    def set_yes_response(self, isAnswered, text = None, func = None):
        if text is not None and func is not None:
            print('provide either a function or text')
            sys.exit(1)

        if text is not None:
            self.yes = (text.encode('ascii', 'xmlcharrefreplace'), isAnswered)

        if func is not None:
            self.yes = (func, isAnswered)

        return self

    def set_no_response(self, isAnswered, text = None, func = None):
        if text is not None and func is not None:
            print('provide either a function or text')
            sys.exit(1)

        if text is not None:
            self.no = (text.encode('ascii', 'xmlcharrefreplace'), isAnswered)

        if func is not None:
            self.no = (func, isAnswered)

        return self

    def add_valid_entity_response(self, entity, response):
        self.entity_to_response_dict[entity] = response
        return self

    def add_invalid_entity_response(self, response):
        self.invalid_response = response
        return self

    def add_default_response(self, response):
        self.default_response = response
        return self