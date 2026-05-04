import cv2
import mediapipe as mp
import servo_braco3d as mao


# 2. Configuração do MediaPipe (DEVE vir antes do loop)
hands = mp.solutions.hands
Hands = hands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

# 3. Configuração da Câmera
cap = cv2.VideoCapture(0)
cap.set(3, 640) # Largura
cap.set(4, 480) # Altura

print("Sistema iniciado. Pressione 'q' para sair.")

while True:
    success, img = cap.read()
    
    # 4. Proteção contra frame vazio
    if not success or img is None:
        continue

    frameRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = Hands.process(frameRGB)
    handPoints = results.multi_hand_landmarks
    h, w, _ = img.shape
    pontos = []

    if handPoints:
        for points in handPoints:
            mpDraw.draw_landmarks(img, points, hands.HAND_CONNECTIONS)
            
            for id, cord in enumerate(points.landmark):
                cx, cy = int(cord.x * w), int(cord.y * h)
                cv2.circle(img, (cx, cy), 4, (255, 0, 0), -1)
                pontos.append((cx, cy))

            if pontos:
                # Lógica dos dedos baseada nas coordenadas Y (ponto 0 é o pulso, valores menores são mais altos)
                # Dica: Para o indicador, se o ponto 8 (ponta) for menor que o 5 (base), o dedo está levantado.
                distPolegar = abs(pontos[17][0] - pontos[4][0])
                distIndicador = pontos[5][1] - pontos[8][1]
                distMedio = pontos[9][1] - pontos[12][1]
                distAnelar = pontos[13][1] - pontos[16][1]
                distMinimo = pontos[17][1] - pontos[20][1]

                # --- Envio para o Hardware ---
                # Polegar
                mao.abrir_fechar(10, 0 if distPolegar < 80 else 1)
                # Indicador
                mao.abrir_fechar(9, 1 if distIndicador >= 1 else 0)
                # Médio
                mao.abrir_fechar(8, 1 if distMedio >= 1 else 0)
                # Anelar
                mao.abrir_fechar(7, 1 if distAnelar >= 1 else 0)
                # Mínimo
                mao.abrir_fechar(6, 1 if distMinimo >= 1 else 0)

    cv2.imshow('Mao Robotica - MediaPipe', img)
    
    # 5. Sai do programa ao apertar 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
