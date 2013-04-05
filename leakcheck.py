import serial
import matplotlib.pyplot as plt

def decode_current_to_pressure(hex_current_data):
	"""
	Decodes the data coming off the rga from a value of A to torr.

	The RGA head measures an ion current and thus returns a value of current when queried. This value is a hex-encoded, little-endian int which represents a mantissa with an exponent of 1e-16 and in units of A. According to the RGA manual p. xiv, the the conversion factor is 2e-4 A/torr.
	"""
	return serial.struct.unpack("<i",hex_current_data)[0] * 1e-16 / 2e-4

# Set up the rga serial object.
rga = serial.Serial("/dev/cu.usbserial", timeout=1, baudrate=28800, \
	bytesize=8, stopbits=2, parity="N",rtscts=1)

# Intialize the hardware
# ----------------------
# Set electron energy to 70eV.
rga.write("ee70\r")
# Set ion energy to high value (12eV).
rga.write("ie1\r")
# Set the focus plate voltage to -100V.
rga.write("vf100\r")
# Switch on the filiment and set the electron emission current to 1.0mA.
rga.write("fl1.0\r")

# Set the CEDM voltage to 0, enabling Faraday cup operation.
rga.write("hv0\r")
# Take maximum averaging (slowest scan rate).
rga.write("nf0\r")
# Reset the zero of the detector.
rga.write("ca\r")

# Clear serial buffer after this initialization.
rga.readlines()

start_time = serial.time.time()

# Set the charge to mass ratio in amu.
# Note:
# He = 4
# N2 = 28
cmr = "4"

# Turn on interactive plotting and initialize the figure.
plt.ion()
fig = plt.figure()

# Look for He.
for indx in range(10):
	buffer = ""
	rga.write("mr" + cmr + "\r")

	# Hang out until the rga's buffer fills up with a legit value.
	while len(buffer) < 4:
	    buffer = buffer + rga.read(rga.inWaiting())

	# print decode_current_to_pressure(buffer)
	pressure = decode_current_to_pressure(buffer)
	plt.plot(serial.time.time() - start_time, pressure, "kx")
	plt.draw()
	# Hang out for a moment so matplotlib doesn't freak out.
	serial.time.sleep(0.05)
