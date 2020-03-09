def Eliminating_Background(path):
  mydir = os.getcwd()
  mydir_new = os.chdir(mydir+"/SemanticSegmentation")
  exec(open('./eval_v2.py --trained_model=./SemanticSegmentation/weights/yolact_plus_resnet50_54_800000.pth --config=yolact_plus_resnet50_config --score_threshold=0.15 --top_k=15 --display_masks=true --display_bboxes=false --display_text=false --images=test_images:output_images').read())
  print ("Hello World!")
  output_images = output_images.save("Eliminated_background.jpg") 
if __name__== "__main__":
  Eliminating_Background()