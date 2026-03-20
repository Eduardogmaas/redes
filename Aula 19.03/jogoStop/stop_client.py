import socket
import json

HOST = "192.168.246.189"
PORT = 9006


def jogar():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))

        # Recebe letra e temas
        data = client.recv(4096)
        dados = json.loads(data.decode())

        letra = dados["letra"]
        temas = dados["temas"]

        print(f"\nLetra sorteada: {letra}")
        print("Preencha os temas:\n")

        respostas = {}

        for tema in temas:
            resposta = input(f"{tema}: ")
            respostas[tema] = resposta

        # Envia respostas
        client.sendall(json.dumps(respostas).encode())

        # Recebe pontuação
        resultado = client.recv(4096)
        pontuacoes = json.loads(resultado.decode())

        print("\n=== RESULTADO ===")
        for jogador, pontos in pontuacoes.items():
            print(f"Jogador {jogador}: {pontos} pontos")


if __name__ == "__main__":
    jogar()