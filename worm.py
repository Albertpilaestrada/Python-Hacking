import sys
import shutil

def main():
    if len(sys.argv)==2:
        for n in range(0,int(sys.argv[1])):
            shutil.copy(sys.argv[0],sys.argv[0]+str(n)+'.py')
    else:
        print("Argumentos necesarios")

if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
