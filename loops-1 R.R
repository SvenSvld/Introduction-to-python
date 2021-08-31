for (i in 1:5){
  print(i^2)
}

#voor elk cijfer in de reeks 1 tot 5 
#print cijfer == i^2
# 1^2 = 1*1 = 1
# 2^2 = 2*2 = 4
# 3^2 = 3*3 = 9
# 4^2 = 4*4 = 16
# 5^2 = 5*5 = 25

for (i in c(-3,6,2,5,9)){
  print(i^2)
}


x = c(-3,6,2,5,9)
for (i in x){
  print(i^2)
}


Storage <- numeric(5)
for(i in 1:5){
  Storage[i]<-i^2
}


for(Temp in c(-4,5,10,-6,-40,30)){
  if(Temp > 0){
    print("warm")}
  else{
    print("not so warm")
  }
}



#nested for-loop
for (i in 1:3){
  for(j in 1:2){
    print(i+j)
  }
}



