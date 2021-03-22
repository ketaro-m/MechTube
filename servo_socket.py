import sys
import pigpio
import socket

SERVO_PIN = 23

args = sys.argv

pi = pigpio.pi()
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # IPアドレスとポートを指定
        s.bind(('', 4041))
        # 1 接続
        s.listen(1)
        # connection するまで待つ
        while True:
            # 誰かがアクセスしてきたら、コネクションとアドレスを入れる
            print("wait connection")
            conn, addr = s.accept()
            with conn:
                print("connected")
                while True:
                    # データを受け取る
                    data = conn.recv(1024)
                    print(type(data))
                    if not data:
                        break
                    print('data : {}, addr: {}'.format(data, addr))
                    # クライアントにデータを返す(b -> byte でないといけない)
                    degree = int(data.decode())
                    print(degree)
                    if (degree > 270 or degree < 0):
                        print("Degree range is 0-270")
                        continue
                    p_width = int(degree * 2000/270 + 500)
                    print("Servo set", degree)
                    pi.set_servo_pulsewidth(SERVO_PIN, p_width)
                    print("Servo set done")
except KeyboardInterrupt:
	print("finish")
	pi.stop()
	pass


