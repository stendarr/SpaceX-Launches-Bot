class strHTML(str):
    def addURL(self, url):
        return "<a href='"+url+"'>"+self+"</a>"
    def makeBold(self):
        return "<strong>" + self + "</strong>"
    def makeItalic(self):
        return "<i>" + self + "</i>"
