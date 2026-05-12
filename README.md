# 🖐️ Mão Robótica com MediaPipe e Arduino

Projeto de visão computacional e robótica utilizando Python, OpenCV, MediaPipe e Arduino para controlar uma mão robótica em tempo real através da detecção dos movimentos da mão humana.

---

# 📌 Sobre o Projeto

O sistema utiliza a webcam do computador para capturar os movimentos da mão do usuário.

A biblioteca MediaPipe realiza a detecção dos landmarks da mão e, com base na posição dos dedos, comandos são enviados para servomotores conectados a um Arduino.

Cada dedo da mão humana controla um servo SG90 correspondente na mão robótica.

---

# 🚀 Tecnologias Utilizadas

- Python 3.10
- OpenCV
- MediaPipe
- PyFirmata
- Arduino
- Servomotores SG90

---

# 🧠 Funcionamento

O MediaPipe Hands detecta 21 landmarks da mão em tempo real.

A lógica do projeto compara posições específicas desses pontos para identificar se cada dedo está aberto ou fechado.

Exemplo:

```python
distIndicador = pontos[5][1] - pontos[8][1]
```

Se a ponta do dedo estiver acima da base, considera-se o dedo levantado.

Os dados são então enviados para o Arduino utilizando PyFirmata.

---

# 📷 Demonstração

## Detecção da mão

- Rastreamento em tempo real
- Desenho automático dos landmarks
- Controle individual dos dedos

---

# 🔧 Estrutura do Projeto

```text
mao-robotica-mediapipe/
│
├── main.py
├── servo_braco3d.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Instalação

## 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/mao-robotica-mediapipe.git

cd mao-robotica-mediapipe
```

---

## 2. Instale o Python 3.10

O projeto foi desenvolvido e testado utilizando Python 3.10.

### Ubuntu/Debian

```bash
sudo apt install python3.10 python3.10-venv
```

---

## 3. Crie o ambiente virtual

```bash
python3.10 -m venv venv
```

---

## 4. Ative o ambiente virtual

### Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## 5. Instale as dependências

```bash
pip install -r requirements.txt
```

# ▶️ Execução

Conecte o Arduino e execute:

```bash
python main.py
```

---


# 👨‍💻 Autor

Desenvolvido para fins de estudo e experimentação em visão computacional e robótica.
Código baseado no repositório do Wellington Isac Souza
Repositório: https://github.com/WellingtonDev25/mao-robotica-mediapipe