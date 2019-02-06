

#-----------------------------------------------------------------------------------------------
class DialogTreeClass(object):
    def __init__(self, npc, idnum, text):
        self.npc=npc
        self.idnum=idnum
        self.text=text
        self.responses=[]

#-----------------------------------------------------------------------------------------------
class DialogClass(object):
    """docstring for DialogClass"""
    def __init__(self,filename='dialog_test.txt'):
        self.dialog_tree=[]
        self.load_dialog_file(filename)

    #-----------------------------------------------------------------------------------------------
    def load_dialog_file(self,filename):
        with open(filename) as file:
            data=file.read().split('\n')
        for row in data:
            if row[0]=='#' or len(row)==0:
                continue
            row=row.split('~')
            dlg=DialogTreeClass(int(row[0]), int(row[1]), row[2])
            p=3
            response=[]
            while True:
                try:
                    response.append((row[p],int(row[p+1])))
                    p+=2
                except:
                    break
            dlg.responses=response
            self.dialog_tree.append(dlg)
        print('load_dialog_file: {} lines loaded'.format(len(self.dialog_tree)))

    #-----------------------------------------------------------------------------------------------
    def print_dialog(self, npc=1):
        print('Dialog list:')
        for dlg in self.dialog_tree:
            if dlg.npc==npc:
                print('NPC:{:2}  ID:{:3}\n{}'.format(dlg.npc,  dlg.idnum, dlg.text))
                for response in dlg.responses:
                    print('      {:3} {}'.format(response[1], response[0]))

   #-----------------------------------------------------------------------------------------------
    def get_dialog(self, npc, idnum):
        for dialog in self.dialog_tree:
            if dialog.npc==npc and dialog.idnum==idnum:
                return dialog
        return False

    #-----------------------------------------------------------------------------------------------
    def talk_to(self, npc, question=100):
        #self.print_dialog()
        dialog=self.get_dialog(npc,question)
        if dialog:
            print('{}'.format(dialog.text))
            return dialog.responses
        print('talk_to: cant find {}, {}'.format(npc,question))
        return False

#-----------------------------------------------------------------------------------------------
if __name__ == '__main__':
    dialog=DialogClass()
    npc=2
    converse=dialog.talk_to(npc)
    while converse:
        for i, response in enumerate(converse):
            print('{:2} - {}'.format(i,response[0]))
        choice=input()
        #should error trap for correct choice
        if choice=='x' or converse[int(choice)][1]==999:
            converse=dialog.talk_to(npc, converse[int(choice)][1])
            print(response[0])
            break
        converse=dialog.talk_to(npc, converse[int(choice)][1])


