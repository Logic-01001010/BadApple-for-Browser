
import time

if __name__ == '__main__':

	frames = []

	for i in range(0, 4450+1):

		print('Load: ', i)
		f = open('frames/frame-'+str(i)+'.txt', 'r')
		

		frames.append(f.read())

	print('END!')
	time.sleep(3)

	for i in range(0, len(frames)):

		print( frames[i] )
		time.sleep(0.0001)
		