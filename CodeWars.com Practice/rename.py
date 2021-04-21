import os
os.chdir('D:\Dropbox\Priv\Tavim\Piano + Organit\ABRSM Piano ALL\ABRSM Piano Grade 3\Abrsm Piano Grade 3 Exam Pieces 2021 - 2022')
# print(os.getcwd())
for f in os.listdir():
  file_name, file_ext = os.path.splitext(f)
  print (file_name,file_ext)
#   file_ext = ('.jpg')

#   # os.rename(f,file_ext)