from appJar import gui 
from model.ConfiguracoesDeCriacao import ConfiguracoesDeCriacao
from model.Agente import Agente


configuracoesDeCriacao = ConfiguracoesDeCriacao()

def press(btn):
    configuracoesDeCriacao.estadoAtual =btn[8]
    app.startSubWindow("one", modal=True)
    app.addLabel("l1", "O que o Agente Fez:")
    app.addButton("Fechar popUp",fecharPopUp)

    agente = Agente(int(btn[8]))
    caminho = agente.maquinaDeMealy.realizarCaminho()
    i=0
    for acao in caminho:
        app.addLabel("lx"+str(acao["estado"]),acao["acao"])
        app.addImage("ep"+str(acao["estado"]),"imagens/e"+str(acao["estado"])+".gif")

    app.addLabel("lpfim","FIM")
    app.stopSubWindow()
    app.showSubWindow("one")


def fecharPopUp(btn):
     app.destroySubWindow("one")


app=gui("FRAME DEMO", "fullscreen")
app.setBg("white")
app.addLabel("aa", "Escolha o Estado Inicial",0,0,colspan=4)
app.getLabelWidget("aa").config(bg="white")
for i in range(0, 4):
    app.startLabelFrame("estado"+str(i+1), row=1, column=i)
    app.addImage("e"+str(i+1), "imagens/e"+str(i+1)+".gif")
    app.addButton("escolher"+str(i+1),press)

    app.stopLabelFrame()
    

for i in range(4, 8):
    app.startLabelFrame("estado"+str(i+1), row=2, column=i-4)
    app.addImage("e"+str(i+1),"imagens/e"+str(i+1)+".gif")
    app.addButton("escolher"+str(i+1),press)
    app.stopLabelFrame()
app.go()