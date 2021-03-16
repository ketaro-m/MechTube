import sys
import pigpio

SERVO_PIN = 23

args = sys.argv

pi = pigpio.pi()
try:
	while(True):
		degree = int(input("Please input degree (0-270).\n"))
		if (degree > 270 or degree < 0):
			print("Degree range is 0-270")
			continue
		p_width = int(degree * 2000/270 + 500)
		print("Servo set", degree)
		pi.set_servo_pulsewidth(SERVO_PIN, p_width)
except KeyboardInterrupt:
	print("finish")
	pi.stop()
	pass

