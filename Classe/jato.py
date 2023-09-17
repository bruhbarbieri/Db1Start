from datetime import datetime

class JatoMilitar1Lugar:
    def __init__(self, modelo, baseAtual):
        self.modelo = modelo
        self.baseAtual = baseAtual
        self.piloto = None
        self.historico = []

    def designar_piloto(self, piloto):
        self.piloto = piloto
        print(f'O piloto {piloto} foi designado para o jato militar.')

    def rebasear_aeronave(self, baseDestino):
        if self.piloto is not None:
            transferencia = (datetime.now(), baseDestino)
            self.historico.append(transferencia)
            print(f'A aeronave foi rebaseada da base {self.baseAtual} para a base {baseDestino}.')
            self.baseAtual = baseDestino
        else:
            print('Não é possível rebasear a aeronave sem um piloto designado.')

    def __str__(self):
        info = f'Jato: {self.modelo}\n'
        info += f'Base inicial: {self.baseAtual}\n'
        info += f'Piloto: {self.piloto}\n'
        info += 'Histórico de transferências:\n'
        for data, base in self.historico:
            info += f'Data/Hora: {data}, Base: {base}\n'
        return info

jato = JatoMilitar1Lugar("F-16", "Base A")
jato.designar_piloto("Sebastião Pereira")
jato.rebasear_aeronave("Base B")
jato.rebasear_aeronave("Base C")

print(jato)

