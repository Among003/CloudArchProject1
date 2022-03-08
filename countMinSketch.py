import socket,os,time,random,struct,sys

#HOSTADDRESS = "10.10.1.1"
HOSTADDRESS = "192.168.222.128"
#HOSTADDRESS = "10.10.1.2"
PORT = 4444
SKETCH_H = 5
SKETCH_W = 5
COEFFICIENTS = 2

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
s.bind((HOSTADDRESS,PORT))
print("Connected")

class countMinSketch:
    def __init__(self):
        #create 5x5 sketch
        self.sketchArray = [[0]*SKETCH_W for _ in range(SKETCH_H)]
        self.hashCoefficients = [[0]*2 for _ in range(SKETCH_H)]
        #create hash variables
        for i in range(0, SKETCH_H):
            for j in range(0, COEFFICIENTS):
                self.hashCoefficients[i][j] =  random.randrange(1,15)
                print(str(self.hashCoefficients[i][j]) + " "+ str(i*5 +j))

    def addToSketch(self,ip):
        for i in range(0, SKETCH_H):
            calculatedHash = ((self.hashCoefficients[i][0] * int(ip)) + self.hashCoefficients[i][1]) % SKETCH_W
            print(calculatedHash)
            self.sketchArray[i][calculatedHash] = self.sketchArray[i][calculatedHash] + 1

    def returnMinCount(self,ip):
        print("do later")
        minFound = sys.maxsize
        for i in range(0, SKETCH_H):
            calculatedHash = ((self.hashCoefficients[i][0] * int(ip)) + self.hashCoefficients[i][1]) % SKETCH_W
            if (self.sketchArray[i][calculatedHash] < minFound):
                minFound = self.sketchArray[i][calculatedHash]
        return minFound

    def printSketch(self):
        for i in range(0, SKETCH_H):
            for j in range(0, SKETCH_W):
                print(self.sketchArray[i][j], end = ' ')
            print("")

def recievePacket():
    return s.recvfrom(65565)

def main():
    
    nonDuplicate = True;
    mySketch = countMinSketch()
    while (True):
        packet = recievePacket()[1][0].replace(".","")
        if (nonDuplicate):
            print(packet)
            mySketch.addToSketch(packet)
            mySketch.printSketch()
            print("Packets recieved from this source: " + str(mySketch.returnMinCount(packet)))
        nonDuplicate = not nonDuplicate
        
if __name__ == "__main__":
    main()



