path = input('Inpur URL')

def Eliminating_Background(path):
    mydir = os.getcwd()
    mydir_new = os.chdir(mydir+"/SemanticSegmentation")
    exec(open('./eval_v3.py').read())
    print ("Hello World!")
    output_images = output_images.save("Eliminated_background.jpg")
if __name__== "__main__":
  Eliminating_Background(path)
