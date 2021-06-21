from dataclasses import dataclass

@dataclass
class FileDTO(object):

    context: str  #외부에서 주입되는 값들은 전부 게터, 세터로 만듦
    fname: str
    url: str
    dframe: object

    @property
    def context(self) -> str:
        return self._context

    @context.setter
    def context(self, context):
        self._context = context

    @property
    def fname(self) -> str:
        return self._fname

    @fname.setter
    def fname(self, fname):
        self._fname = fname

    @property
    def dframe(self) -> object:
        return self._dframe

    @dframe.setter
    def dframe(self, dframe):
        self._dframe = dframe

    @property
    def url(self) -> str:
        return self._url

    @url.setter
    def url(self, url):
        self._url = url