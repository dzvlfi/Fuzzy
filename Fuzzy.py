def Emosi(emo):
	# 1 = low
	# 2 = med
	# 3 = medhigh
	# 4 = high
	if (0<=emo and 20>=emo):
		emosi1,cons1=1,1
		emosi2,cons2=0,2
	elif (20<emo and 30>emo):
		emosi1,cons1=(30.0-emo)/10.0,1
		emosi2,cons2=1-emosi1,2
	elif (30<=emo and 50>=emo):
		emosi1,cons1=1,2
		emosi2,cons2=0,3
	elif (50<emo and 60>emo):
		emosi1,cons1=(60-emo)/10.0,2
		emosi2,cons2=1-emosi1,3
	elif (60<=emo and 80>=emo):
		emosi1,cons1=1,3
		emosi2,cons2=0,4
	elif (80<emo and 90>emo):
		emosi1,cons1=(90-emo)/10.0,3
		emosi2,cons2=1-emosi1,4
	elif (90<=emo and 100>=emo):
		emosi1,cons1=0,3
		emosi2,cons2=1,4

	return emosi1,cons1,emosi2,cons2

def Provokasi(prov):
	if (0<=prov and 20>=prov):
		provo1,cons1=1,1
		provo2,cons2=0,2
	elif (20<prov and 30>prov):
		provo1,cons1=(30.0-prov)/10.0,1
		provo2,cons2=1-provo1,2
	elif (30<=prov and 50>=prov):
		provo1,cons1=1,2
		provo2,cons2=0,3
	elif (50<prov and 60>prov):
		provo1,cons1=(60-prov)/10.0,2
		provo2,cons2=1-provo1,3
	elif (60<=prov and 80>=prov):
		provo1,cons1=1,3
		provo2,cons2=0,4
	elif (80<prov and 90>prov):
		provo1,cons1=(90-prov)/10.0,3
		provo2,cons2=1-provo1,4
	elif (90<=prov and 100>=prov):
		provo1,cons1=1,4
		provo2,cons2=0,3

	return provo1,cons1,provo2,cons2

def FuzzyRules(emo,pro):
	# 0 = tidak
	# 1 = ya
	if (emo==1 and pro==1):
		return 0
	elif (emo==1 and pro==2):
		return 0
	elif (emo==1 and pro==3):
		return 0
	elif (emo==1 and pro==4):
		return 1
	elif (emo==2 and pro==1):
		return 0
	elif (emo==2 and pro==2):
		return 0
	elif (emo==2 and pro==3):
		return 0
	elif (emo==2 and pro==4):
		return 1
	elif (emo==3 and pro==1):
		return 0
	elif (emo==3 and pro==2):
		return 1
	elif (emo==3 and pro==3):
		return 1
	elif (emo==3 and pro==4):
		return 1
	elif (emo==4 and pro==1):
		return 0
	elif (emo==4 and pro==2):
		return 0
	elif (emo==4 and pro==3):
		return 1
	elif (emo==4 and pro==4):
		return 1

def Inference(emo1,econ1,emo2,econ2,pro1,pcon1,pro2,pcon2):
	y = {0:0,1:0,2:0,3:0}
	x = {0:0,1:0,2:0,3:0}
	iy,ix = 0,0

	if FuzzyRules(econ1,pcon1)==1:
		y[iy]=min(emo1,pro1)
		iy+=1
	else:
		x[ix]=min(emo1,pro1)
		ix+=1

	if FuzzyRules(econ1,pcon2)==1:
		y[iy]=min(emo1,pro2)		
		iy+=1
	else:
		x[ix]=min(emo1,pro2)
		ix+=1

	if FuzzyRules(econ2,pcon1)==1:
		y[iy]=min(emo2,pro1)		
		iy+=1
	else:
		x[ix]=min(emo2,pro1)
		ix+=1

	if FuzzyRules(econ2,pcon2)==1:
		y[iy]=min(emo2,pro2)
		iy+=1
	else:
		x[ix]=min(emo2,pro2)
		ix+=1

	return max(y[0],y[1],y[2],y[3]),max(x[0],x[1],x[2],x[3])

def Main():
	# HasilEmo = angka emosi
	# HasilECons = atribut emosi (kondisi)
	# HasilProv= angka provokasi
	# HasilPCons = atribut provokasi (kondisi)

	# Fuzzification
	emosi = input('Masukkan emosi: ')
	provokasi = input('Masukkan provokasi: ')
	HasilEmo1,HasilECons1,HasilEmo2,HasilECons2 = Emosi(emosi)
	HasilProv1,HasilPCons1,HasilProv2,HasilPCons2 = Provokasi(provokasi)

	#Inference
	y,x = Inference(HasilEmo1,HasilECons1,HasilEmo2,HasilECons2,HasilProv1,HasilPCons1,HasilProv2,HasilPCons2)

	#Defuzzification
	#sugeno, 40>= ya, else tidak
	result = (y*40)+(x*80)/(y+x)

	if result<=40:
		print "Hoax: ya"
	else:
		print "Hoax: tidak"

Main()