import os 
import subprocess


def main():
  for root, dirs, files in os.walk('./CTCIQs'):
    flist = []
    for file in files:

      flist.append(
        (root + '/' + file, 
          os.path.getmtime( root + '/'+ file)
        ))


    max = 0

    for i in range(0,len(flist)):
      if flist[i][1] > flist[max][1]:
        max = i

    subprocess.run(['python',flist[max][0]])
    


if __name__=="__main__":
  main()