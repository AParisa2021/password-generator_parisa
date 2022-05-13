import PySimpleGUI as gui;
import random;
#testcomment
class PwGen:
    def __init__(self) -> None:
        gui.theme('Black');
        self.layout = [
            [gui.Text("Anzahl der Zeichen:    "),gui.Input(key="amountInput", size=(10,10))],
            [gui.Text("Generiertes Passwort:"), gui.Input(key="pwOutput")],
            [gui.Button("Passwort generieren", key="genPw"), gui.Button("Beenden", key="quit", auto_size_button=False)]
        ];
        self.window = gui.Window("PWGen", self.layout, size=(600,100), icon="favicon.ico");
        self.charList = self.buildCharList();
        self.guiInit();

    def guiInit(self):
        loop = True;
        while(loop):
            event, values = self.window.read();
            if event == "genPw":
                #failsafe for empty amount input
                if(values["amountInput"] == ""):
                    values["amountInput"] = "10";
                #generate password
                tmp = self.genCode(values["amountInput"], True);
                #output password
                self.window["pwOutput"].update(tmp);
            if event == gui.WINDOW_CLOSED or event == "quit":
                loop = False;
    
    def genCode(self, amount, allowSpecialChars):
        amount = int(amount);
        res = "";
        for i in range(0,amount):
            res += self.charList[random.randint(0,len(self.charList)-1)];
        return res;
    
    def buildCharList(self):
        res = [];
        #numbers
        for i in range(48, 58):
            res.append(chr(i));
        #lower case letters
        for i in range(65, 91):
            res.append(chr(i));
        #upper case letters
        for i in range(97, 123):
            res.append(chr(i));
        return res;
    
t = PwGen();