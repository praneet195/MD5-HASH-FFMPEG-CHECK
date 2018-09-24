import os
import re
import sys
import cv2
import time
import hashlib 
import glob
import json
import ffmpeg as e
import np_opencv_module as npcv
import binascii as bn
import string
from string import printable
# source_file="rtsp://10.18.20.106/h264"

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""
if __name__=="__main__":
	f=open("hashmark12.txt","w")
	re1=re.compile("^([0][0][0][0][a-z||0-9][a-z||0-9][a-z||0-9][a-z||0-9][2][5])$")
	#re2=re.compile("^([0][0][0][0][a-z||0-9][a-z||0-9][a-z||0-9][a-z||0-9][2][5])$')
	i=0
	while(True):
		printable = set(string.printable)
		frame_num=0
		fmv=e.FMV(2,sys.argv[1])
		frame_dict={}
		fmv.connect(True)
		# print(fmv.getFPS())
		t1=time.time()
		
		frame_num=fmv.extract_frame_with_sei()
		while(frame_num==fmv.get_current_frame_number()):
			frame_num=fmv.extract_frame_with_sei()
			#cvmat=fmv.getMAT();#print(cvmat)
			#scaled_im = cv2.resize(cvmat, (608,608), interpolation = cv2.INTER_AREA)
			pkt_data=fmv.getPacketData();
			#if(pkt_data!="" and re1.match(pkt_data[304:314])):
			if(pkt_data!="" and re1.match(pkt_data[302:312])):
				i+=1
				#print pkt_data[310:]
				sei=fmv.getSEI()
				sei=sei.strip()
				sei=filter(lambda x: x in printable, sei)
				f.write(" HEX HASH: "+hashlib.md5(pkt_data[310:]).hexdigest()+" SEI MARKER: "+bn.unhexlify(sei)+"\n")
			if(i==1000):
				exit(0);
			# print bn.unhexlify(pkt_data)
			# mv=json.loads(fmv.getMV())
			# yolo_frame_data, vehicle_count=a.run_analytics(scaled_im, mv, timestamp)
			# cv2.imshow("Live Feed", cvmat)
			#cv2.imshow("Live Feed", scaled_im)
			#k = cv2.waitKey(10) & 0xFF
			#if k == ord('q'):
				#print("Exiting: You pressed 'q'")
		break
	
