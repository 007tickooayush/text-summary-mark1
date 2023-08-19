from summarizer import Summarizer

class Summary:
    def __init__(self):
        self._bert_model = Summarizer()
        self._content = ''
        self._summary = ''
        self._min_length = None

    # def __init__(self,content,summary,min_length):
    #     self._bert_model = Summarizer()
    #     self._content = content
    #     self._summary = summary
    #     self._min_length = min_length

    def create__summary(self,content='',min_length=None):
        if self._content == '':
            self._summary = ''.join(self._bert_model(content,min_length=min_length))
        else:
            self._summary = ''.join(self._bert_model(self._content,min_length=min_length))

        return self._summary