from kivymd.app import MDApp
from kivymd.toast import toast

class mainapp(MDApp):
    def __init__(self, **kwargs):
        super(mainapp, self).__init__(**kwargs)

    def build(self):
        self.root.ids.cal.text='0'
        

    def a(self,number):
        if(number=='clear' or number=='=' or number=='CCC'):
            if(number=='='):
                self.root.ids.cal.text=self.root.ids.ans.text
            if(number=='CCC'):
                self.root.ids.cal.text='0'
                self.root.ids.ans.text='0'
            if(number=='clear'):
                self.root.ids.cal.text=self.root.ids.cal.text[:-1]
        else:
            if(number=='+' or number=='-' or number=='*' or number=='/' or number=='.'):
                self.root.ids.cal.text+=number
            else:
                if(self.root.ids.cal.text=='0'):
                    self.root.ids.cal.text=number
                else:
                    self.root.ids.cal.text+=number
                    try:
                        self.root.ids.ans.text=str(eval(self.root.ids.cal.text))
                    except (SyntaxError,NameError,TypeError,ZeroDivisionError):
                        toast("something went wrong or don't use extra zero and extra symbol")

def main():
    mainapp().run()


if __name__ == '__main__':
    main()