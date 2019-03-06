class MaquinaDeMealy:
    def __init__(self,estadoInicial):
            self.estadoInicial = estadoInicial
            self.grafo={
                       1:{
                           "transicoes":[{
                               "Saida":"Limpar",
                               "ProximoEstado":5
                            },
                            {
                               "Saida":"Direita",
                               "ProximoEstado":2
                            }
                            ],
                           "final":False
                           },
                       2:{
                           "transicoes":[{
                               "Saida":"Limpar",
                               "ProximoEstado":4
                          },
                            {
                               "Saida":"Esquerda",
                               "ProximoEstado":1
                            }
                            ],
                           "final":False
                        },
                        3:{
                           "transicoes":[{
                               "Saida":"Limpar",
                               "ProximoEstado":7
                          },
                            {
                               "Saida":"Direita",
                               "ProximoEstado":4
                            }
                            ],
                           "final":False
                        },
                        4:{
                           "transicoes":[{
                               "Saida":"Esquerda",
                               "ProximoEstado":3
                          }
                            ],
                           "final":False
                        },
                        5:{
                           "transicoes":[{
                               "Saida":"Direita",
                               "ProximoEstado":6
                          }
                            ],
                           "final":False
                        },
                        6:{
                           "transicoes":[{
                               "Saida":"Limpar",
                               "ProximoEstado":8
                          },
                          {
                               "Saida":"Esquerda",
                               "ProximoEstado":5
                          }
                           ],
                           "final":False
                        },

                       7:{
                           "transicoes":[{
                               "Saida":"Direita",
                               "ProximoEstado":8
                          }
                           ],
                           "final":True
                        },

                       8:{
                           "transicoes":[{
                               "Saida":"Esquerda",
                               "ProximoEstado":7
                          }
                           ],
                           "final":True
                        }
                   }
    def funcaoDeTransicao(self,estado):
        return self.grafo[estado]["transicoes"][0]
    
    def isEstadoFinal(self,estado):
        return self.grafo[estado]["final"]


    def realizarCaminho(self):
        estado =self.estadoInicial
        acoesTomadas = [] 
        acoesTomadas.append({"estado":estado,"acao":"Nenhuma"})
        while not self.isEstadoFinal(estado):
            transicao = self.funcaoDeTransicao(estado)
            estado = transicao["ProximoEstado"]
            acoesTomadas.append({"estado":estado,"acao":transicao["Saida"]})

        return acoesTomadas


        

        

        
         




            


    


    

