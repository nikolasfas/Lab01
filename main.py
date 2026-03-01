import random
from contextlib import nullcontext


def leggi_file(nome_file):
    with open(nome_file, 'r', encoding='utf-8') as f:
        righe = [r.strip() for r in f.readlines()]

    domande = []
    i=0
    while i< len(righe):
        if i=="":
            i+=1
            continue

        testo = righe[i]
        punti = int(righe[i+1])
        rispCorretta = righe[i+2]
        risposte = righe[i+2:i+6]

        domanda = Domanda(testo, punti, rispCorretta, risposte)
        domande.append(domanda)

        i+=7
    return domande



class Domanda:
    def __init__(self, testo, punti, rispCorretta, risposte):
        self.testo=testo
        self.punti=punti
        self.rispCorretta=rispCorretta
        self.risposte=risposte

class Giocatore:
    def __init__(self, nickname, punti):
        self.nickname=nickname
        self.punti=punti

def main():
    DOMANDE = "domande.txt"
    ok = False
    while not ok:
        try:
            domande = leggi_file(DOMANDE)
            ok = True
        except OSError:
            print('Il file è sbagliato')
            file = input('Inserisci nome file: ')

    classifica = []
    continua = True
    while continua:
        livello = 0
        gioco = True

        while gioco:
            if livello == 5:
                gioco = False
            domandeLivello = []
            for d in domande:
                if livello==d.punti:
                    domandeLivello.append(d)

            d = random.choice(domandeLivello)
            print(f"Livello {livello})  {d.testo}")

            r = 0
            random.shuffle(d.risposte)
            for i, risp in enumerate(d.risposte):
                if (risp == d.rispCorretta):
                    r = i+1
                print(f"    {i+1}. {risp}")

            risposta = int(input("Inserisci la risposta (-1 per uscire dal gioco): "))

            if risposta == -1:
                continua = False
                gioco = False
                break


            if (risposta == r):
                livello += 1
                print("Risposta giusta!")
            else:
                gioco = False
        if continua:
            print(f"Hai totalizzato {livello} punti!")
            nome = input("Inserisci il tuo nickname: ")
            if nome == "":
                nome = input("Nickname non valido, inserisci il tuo nickname: ")

            punteggio = livello
            player = Giocatore(nome, punteggio)
            classifica.append(player)

    classificaOrdinaria = sorted(classifica, key=lambda elemento: elemento.punti, reverse = True)

    with open("punti.txt", "w", encoding="utf-8") as f:
        f.write("CLASSIFICA FINALE "+"\n")
        f.write("----------------------------------------------"+"\n")
        for p in classificaOrdinaria:
            # print(f"Player: {p.nickname} - score: {p.punti}")
            riga = p.nickname + " - " + str(p.punti)+ "\n"
            f.write(riga)
#non capisco




main()

