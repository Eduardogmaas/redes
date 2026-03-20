import socket
import threading
import random
import json

HOST = "192.168.246.189"
PORT = 9006
NUM_JOGADORES = 3

TEMAS = ["Nome", "CEP", "Animal", "Fruta", "Cor", "Anime", "Objeto", "Carro"]

clientes = []
respostas_jogadores = {}
lock = threading.Lock()
todos_responderam = threading.Event()


def sortear_letra():
    return random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


def calcular_pontuacao():
    pontuacoes = {i: 0 for i in range(len(clientes))}

    for tema in TEMAS:
        respostas_tema = []

        # Coleta respostas daquele tema
        for i in respostas_jogadores:
            respostas_tema.append(respostas_jogadores[i][tema].lower())

        # Conta frequência
        for i in respostas_jogadores:
            resposta = respostas_jogadores[i][tema].lower()

            if respostas_tema.count(resposta) == 1:
                pontuacoes[i] += 3
            else:
                pontuacoes[i] += 1

    return pontuacoes


def atender_cliente(conn, addr, player_id):
    print(f"[Server] Jogador {player_id} conectado: {addr}")

    # Espera todos conectarem
    while len(clientes) < NUM_JOGADORES:
        pass

    # Recebe respostas
    data = conn.recv(4096)
    respostas = json.loads(data.decode())

    with lock:
        respostas_jogadores[player_id] = respostas
        print(f"[Server] Respostas recebidas do jogador {player_id}")

        if len(respostas_jogadores) == NUM_JOGADORES:
            todos_responderam.set()

    # Espera todos responderem
    todos_responderam.wait()

    # Calcula pontuação
    pontuacoes = calcular_pontuacao()

    # Envia resultado
    conn.sendall(json.dumps(pontuacoes).encode())

    conn.close()


def iniciar_servidor():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()

        print(f"[Server] Aguardando {NUM_JOGADORES} jogadores...")

        # Aceita jogadores
        while len(clientes) < NUM_JOGADORES:
            conn, addr = server.accept()
            clientes.append(conn)

        print("[Server] Todos os jogadores conectados!")

        # Sorteia letra
        letra = sortear_letra()
        print(f"[Server] Letra sorteada: {letra}")

        # Envia letra e temas
        dados_iniciais = {
            "letra": letra,
            "temas": TEMAS
        }

        for conn in clientes:
            conn.sendall(json.dumps(dados_iniciais).encode())

        # Cria threads para cada jogador
        for i, conn in enumerate(clientes):
            thread = threading.Thread(
                target=atender_cliente,
                args=(conn, conn.getpeername(), i),
                daemon=True
            )
            thread.start()

        # Mantém servidor vivo
        while True:
            pass


if __name__ == "__main__":
    iniciar_servidor()