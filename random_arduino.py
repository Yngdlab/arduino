import serial

# Arduinoとのシリアル通信を開始
ser = serial.Serial('COM5', 9600)  # 'COM3' はArduinoが接続されているポート名です
# CDラインの状態を取得
cd_line = ser.cd
print(f'CDラインの状態: {cd_line}')

# CTSラインの状態を取得
cts_line = ser.cts
print(f'CTSラインの状態: {cts_line}')

# DSRラインの状態を取得
dsr_line = ser.dsr
print(f'DSRラインの状態: {dsr_line}')

try:
    while True:
        # Arduinoからデータを読み取り、デコードして表示
        data = ser.readline().decode('utf-8').strip()
        print("受信したデータ:", data)
except KeyboardInterrupt:
    # キーボードでCtrl+Cが押された場合にクリーンアップ
    ser.close()
