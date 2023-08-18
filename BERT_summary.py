from summarizer import Summarizer

class Summary:
    def __init__(self):
        self._bert_model = Summarizer()
        self._content = ''
        self._summary = ''

    def __init__(self,content,summary):
        self._bert_model = Summarizer()
        self._content = content
        self._summary = summary

    def create__summary(self,content='',min_length=None,):
        if self._content == '':
            self._summary = ''.join(self._bert_model(content,min_length=min_length))
        else:
            self._summary = ''.join(self._bert_model(self._content,min_length=min_length))

        return self._summary